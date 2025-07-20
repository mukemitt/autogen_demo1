import openai

client = openai.OpenAI(
    api_key="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",  # Replace with your OpenRouter API Key
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="moonshotai/kimi-k2:free",  # Specify the free Kimi K2 model
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain the concept of quantum entanglement in simple terms."}
    ]
)

print(response.choices[0].message.content)