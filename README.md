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


## Overview

Language Processing: Utilizes HuggingFaceEmbeddings for generating embeddings and Chroma for storing and retrieving vectorized documents.

Conversational AI: Employs a ConversationalRetrievalChain that integrates a HuggingFace language model with the retrieval system to provide accurate answers.

Codebase Interaction: Reads and analyzes the codebase dynamically, ensuring that users have access to the most current information.

