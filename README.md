# 📝 LLM-Powered Text Summarizer

This is a Streamlit web app that uses a pre-trained **BART Transformer** model to summarize input text into concise, meaningful summaries.

## 🚀 Features
- 🧠 Uses `facebook/bart-large-cnn` from Hugging Face for summarization
- 🎨 Custom background, fonts, and styles
- ⚡ Fast, clean and interactive UI via Streamlit
- 🧾 Button to summarize and clear inputs

## 🧠 Model Used
- **facebook/bart-large-cnn**
- Pretrained on CNN/DailyMail dataset
- Performs **abstractive summarization**

## 🗂️ Project Structure
├── app.py # Streamlit front-end
├── summarizer_logic.py # BART summarizer logic
└── requirements.txt # Required Python packages

## 📦 Installation

Install dependencies:
```bash
pip install -r requirements.txt

