from groq_client import get_groq_client

client = get_groq_client()

class PersonalAssistant:
    def __init__(self):
        print("Hi, I am your AI assistant ... How can i help you?")

    def ans_query(self):

        question = input("Ask me anything:")
        chat_completion = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
                {
                    "role":"system",
                    "content": "Act as a helpful assistant"
                },
                {
                    "role":"user",
                    "content":question
                }
            ],
            temperature = 0.7,
            max_tokens = 1024
        )
        print(chat_completion.choices[0].message.content.strip())