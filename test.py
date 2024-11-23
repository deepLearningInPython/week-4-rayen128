import numpy as np


text = "The quick brown fox jumps over the lazy dog!"


def tokenize(string: str) -> list:
    # Remove punctuation manually
    punctuation = "!?@#$%^&*(),."

    cleaned_string = ''.join(
        char if char not in punctuation else '' for char in string)

    # Split into words, convert to lowercase, and remove duplicates
    tokens = [word.lower() for word in cleaned_string.split()]

    return sorted(set(tokens))


def token_to_id(text):
    token_to_id = {word.lower(): i for i,
                   word in enumerate(set(tokenize(text)))}

    return token_to_id


documents = ["hallo, ik ben Rayen", "Goedemorgen rayen, hoe gaat het?"]

tokens = set()

for text in documents:
    for word in tokenize(text):
        tokens = tokens.union(tokenize(text))

token_to_id = {}
id_to_token = {}

for i, word in enumerate(tokens):
    token_to_id[i] = word
    id_to_token[word] = i

print(token_to_id)
print(id_to_token)
