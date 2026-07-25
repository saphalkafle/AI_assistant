from groq_client import get_groq_client
client = get_groq_client()

class PersonalAssistant:
    def __init__(self):
        print("Hi, I am your AI assistant ... How can i help you?")

    def ans_query(questions):
        chat_completion = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
                {
                    "role":"system",
                    "content": "Act as a helpful assistant"
                },
                {
                    "role":"user",
                    "content":questions
                }
            ],
            temperature = 0.7,
            max_output_tokens = 1024
        )
        return chat_completion.choices[0].content.strip()