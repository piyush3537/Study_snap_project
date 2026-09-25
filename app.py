import streamlit as st
from modules import ocr 
from modules import summarizer, qa_engine

st.title("📚 StudySnap – Your AI Study Assistant")

option = st.sidebar.selectbox("Choose a feature", 
    ["OCR", "Summarize", "Flashcards", "Translate", "Ask Notes", "Lecture to Text"])

if option == "OCR":
    file = st.file_uploader("Upload image")
    if file:
        text = ocr.extract_text(file)
        st.text_area("Extracted Text", text)
elif option == "Summarize":
    input_text = st.text_area("Enter text")
    if st.button("Summarize"):
        summary = summarizer.summarize_text(input_text)
        st.success(summary)
elif option == "Ask Notes":
    context = st.text_area("Paste your notes")
    question = st.text_input("Your question")
    if st.button("Answer"):
        ans = qa_engine.answer_question(context, question)
        st.success(ans)
