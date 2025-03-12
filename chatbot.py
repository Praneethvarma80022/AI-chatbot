import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Fix SSL issue for nltk downloads
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("C:/Projects/Personal/Chatbot_using_NLP_AICTE_Cycle4/intents.json")
if not os.path.exists(file_path):
    st.error("Error: 'intents.json' file not found. Please check the file path.")
    st.stop()

with open(file_path, "r") as file:
    intents = json.load(file)

# Vectorizer and Classifier
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot_response(user_input):
    input_vector = vectorizer.transform([user_input])
    tag = clf.predict(input_vector)[0]
    for intent in intents:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

# Create conversation log file if not exists
log_file = 'chat_log.csv'
if not os.path.exists(log_file):
    with open(log_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

def save_chat_history(user_input, response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([user_input, response, timestamp])

def load_chat_history():
    history = []
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header
            for row in csv_reader:
                history.append(row)
    return history

def main():
    st.set_page_config(page_title="AI Chatbot", layout="wide")
    st.sidebar.image("chatbot.png", width=200)
    st.sidebar.title("Navigation")
    menu = ["Chat", "Conversation History", "About"]
    choice = st.sidebar.radio("Go to", menu)

    if choice == "Chat":
        st.title("🤖 AI Chatbot")
        st.write("Ask me anything!")
        
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        user_input = st.chat_input("Type your message here...")
        if user_input:
            response = chatbot_response(user_input)
            
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            with st.chat_message("user"):
                st.markdown(user_input)
            with st.chat_message("assistant"):
                st.markdown(response)
            
            save_chat_history(user_input, response)
    
    elif choice == "Conversation History":
        st.title("📜 Conversation History")
        history = load_chat_history()
        if history:
            for entry in reversed(history):
                st.markdown(f"**🗣 User:** {entry[0]}")
                st.markdown(f"**🤖 Chatbot:** {entry[1]}")
                st.caption(f"🕒 {entry[2]}")
                st.divider()
        else:
            st.info("No conversation history available.")

    elif choice == "About":
        st.title("📌 About the Chatbot")
        st.write(
            "This chatbot uses NLP and Logistic Regression to understand and respond to user queries."
        )
        st.markdown("### 🔍 Features")
        st.write("✔️ AI-powered responses using machine learning")
        st.write("✔️ Interactive chat interface")
        st.write("✔️ Conversation history tracking")
        st.write("✔️ Streamlit-powered web UI")

if __name__ == '__main__':
    main()
