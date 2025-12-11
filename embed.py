import ollama

def ask_model(prompt):
    stream = ollama.chat(
        model="llama3.1",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    for chunk in stream:
        if "message" in chunk:
            yield chunk["message"]["content"]
