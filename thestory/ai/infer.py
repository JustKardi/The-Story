from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="model/story-ai",
    tokenizer="model/story-ai",
    max_new_tokens=150
)

print(pipe("User: I feel lost.\nNarrator:")[0]["generated_text"])
