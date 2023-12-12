# OP Stack

The OpenAI Pinecone (OP) stack is an increasingly popular choice for building high-performance AI apps, including retrieval-augmented GQA.

Our pipeline during query time consists of the following:

1. OpenAI Embedding endpoint to create vector representations of each query.

https://platform.openai.com/docs/guides/embeddings

https://platform.openai.com/docs/api-reference/embeddings 
2. Pinecone vector database to search for relevant passages from the database of previously indexed contexts.
3. OpenAI Completion endpoint to generate a natural language answer considering the retrieved contexts.
https://www.pinecone.io/learn/openai-gen-qa/

Canopy:
Retrieval Augmented Generation (RAG) framework and context engine powered by Pinecone

https://github.com/pinecone-io/canopy

