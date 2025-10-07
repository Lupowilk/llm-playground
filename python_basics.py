import random

name = "LLM Playground"
max_tokens = 100
temperature = 0.7

print(f"Project: {name}")
print(f"Max tokens:{max_tokens}")
print(f"temperature:{temperature}")


# Lists
models = ["gpt2", "gpt2-medium", "distilgpt2"]

#Dictionaires
config = {
    "temperature": 0.7,
    "max_lenght": 50,
    "top_k": 50
}

print(f"\nAvailable models: {models}")
print(f"Config: {config}")

#Functions
def greet(name):
    return f"Hello, {name}!"

# call the funciion
message = greet("AI engineer")
print(f"\n{message}")

random_temp = random.uniform(0.5, 1.5)
print(f"\nRandom temperature: {random_temp:.2f}")
