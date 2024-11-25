from tasks import *


def test_encode_sentences():
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
    enc, t2i, i2t = tokenize_and_encode(docs)
    assert " | ".join([" ".join(i2t[i] for i in e) for e in enc]) == " | ".join(
        " ".join(tokenize(d)) for d in docs)
