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

## 🔌 API Usage

* **Endpoint:** `/chat`
* **Method:** `POST`
* **Payload Example:**

```json
{
  "session_id": "abc123",
  "user_message": "عندي صداع ودوخة"
}
```

* **Response:**

```json
{
  "bot_message": "من قد إيه بتحس بالصداع؟",
  "finished": false
}
```

---

## 🧠 How It Works

* The chatbot interacts in Arabic using a transformer-based language model.
* Each patient message is scored for confidence and information coverage.
* The bot dynamically decides whether to continue asking questions or end the conversation.

---

## 🌍 Vision

This project is a step toward building AI tools that support Arabic-language users in healthcare settings, replacing rigid form-based systems with empathetic, intelligent dialogue.

---





