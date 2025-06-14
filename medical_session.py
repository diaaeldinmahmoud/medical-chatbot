import re
from typing import List, Dict

class MedicalSession:
    def __init__(self):
        self.questions_asked = 0
        self.finished = False
        self.last_bot_message = "تمام الحمد لله، تقدر تقولي إيه المشكلة؟"
        self.useless_responses = {
            "مرحبا", "اهلا", "السلام عليكم", "هاي", "إزيك", 
            "صباح الخير", "مساء الخير", "هلا", "هاي", "كيفك"
        }
        self.messages = [
            {
                "role": "system",
                "content": "\n".join([
                    "أنت مساعد طبي افتراضي متخصص في جمع المعلومات من المرضى لمساعدة الأطباء في التشخيص.",
                    "سيتم تزويدك بمعلومات أولية عن حالة المريض.",
                    "مهمتك إنك تسأل المريض بطريقة ودودة وطبيعية زي دكتور جلدية بيسأل مريضه.",
                    # ... [rest of the system prompt from notebook]
                    "رد بالسؤال بس"
                ])
            }
        ]

    def process_input(self, user_input: str, tokenizer, model, device: str) -> str:
        user_input_cleaned = user_input.strip().lower()

        if self.finished or re.match(r"^\\s*تمام\\b", user_input_cleaned, re.IGNORECASE) or \
           user_input_cleaned in ["لا شكرا", "خروج", "انتهاء", "exit", "quit"]:
            self.finished = True
            return "شكرًا لك! أتمنى لك الصحة والعافية. 😊"

        self.messages.append({"role": "user", "content": user_input})

        if user_input_cleaned in self.useless_responses:
            response = self.last_bot_message
            self.messages.append({"role": "assistant", "content": response})
            return response

        text = tokenizer.apply_chat_template(self.messages, tokenize=False, add_generation_prompt=True)
        model_inputs = tokenizer([text], return_tensors="pt").to(device)
        generated_ids = model.generate(model_inputs.input_ids, max_new_tokens=100, do_sample=False)

        generated_ids = [
            output_ids[len(input_ids):]
            for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

        self.last_bot_message = response
        self.messages.append({"role": "assistant", "content": response})
        self.questions_asked += 1

        return response

    def get_full_arabic_conversation(self) -> str:
        return "\n".join([
            f"{'المساعد' if msg['role'] == 'assistant' else 'المريض'}: {msg['content']}"
            for msg in self.messages if msg["role"] in {"user", "assistant"}
        ])