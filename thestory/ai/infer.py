from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Load your trained model
model_path = "model/storyai"  # or wherever your model was saved

tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T")
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_path)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200
)

# Test it
test_input = "User: I won my first competition.\nNarrator:"
output = pipe(test_input)[0]["generated_text"]
print(output)
