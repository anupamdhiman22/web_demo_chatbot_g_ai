# def retrieve_context(query, documents):
#     query = query.lower()

#     for doc in documents:
#         if any(word in doc.lower() for word in query.split()):
#             return doc

#     return "No relevant information found."


from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
