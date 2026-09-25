# modules/qa_engine.py
from transformers import pipeline
qa = pipeline("question-answering")

def answer_question(context, question):
    return qa(question=question, context=context)['answer']
