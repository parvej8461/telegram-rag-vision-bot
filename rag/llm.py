import requests
import os

def ask_llm(prompt):
    try:
        url = f"{os.getenv('OLLAMA_URL')}/api/generate"

        response = requests.post(url, json={
            "model": os.getenv("OLLAMA_MODEL"),
            "prompt": prompt,
            "stream": False
        })

        data = response.json()

        #  Debug print (optional but useful)
        print("LLM RAW RESPONSE:", data)

        if "response" in data:
            return data["response"]
        elif "error" in data:
            return f" LLM Error: {data['error']}"
        else:
            return " Unexpected response from LLM."

    except Exception as e:
        return f" Exception: {str(e)}"