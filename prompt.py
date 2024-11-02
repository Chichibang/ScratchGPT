from huggingface_hub import InferenceClient

client = InferenceClient(api_key="hf_xxxxxxxx")
def send(message):
    messages = [
        { "role": "user", "content": message }
    ]

    stream = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct", 
        messages=messages, 
        max_tokens=500,
        stream=True
    )
    # Collect all parts into a single string
    output = ""
    for chunk in stream:
        output += chunk.choices[0].delta.content
    return output
