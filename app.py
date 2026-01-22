from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from google import genai

from rag.loader import load_documents
from rag.retriever import retrieve_context

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

app = Flask(__name__)

# Load RAG documents once
documents = load_documents()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    context = retrieve_context(user_message, documents)

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{user_message}
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
