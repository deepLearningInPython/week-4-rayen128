import numpy as np
from tasks import tokenize, token_counts, make_vocabulary_map

# text = "The quick brown fox jumps over the lazy dog!"

text = """The quick brown fox jumps over the lazy dog. The fox and the dog play together.
              The fox chases the dog, but the dog runs quickly. The fox is fast, and the dog escapes."""


t2i, i2t = make_vocabulary_map([text])

print(i2t)
