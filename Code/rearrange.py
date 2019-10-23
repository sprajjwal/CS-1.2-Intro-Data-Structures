from random import choice
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    del argv[0] # deleting the file name
    assert len(argv) != 0, "No arguments were given" # no arguments given
    rearr_str = ""
    while len(argv) > 0:
        rearr_str += argv.pop(argv.index(choice(argv)))
        if len(argv) != 1:
            rearr_str += " "
    print(rearr_str)