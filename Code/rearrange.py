from random import choice
from sys import argv
import time_benchmark as T

def rearrange(words):
    """rearrange the words"""
    rearr_str = ""
    while len(argv) > 0:
        rearr_str += words.pop(words.index(choice(argv)))
        if len(words) != 0:
            rearr_str += " "
    return rearr_str


if __name__ == "__main__":
    # timer = T.Timer("rearrange")
    # timer.start_timer()
    argc = len(argv)
    del argv[0] # deleting the file name
    assert len(argv) != 0, "No arguments were given" # no arguments given
    print(rearrange(argv))
    # timer.stop_timer()
    # print(f"Time taken: {timer.show_benchmark()}")
    # timer.show_all_benchmarks()