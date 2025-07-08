# summarizer_logic.py

from transformers import pipeline

# ✅ Load summarization pipeline using a pretrained model
# This automatically uses CPU if no GPU is available
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

def get_summary(text):
    """
    Summarize the input text using a pre-trained BART model.
    Returns a summarized string.
    """
    if not text.strip():
        return "⚠️ Please provide valid text."

    # Run summarization
    result = summarizer(
        text,
        max_new_tokens=100,   # ✅ Only set this, not max_length
        do_sample=False       # 🔒 Disable randomness for consistent output
    )

    # Extract summary text
    summary_text = result[0]['summary_text']
    return summary_text
