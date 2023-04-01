import os
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

intents = [
    {
    "tag": "greeting",
    "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"],
    "responses": ["Hi there", "Hello", "Hey", "I'm fine, thank you","Nothing much"]
    },
    {
    "tag":"goodbye",
    "patterns":["Bye", "See you later", "Goodbye", "Take care"],
    "responses": ["Goodbye", "See you later", "Take care"]
    },
    {
    "tag": "thanks",
    "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"],
    "responses": ["You're welcome", "No problem", "Glad I could help"]
    },
    {
    "tag": "about",
    "patterns": ["What can you do", "Who are you", "What are you", "What is your purpose"],
    "responses": ["I am a chatbot that can give information about Soufiane Lamchoudi", "My purpose is to assist you to know more Soufiane Lamchodui", "I can answer questions and provide assistance about Soufiane Lamchoudi"]
    },
    {
    "tag": "help",
    "patterns": ["Help", "I need help", "Can you help me", "What should I do"],
    "responses": ["Sure, what do you need help with?", "I'm here to help. What's the problem?", "How can I assist you?"]
    }
]

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)