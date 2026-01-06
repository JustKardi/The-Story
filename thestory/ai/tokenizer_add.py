from transformers import AutoTokenizer

ORIGINAL_MODEL_ID = "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T"
tokenizer = AutoTokenizer.from_pretrained(ORIGINAL_MODEL_ID)
tokenizer.pad_token = tokenizer.eos_token

tokenizer.save_pretrained("model/storyai")
