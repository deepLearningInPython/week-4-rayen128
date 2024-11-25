import numpy as np
from tasks import tokenize, token_counts, make_vocabulary_map, tokenize_and_encode

# text = "The quick brown fox jumps over the lazy dog!"

# text = """The quick brown fox jumps over the lazy dog. The fox and the dog play together.
#             The fox chases the dog, but the dog runs quickly. The fox is fast, and the dog escapes."""

docs = [
    "The cat sat on the mat.",
    "The cat and the cat.",
    "The Quick Brown Fox jumps Over the lazy Dog.",
    "The cat has 2 paws and 4 legs.",
    "Hello, world! How are you?",
    "hello",
    "This is a test of the tokenizer.",
    "This is a long document that contains many words, phrases, and repeated occurrences. Words, phrases, and sentences repeat to test scalability."
]

enc = list()

i2t, t2i = make_vocabulary_map(docs)


for idtext, text in enumerate(docs):
    enc.append(list())
    for idword, word in enumerate(tokenize(text)):
        enc[idtext].append(t2i[word])


enc_comprehension = [[t2i[word] for word in tokenize(text)] for text in docs]

assert enc == enc_comprehension
