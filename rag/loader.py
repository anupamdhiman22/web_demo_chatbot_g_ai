import os

def load_documents(folder_path="data/doc"):
    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                documents.append(f.read())

    return documents
