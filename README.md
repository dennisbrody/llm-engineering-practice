
# Bible Verse Summarizer

This project is a web-based Bible verse summarizer built with Gradio and OpenAI's GPT-4. Users can enter a book, chapter, and verse from the Bible and receive both a plain-language summary and a scholarly interpretation.

## Features

- Fetches the actual verse text using the [Bible API](https://bible-api.com/)
- Uses OpenAI GPT-4 to generate meaningful summaries and theological interpretations
- Clean, shareable Gradio interface

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/bible-verse-summarizer.git
cd bible-verse-summarizer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
OPENAI_API_KEY=your-openai-api-key
```

### 4. Run the app

```bash
python app.py
```

It will launch a Gradio interface and give you a shareable link.

## Tech Stack

- Python
- Gradio
- OpenAI GPT-4
- Requests
- dotenv
- Bible API

## Example Prompt

> Book: John  
> Chapter: 3  
> Verse: 16  

---

> "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."

The app will return a summary and scholarly breakdown of this verse.

## License

MIT License
