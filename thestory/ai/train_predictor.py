import os
import torch
import torch_directml
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, modeling_utils
from datasets import load_dataset

if not hasattr(modeling_utils, "ALL_PARALLEL_STYLES") or modeling_utils.ALL_PARALLEL_STYLES is None:
    modeling_utils.ALL_PARALLEL_STYLES = ["tp", "none", "colwise", "rowwise"]

device = torch_directml.device()

BASE_MODEL = "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T"
OUTPUT_DIR = "model/future"

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(BASE_MODEL)
model.to(device) 

dataset = load_dataset("json", data_files="casual.jsonl")

def format_example(ex):
    text = f"Predict the likely outcome.\nSituation: {ex['prompt']}\nOutcome: {ex['response']}"
    tokens = tokenizer(text, truncation=True, padding="max_length", max_length=512)
    tokens["labels"] = tokens["input_ids"].copy()
    return tokens

dataset = dataset.map(format_example, remove_columns=["prompt", "response"])

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    num_train_epochs=6,
    learning_rate=2e-5,
    save_strategy="epoch",
    logging_steps=5,
    fp16=False,
    bf16=False,
    report_to="none",
    no_cuda=True,     
    use_cpu=False,    
    remove_unused_columns=False
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"]
)

print(f"Training on: {device}")
trainer.train()

trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
