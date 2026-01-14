prompt = """You analyze situations and predict realistic consequences.

Conditions:
A city blocks trade routes during a drought.

Outcome:
"""

inputs = tokenizer(prompt, return_tensors="pt")
out = model.generate(
    **inputs,
    max_new_tokens=80,
    temperature=0.3,
    do_sample=True
)

print(tokenizer.decode(out[0], skip_special_tokens=True))
