import requests
import time

ollama_url = "http://127.0.0.1:11434"
langfuse_url = "https://api.langfuse.com/log"  # Replace with actual Langfuse URL if different
langfuse_api_key = "your_langfuse_api_key"  # Replace with your actual API key

def query_ollama(prompt, model="llama3.1"):
    data = {
        "prompt": prompt,
        "model": model,
        "stream": False
    }

    response = requests.post(f"{ollama_url}/api/generate", json=data)

    if response.status_code == 200:
        response_text = response.json().get("response", "No response Found")
        log_to_langfuse(prompt, response_text)
        return response_text
    else:
        error_message = f"Error: {response.status_code}, {response.text}"
        log_to_langfuse(prompt, error_message, status="error")
        return error_message

def log_to_langfuse(prompt, response, status="success"):
    log_data = {
        "timestamp": time.time(),
        "event": "ollama_query",
        "status": status,
        "prompt": prompt,
        "response": response,
        # You can include additional metadata if needed, like model, user id, etc.
    }

    headers = {
        "Authorization": f"Bearer {langfuse_api_key}",
        "Content-Type": "application/json"
    }

    try:
        langfuse_response = requests.post(langfuse_url, json=log_data, headers=headers)
        if langfuse_response.status_code != 200:
            print(f"Langfuse logging failed: {langfuse_response.status_code} - {langfuse_response.text}")
    except Exception as e:
        print(f"Error logging to Langfuse: {e}")

# Call the function
response = query_ollama("Greet me in 3 words!")
print(response)
