from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv()

# Get API Key
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Client
client = genai.Client(api_key=API_KEY)

# Flask app
app = Flask(__name__)

# RAG imports
from rag.loader import load_documents
from rag.retriever import retrieve_context

# Load documents once
documents = load_documents()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Retrieve context using RAG
    context = retrieve_context(user_message, documents)

    # Prompt
    prompt = f"""
You are a helpful assistant.
Use the following context to answer the question.

Context:
{context}

Question:
{user_message}
"""

    # Gemini response
    response = client.models.generate_content(
        model="gemini-1.0-pro",
        contents=prompt
    )

    return jsonify({"reply": response.text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
