from dictogram import *
import random
import sys

class Markogram(dict):
    def __init__(self, words=None, order=1):
        """Initialize this histogram as a new dict and count given words."""
        super(Markogram, self).__init__()
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 1  # Total count of all word tokens in this histogram
        self.order = order 
        # Count words in given list, if any

        if words is not None:
            prev = tuple(words[0:order])
            for index in range(1, len(words) - order+1):
                self.add_count(prev, tuple(words[index:index+order]))
                prev = tuple(words[index:index+order])
            for key in self.keys():
                self[key] = Dictogram(self[key])

    def add_count(self, prev, word):
        """adds word to markogram"""
        if not prev in self.keys():
            self[prev] = []
            self.types += 1
        self[prev].append(word)
        self.tokens += 1

    def sample(self, key):
        """gets a random word  that appears after key"""
        return self[key].sample()

    def get_string(self, len=1):
        """returns a string of len based on markov's chain"""
        start = random.choice(list(self.keys()))
        print(start)
        strin = start[0]
        prev = start
        for _ in range(len-1):
            prev = self.sample(prev)
            strin += f" {prev[0]}"
        strin += "."
        return strin.capitalize()


if __name__ == "__main__":
    # with open("bro_code.txt", 'r') as f:
    #     words = f.read()
    words = "I went left, you went right, I went left, I went right,"
    dic = Markogram(words.split(), order=3)
    # for key in dic.keys():
    #     print(f"{key}: {dic[key]}")
    # print(dic.sample('a'))
    # print(f"tokens: {dic.tokens}")
    # print(f"types: {dic.types}")
    # print(dic.get_string(20))
    for key in dic.keys():
        print(f"{key}:  {dic[key]}")
       
