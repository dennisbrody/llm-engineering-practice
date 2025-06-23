
import os
import requests
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

# Load API keys from .env
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

# Initialize OpenAI client
openai_client = OpenAI(api_key=openai_api_key)

# Optional: Fetch verse using a free Bible API
def fetch_verse(book: str, chapter: str, verse: str) -> str:
    url = f"https://bible-api.com/{book}+{chapter}:{verse}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("text", "Verse not found.").strip()
    return "Error fetching verse."

# Main LLM function
def summarize_and_interpret(book: str, chapter: str, verse: str) -> str:
    verse_text = fetch_verse(book, chapter, verse)

    prompt = f"""
    The following is a verse from the Bible: "{verse_text}" 
    (Book: {book}, Chapter: {chapter}, Verse: {verse}).

    1. Summarize this verse in simple terms.
    2. Provide a scholarly interpretation of its meaning, referencing common theological perspectives.
    """

    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Gradio UI
iface = gr.Interface(
    fn=summarize_and_interpret,
    inputs=[
        gr.Textbox(label="Book of the Bible (e.g., John)"),
        gr.Textbox(label="Chapter (e.g., 3)"),
        gr.Textbox(label="Verse (e.g., 16)")
    ],
    outputs=gr.Textbox(label="Summary and Interpretation"),
    title="📖 Bible Verse Summarizer",
    description="Enter a book, chapter, and verse to get a summary and scholarly interpretation.",
)

# Launch public Gradio app
iface.launch(share=True)
