import streamlit as st
from summarizer_logic import get_summary

# ✅ Set yellow background using URL
def set_background_from_url(image_url: str):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Set background image (yellow background)
set_background_from_url("https://www.shutterstock.com/image-photo/back-school-concept-frame-border-600nw-2324631629.jpg")

# ✅ Apply stylish font + custom colors (Updated textarea)
st.markdown("""
    <style>
    /* Import stylish font from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif;
    }

    .stTextArea textarea {
        color: #000000 !important;            /* 🔧 Black text */
        background-color: #f5f5f5 !important; /* 🔧 Light grey background */
        font-weight: bold;
        font-size: 16px;
        border-radius: 10px;
    }

    .custom-summary {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        color: #000000;
        font-size: 18px;
        font-weight: 500;
    }

    .stButton button {
        background-color: #8B0000;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5em 1em;
        font-size: 16px;
    }

    .stButton button:hover {
        background-color: #a80000;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ App Title and Instructions
st.markdown('<h1 style="color:#8B0000;">📝 LLM-Powered Text Summarizer</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#006400; font-size:18px;">Paste a paragraph below and click "Summarize" to get a short summary.</p>', unsafe_allow_html=True)

# ✅ Input Text Area
input_text = st.text_area("🔽 Paste your text here:", height=200)

# ✅ Summarize Button Logic
if st.button("Summarize"):
    if input_text.strip():
        with st.spinner("Summarizing..."):
            summary = get_summary(input_text)
        st.success("✅ Summary:")
        st.markdown(f'<div class="custom-summary">{summary}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter some text first.")

# ✅ Clear Button
if st.button("Clear"):
    st.rerun()
