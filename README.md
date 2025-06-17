# 🩺 Arabic Medical Chatbot

An open-source AI chatbot that conducts smart, multi-turn medical interviews with Arabic-speaking patients. It uses prompt engineering and transformer models to ask relevant questions, analyze answers, and decide when the conversation has collected enough information.

🎓 **This project was developed as my graduation project.**

## 🚀 Features

* 💬 Conversational flow in Arabic
* 🤖 Few-shot Prompt Engineering for medical Q\&A
* 🧠 Custom logic to detect vague or redundant replies
* ⚡ FastAPI backend for API integration
* 🗃️ Modular codebase for easy customization and scaling

---

## 🗂️ Project Structure

| File                     | Description                                     |
| ------------------------ | ----------------------------------------------- |
| `main.py`                | Entry point for running the chatbot server      |
| `api_server.py`          | FastAPI-based API to serve chatbot interactions |
| `medical_session.py`     | Manages the conversation logic and state        |
| `translation_service.py` | Handles translation tasks if needed             |
| `model_loader.py`        | Loads and configures the transformer model      |
| `config.py`              | Contains configuration parameters               |
| `requirements.txt`       | Python dependencies                             |

---

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/diaaeldinmahmoud/medical-chatbot.git
cd medical-chatbot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the API server:

```bash
python main.py
```

---

🔌 Try the API (Live Demo)
You can test the chatbot live using Swagger UI via the  link you got after running  (python main.py):


Example: 🌐 https://a5e8-34-142-184-39.ngrok-free.app/docs

This opens the interactive API documentation where you can:

Start a new session

Send user messages

Export conversation history

🧪 Example Request
Go to the /chat endpoint

Click "Try it out"

Paste a JSON body like:

json
Copy
Edit
{
  "session_id": "session123",
  "user_message": "عندي وجع في المعدة"
}
Click "Execute"

Read the chatbot's Arabic response in the bot_message field

✅ Use this to simulate a real conversation with the AI agent!



---

## 🧠 How It Works

* The chatbot interacts in Arabic using a transformer-based language model.
* Each patient message is scored for confidence and information coverage.
* The bot dynamically decides whether to continue asking questions or end the conversation.

---

## 🌍 Vision

This project is a step toward building AI tools that support Arabic-language users in healthcare settings, replacing rigid form-based systems with empathetic, intelligent dialogue.

---





