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
                    "ماتبداش بالاساله غير لما المريض يحكي مشكلته :ازيك عامل ايه او ايه جمله ترحيبيه ,انت المفروض ترد تقوله تمام الحمد لله تقدر تقولي مشكلتك",
                    "بعد كده، اسأله عن بداية ظهور المشكلة: من إمتى ظهرت؟",
                    "استفسر عن التغيرات اللي حصلت للمكان ده: اللون، الحجم، الملمس، القشور، الشكل.",
                    "اسأله لو في أعراض مصاحبة: حكة؟ وجع؟ نزيف؟ أو أي إحساس تاني.",
                    "اسأله لو استخدم أي حاجة على المكان زي مرهم، كريم، أو وصفة بيتية، وهل حصل تحسن أو ساءت الحالة.",
                    "بعد كده اسأله عن العوامل اللي ممكن تكون بتزود المشكلة زي: لبس ضيق، أو الاحتكاك.",
                    "استفسر عن تاريخ التعرض للشمس: شغله كان فيه شمس؟ اتحرق قبل كده؟ بيستخدم واقي شمس؟",
                    "اسأله لو في تاريخ عائلي لحالات شبه دي، زي سرطان الجلد أو شامات غريبة.",
                    "استفسر عن وصف شكل الحاله الي عنده و لو عنده علامات شبه تانيه",
                    "يبقي اساله سوال اخير  : في حاجه تانيه عايز تضيفها ",
                    "استخدم لغة عامية مصرية بسيطة وواضحة، وخليك دايمًا مهتم وبتتكلم بود.",
                    "اسأل سؤال واحد بس في كل مرة، وكمّل على حسب رد المريض.",
                    "ما تقدمش أي تشخيص، شغلتك تجمع المعلومات اللي الدكتور هيحتاجها بعد كده.",
                    "ما تبدأش بمقدمة وما تختمش، بس كمل المحادثة على حسب كل إجابة.",
                    "رد بالسؤال بس"
                ])
            }
        ]

    def process_input(self, user_input: str, tokenizer, model, device: str) -> str:
        user_input_cleaned = user_input.strip().lower()

        if self.finished or re.match(r"^\s*تمام\b", user_input_cleaned, re.IGNORECASE) or user_input_cleaned in ["لا شكرا", "خروج", "انتهاء", "exit", "quit"]:
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
