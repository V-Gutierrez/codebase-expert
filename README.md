# llm-codebase-expert

## Description
The llm-codebase-expert project is a sophisticated tool designed to facilitate querying codebases using natural language, powered by the latest advancements in Large Language Models (LLMs). This tool bridges the gap between complex codebases and users by allowing natural language interactions, significantly enhancing the accessibility and understanding of code.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technical Overview](#technical-overview)
- [Starting Models](#starting-models)
- [Contributing](#contributing)

## Installation

To set up llm-codebase-expert, run the following commands:

```bash
source ./install_deps.sh
```

This script will install all necessary dependencies to ensure the tool is ready for use.

## Usage

Initiate the tool with:

```bash
source ./execute.sh
```

Upon completion of model downloads, document splitting, and embeddings generation, you will enter an interactive mode that allows for natural language queries about your codebase.

### Interactive Mode Screenshots

Here are some examples of the tool in action using the GenesisApp codebase:

![Example Interaction 1](https://github.com/V-Gutierrez/llm-codebase-expert/assets/62355596/631bba51-0aa0-4b88-8626-16afef28a555)

![Example Interaction 2](https://github.com/V-Gutierrez/llm-codebase-expert/assets/62355596/edc85e3c-63ed-42f0-a93f-1fd334e8ca0b)

## Features

- **Natural Language Queries:** Engage with your codebase using plain English questions and receive precise, context-aware answers.
- **Dynamic Codebase Analysis:** Automatically reads and analyzes your codebase, ensuring up-to-date information.
- **Advanced Language Processing:** Leverages HuggingFaceEmbeddings for generating code-specific embeddings.
- **Conversational AI Integration:** Utilizes a ConversationalRetrievalChain, integrating a HuggingFace language model with the retrieval system for seamless interaction.
- **RAG (Retrieval-Augmented Generation):** Enhances responses by combining the power of retrieval from Chroma Vector Store with the generative capabilities of LLMs.

## Technical Overview

The llm-codebase-expert utilizes the following technologies:

- **LangChain:** For orchestrating the interaction between different AI components.
- **HuggingFaceEmbeddings & Transformers:** For processing natural language queries and generating text-based responses.
- **Chroma Vector Store:** Efficiently stores and retrieves document embeddings, enabling quick access to relevant information.
- **ConversationalRetrievalChain:** Combines language understanding and retrieval capabilities to provide precise answers.

## Starting Models

- **Text Generation:** `stabilityai/stable-code-3b`
- **Embeddings:** `krlvi/sentence-t5-base-nlpl-code-x-glue`

These models form the backbone of the system, handling the generation of context-aware responses and the creation of embeddings for efficient document retrieval.

## Contributing

We welcome contributions! If you have suggestions for improvements or want to contribute code, please feel free to make a pull request or open an issue

By combining the strengths of RAG, advanced embeddings, and Chroma Vector Store, llm-codebase-expert offers an unparalleled tool for interacting with codebases through natural language, streamlining the process of understanding and navigating complex code.
