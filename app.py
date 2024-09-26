import os

os.environ["OPENAI_API_KEY"] = "Your open API key goes here."
os.environ["GROQ_API_KEY"] = "Your groq API key goes here."

from routellm.controller import Controller

client = Controller(
  routers=["mf"],
  strong_model="chatgpt-4o-latest",
  weak_model="groq/llama3-8b-8192"
)

response = client.chat.completions.create(
  # This tells RouteLLM to use the MF router with a cost threshold of 0.11593
  model="router-mf-0.11593",
  messages=[
    # {"role": "user", "content": "What is AI-driven automation?"}
    {"role": "user", "content": "Analyze the potential economic impacts of AI-driven automation across various industries over the next decade."}
  ]
)

message_content = response['choices'][0]['message']['content']
model_name = response['model']

print(f"Message content: {message_content}")
print(f"Model name: {model_name}")