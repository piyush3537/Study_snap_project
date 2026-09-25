# modules/flashcard_gen.py
from transformers import pipeline
qa_gen = pipeline("question-generation")

def generate_flashcards(text):
    return qa_gen(text)
