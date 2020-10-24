import string
import numpy as np


WORDS = [
    "yeah",
    "yes",
    "yup",
    "yeah",
    "yea",
    "ye",
    "ya",
    "yes",
    "yas",
    "yess",
    "yee",
    "yeet",
    "no",
    "nope",
    "naw",
    "nae",
    "noo",
    "na"
]

ISYES = np.array([
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
 ])


def make_data(word: str) -> list:
    return np.array([1 if char in word else 0 for char in string.ascii_lowercase])

class InputData:
    def __init__(self):
        self.words = WORDS
        self.Y = ISYES
        self.X = self.setup_data()

    def setup_data(self):
        return np.array([make_data(word) for word in self.words])
