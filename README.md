Absolutely! Here's the updated `README.md` with the **"Option 2: Terminal Test"** step included under the `⚡ Run the Chatbot` section:

---

# 🤖 AI Chatbot using NLP & LLaMA (Streamlit + Ollama)

This project is an **AI-powered chatbot** that combines **Natural Language Processing (NLP)** techniques with **local Large Language Models (LLMs)** like **LLaMA 3.2** via [Ollama](https://ollama.com). The chatbot provides intelligent and context-aware responses using both **intent classification** and **language model inference**, making interactions more human-like and dynamic.

---

## 📌 Features

* **🧠 Natural Language Understanding (NLU):** Processes and interprets user input
* **⚙️ Machine Learning Integration:** Uses TF-IDF + Logistic Regression to detect intent
* **💬 LLaMA 3.2 Model via Ollama:** Generates real-time AI responses from a local LLM
* **📚 Custom Intents:** Easily customizable with your own `intents.json`
* **🗃️ Chat History:** Logs all conversations with timestamps in CSV format
* **🌐 Streamlit Interface:** Clean, modern, and interactive UI

---

## 🛠 Technologies Used

* **Python 3.8+**
* **Streamlit** – Web UI
* **NLTK** – Text preprocessing
* **scikit-learn** – Intent classification
* **Ollama** – LLaMA 3.2 model inference
* **CSV** – Conversation logging

---

## 🚀 Installation

### 1. Clone the repository:

```bash
git clone https://github.com/Praneethvarma80022/AI-chatbot.git
cd AI-chatbot
```

### 2. Create a virtual environment (optional but recommended):

```bash
python -m venv chatbot_env
chatbot_env\Scripts\activate  # Windows
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚡ Run the Chatbot

### ✅ Step 1: Start Ollama Server

```bash
ollama serve
```

---

### ✅ Step 2: Verify Ollama is Running (Terminal Test)

Run the following command in a new terminal window:

```bash
curl http://localhost:11434/api/tags
```

If Ollama is running, you’ll receive a list of available models like:

```json
{"models":[{"name":"llama3.2:latest", "size":"2.0 GB"}, ...]}
```

This confirms the server is active and ready to serve responses.

---

### ✅ Step 3: Run the LLaMA Model

```bash
ollama run llama3.2
```

---

### ✅ Step 4: Launch the Streamlit Chatbot App

```bash
streamlit run chatbot_app.py
```

Access it at: [http://localhost:8501](http://localhost:8501)

---

## 💬 Example Interaction

```
User: Hello!
Chatbot: Hi! How can I assist you today?

User: What is AI?
Chatbot: AI stands for Artificial Intelligence, which enables machines to learn and perform tasks that typically require human intelligence.
```

---

## 🧠 Customization

* Modify `intents.json` to define your own intents and patterns.
* Update the `chatbot_app.py` logic to change how fallback responses are handled.
* Replace `llama3.2` with another Ollama-supported model like `mistral`, `gemma`, or `tinyllama`.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added a new feature"`)
4. Push to GitHub (`git push origin feature-branch`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

⭐ **Star this repo** if you found it useful!
🚀 Build your own AI assistant locally with full control over the model and interface.

---

Let me know if you'd like me to turn this into a Markdown file you can directly upload to GitHub.
