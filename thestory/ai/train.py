from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset

MODEL_ID = "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(MODEL_ID)

dataset = load_dataset("json", data_files="stories.jsonl")

def format(ex):
    text = f"You are a reflective narrator.\nUser: {ex['prompt']}\nNarrator: {ex['response']}"
    tokenized = tokenizer(text, truncation=True, padding="max_length", max_length=2048)
    tokenized['labels'] = tokenized['input_ids'].copy()
    return tokenized

dataset = dataset.map(format, remove_columns=["prompt", "response"])

training_args = TrainingArguments(
    output_dir="model/storyai",
    per_device_train_batch_size=1,
    num_train_epochs=3,
    logging_steps=1,
    save_strategy="epoch",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
)

print("Starting training...")
trainer.train()
print("Training completed!")
trainer.save_model("model/storyai")
tokenizer.save_pretrained("model/storyai")
