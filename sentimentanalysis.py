# extra sentiment analysis
from transformers import pipeline

# Load the classification pipeline with the specified model
pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

# Classify a new sentence
sentence = "I hate how good this product is"
result = pipe(sentence)

# Print the result
print(result)
