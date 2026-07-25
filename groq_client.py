import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_groq_client():

    #get client from api
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("Groq_api_Key is not set")
    
    return Groq(api_key=api_key)
