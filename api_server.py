from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, List, Any
import uvicorn
from pyngrok import ngrok
import nest_asyncio
from medical_session import MedicalSession
from translation_service import TranslationService, TranslateModel
from config import NGROK_AUTH_TOKEN

class ChatRequest(BaseModel):
    message: str

class APIServer:
    def __init__(self, tokenizer, model, device):
        self.app = FastAPI(title="Medical Chatbot API")
        self.sessions: Dict[str, MedicalSession] = {}
        self.tokenizer = tokenizer
        self.model = model
        self.device = device
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.post("/chat/{session_id}")
        def chat_with_doctor(session_id: str, request: ChatRequest):
            if session_id not in self.sessions:
                self.sessions[session_id] = MedicalSession()
            session = self.sessions[session_id]
            response = session.process_input(request.message, self.tokenizer, self.model, self.device)
            return {
                "response": response,
                "finished": str(session.finished),
                "full_conversation": session.messages
            }

        @self.app.get("/export/{session_id}")
        def export_session(session_id: str):
            if session_id not in self.sessions:
                return JSONResponse(status_code=404, content={"error": "الجلسة غير موجودة."})

            session = self.sessions[session_id]
            ar_text = session.get_full_arabic_conversation()

            try:
                message = TranslationService.create_translate_template(ar_text)
                translated_json = TranslationService.generate_translation(
                    message, self.tokenizer, self.model, self.device)
            except Exception as e:
                translated_json = {"error": f"فشل في الترجمة: {str(e)}"}

            return {
                "session_id": session_id,
                "finished": str(session.finished),
                "full_conversation": session.messages,
                "translated_conversation": translated_json
            }

        @self.app.get("/translate/{session_id}")
        def translate_conversation(session_id: str):
            if session_id not in self.sessions:
                return JSONResponse(status_code=404, content={"error": "الجلسة غير موجودة."})

            session = self.sessions[session_id]
            ar_text = session.get_full_arabic_conversation()

            try:
                message = TranslationService.create_translate_template(ar_text)
                translated_json = TranslationService.generate_translation(
                    message, self.tokenizer, self.model, self.device)
                return translated_json
            except Exception as e:
                return JSONResponse(status_code=500, content={"error": f"فشل في الترجمة: {str(e)}"})

    def run(self, port: int = 8000):
        ngrok.set_auth_token(NGROK_AUTH_TOKEN)
        public_url = ngrok.connect(port)
        print(f"🔗 API متاحة على: {public_url}")

        nest_asyncio.apply()
        uvicorn.run(self.app, port=port)
