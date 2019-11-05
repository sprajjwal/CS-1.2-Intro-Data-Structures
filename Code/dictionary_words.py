from sys import argv
import random

def dictionary_word(num_needed):
    """returns n random words from word list"""
    huge_list = []
    with open("/usr/share/dict/words", "r") as f:
        for line in f:
            huge_list.extend(line.split())
    str_output = ""
    for t in range(num_needed):
        str_output += huge_list[random.randrange(len(huge_list))]
        if t < num_needed - 1:
            str_output += " "
    str_output += "."
    return str_output

if __name__ == "__main__":
    assert len(argv) == 2, "Incorrect number of arguments"
    num_needed = int(argv[1])
    print(dictionary_word(num_needed))
    