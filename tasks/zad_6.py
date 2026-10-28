import re


def word_frequencies(text: str) -> dict:
    frequency = {}

    text = text.lower()

    for word in re.split(r"[^a-z0-9]+", text):
        if len(word) == 0:
            continue

        frequency[word] = frequency.get(word, 0) + 1

    return frequency
