from random import choice
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    del argv[0] # deleting the file name
    rearr_str = ""
    while len(argv) > 0:
        rearr_str += argv.pop(argv.index(choice(argv)))
        rearr_str += " "
    print(rearr_str)