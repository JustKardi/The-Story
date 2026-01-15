import os
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "future") 
BASE_MODEL = "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T" 

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
tokenizer.pad_token = tokenizer.eos_token  

model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float32)
model.eval()

if len(sys.argv) < 2:
    print("Usage: python infer.py 'Your prompt here'")
    sys.exit(1)

prompt = sys.argv[1]

inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

with torch.no_grad():
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"], 
        max_new_tokens=120,
        do_sample=True,
        temperature=0.8,
        pad_token_id=tokenizer.eos_token_id 
    )


text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(text)
