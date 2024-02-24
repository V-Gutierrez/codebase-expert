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

## Overview

Language Processing: Utilizes HuggingFaceEmbeddings for generating embeddings and Chroma for storing and retrieving vectorized documents.

Conversational AI: Employs a ConversationalRetrievalChain that integrates a HuggingFace language model with the retrieval system to provide accurate answers.

Codebase Interaction: Reads and analyzes the codebase dynamically, ensuring that users have access to the most current information.

