# llm-codebase-expert
## Description
This project is made as a tool to query codebases with natural language using LLMs

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Overview](#overview)

## Installation

source ./install_deps.sh

## Usage

source ./execute.sh

After model downloads, documents splits and embeddings generations you will go into interactive mode: 

(Example using this codebase: https://github.com/V-Gutierrez/genesisapp-be)
<img width="1202" alt="image" src="https://github.com/V-Gutierrez/llm-codebase-expert/assets/62355596/631bba51-0aa0-4b88-8626-16afef28a555">
<img width="1077" alt="image" src="https://github.com/V-Gutierrez/llm-codebase-expert/assets/62355596/edc85e3c-63ed-42f0-a93f-1fd334e8ca0b">



## Features

Features

- Natural Language Queries: Ask questions about your codebase in plain English and receive accurate, context-aware answers.
- Dynamic Codebase Analysis: Automatically reads and analyzes your codebase, ensuring that the information provided is always up to date.
- Advanced Language Processing: Utilizes HuggingFaceEmbeddings for generating embeddings and Chroma for efficient storage and retrieval of vectorized documents.
- Conversational AI Integration: Employs a ConversationalRetrievalChain that integrates a HuggingFace language model with the retrieval system, enabling a seamless question-and-answer experience.

This tool is built using the following key components:

- HuggingFaceEmbeddings & Transformers: For processing natural language queries and generating text-based responses.
- Chroma Vector Store: For efficient storage and retrieval of document embeddings, enabling quick access to relevant code snippets.
- ConversationalRetrievalChain: A custom pipeline that combines language understanding and retrieval capabilities to provide precise answers to user queries.

## Overview

Starting Models used: "stabilityai/stable-code-3b" for text-generation and "krlvi/sentence-t5-base-nlpl-code-x-glue" for embeddings
