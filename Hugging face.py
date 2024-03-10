import torch
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "aiwannafly/semantics-analysis-term-classifier"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
pipe = pipeline("text-classification", model=model_name, tokenizer=tokenizer)
res = pipe("output_final.json")
print(res)
