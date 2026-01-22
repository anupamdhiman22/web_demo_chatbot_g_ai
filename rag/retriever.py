def retrieve_context(query, documents):
    query = query.lower()

    for doc in documents:
        if any(word in doc.lower() for word in query.split()):
            return doc

    return "No relevant information found."
