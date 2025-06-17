# 🩺 Arabic Dermatology Chatbot
An open-source, AI-powered Arabic chatbot for dermatology that simulates intelligent medical interviews with patients. It understands symptoms, asks relevant follow-up questions, and knows when to end the conversation — all in natural Arabic.

🎓 This project was developed as my graduation project in the field of AI and medical NLP.

## 🚀 Features

* 💬 Conversational flow in Arabic
* 🤖 Few-shot Prompt Engineering for medical Q\&A
* 🧠 Custom logic to detect vague or redundant replies
* ⚡ FastAPI backend for API integration
* 🗃️ Modular codebase for easy customization and scaling

---
## 💡 Project Overview
Skin-related issues are among the most common reasons people seek medical advice — but Arabic speakers often lack accessible, intelligent tools. This chatbot provides a dermatology-focused medical interview experience, designed to:

* Collect patient symptoms in Arabic

* Ask medically relevant, targeted follow-up questions

* Stop the conversation automatically when enough data is collected

The goal is to replicate the logic of a dermatology consultation, powered by NLP.

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

## 📊 How It Works

*Uses a few-shot prompt to simulate a dermatology consultation

*Tracks which symptoms or clinical information have been covered


---
## 🧪 Common Topics Covered
حب الشباب (Acne) *

الإكزيما (Eczema)*

التينيا والفطريات (Fungal infections)*

الطفح الجلدي (Rashes)*


You can easily expand the supported conditions via the prompt template or logic.
---
## 👨‍⚕️ Vision
This chatbot is a step toward making dermatological advice more accessible for Arabic speakers, especially in underserved areas. It can be used in telehealth triage, virtual clinics, or awareness apps.

---





