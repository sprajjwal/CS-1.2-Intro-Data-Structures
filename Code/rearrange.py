from random import choice
from sys import argv
import time_benchmark as T

if __name__ == "__main__":
    timer = T.Timer("rearrange")
    timer.start_timer()
    argc = len(argv)
    del argv[0] # deleting the file name
    assert len(argv) != 0, "No arguments were given" # no arguments given
    rearr_str = ""
    while len(argv) > 0:
        rearr_str += argv.pop(argv.index(choice(argv)))
        if len(argv) != 0:
            rearr_str += " "
    print(rearr_str)
    timer.stop_timer()
    print(f"Time taken: {timer.show_benchmark()}")
    timer.show_all_benchmarks()