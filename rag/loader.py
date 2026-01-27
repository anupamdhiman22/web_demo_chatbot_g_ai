# import os

# def load_documents(folder_path="data/doc"):
#     documents = []

#     for file in os.listdir(folder_path):
#         if file.endswith(".txt"):
#             with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
#                 documents.append(f.read())

#     return documents

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def load_and_index_documents(folder_path="data/doc"):
    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                documents.append(f.read())

    # ✅ Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text("\n".join(documents))

    # ✅ Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # ✅ Vector Store
    vectorstore = FAISS.from_texts(chunks, embeddings)
    vectorstore.save_local("vector_store")

    print("✅ Documents indexed successfully")

if __name__ == "__main__":
    load_and_index_documents()
