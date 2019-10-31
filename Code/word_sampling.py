import random
import sys
from histogram import histogram

def word_sampler(hist):
    """Takes a histogram and returns a word based of its frequency"""
    total = 0
    total += sum(hist.values())
    sum_prob = 0
    predict = random.random()
    for key in hist.keys():
        prob = hist[key]/total
        if predict > sum_prob and predict <= sum_prob + prob:
            return key
        sum_prob += prob

def test_sampler(hist):
    """ tests sampler by running it 10000 times, uncomment line 32 for this"""
    test_words = []
    for _ in range(10000):
        test_words.append(word_sampler(hist))
    test_hist = histogram(test_words)
    for item in test_hist.keys():
        print(f"{item}: {test_hist[item]}")

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file, 'r') as f:
        words = f.read().split()
        hist = histogram(words)
    test_sampler(hist)
    #print(word_sampler(hist))