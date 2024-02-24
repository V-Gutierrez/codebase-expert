import os
from langchain.docstore.document import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain import HuggingFacePipeline, PromptTemplate
import transformers
from langchain.chains import ConversationalRetrievalChain

folder_name = "sample_code"
target_repository = os.getenv("TARGET_REPOSITORY", "https://github.com/V-Gutierrez/genesisapp-be")

os.system(f"git clone {target_repository} {folder_name}")

documents = []

print("Reading files...")
for root, dirs, files in os.walk(folder_name):
    for file in files:
        try:
            with open(os.path.join(root, file), "r", encoding="utf-8") as o:
                code = o.readlines()
                d = Document(page_content="\n".join(code), metadata={"source": os.path.join(root, file)})
                documents.append(d)
        except UnicodeDecodeError:
            # some files are not utf-8 encoded; let's ignore them for now.
            pass


print("Creating vector store...")
huggingface_embeddings = HuggingFaceEmbeddings(model_name="krlvi/sentence-t5-base-nlpl-code-x-glue")
persist_directory = "db"

db = Chroma.from_documents(documents, huggingface_embeddings, persist_directory=persist_directory)
db.persist()

retriever = db.as_retriever()

print("Creating pipeline...")
model_id = "stabilityai/stable-code-3b"
config = transformers.AutoConfig.from_pretrained(model_id,trust_remote_code=True)
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
model = transformers.AutoModelForCausalLM.from_pretrained(model_id, config=config, trust_remote_code=True)

pipe = transformers.pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=200)
pipe.model.config.pad_token_id = pipe.model.config.eos_token_id

llm = HuggingFacePipeline(pipeline=pipe)

qa_chain = ConversationalRetrievalChain.from_llm(llm=llm,retriever=retriever,return_source_documents=True)
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    user_question = input("Make your question about the codebase: \n")
    
    if user_question.lower() == 'quit': 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Goodbye!")
        break
    
    print("Answering...")
    result = qa_chain({"question":user_question, "chat_history":[]})
    print(f"Answer: {result['answer']}")
    print(f"Sources: {[x.metadata['source'] for x in result['source_documents']]}")