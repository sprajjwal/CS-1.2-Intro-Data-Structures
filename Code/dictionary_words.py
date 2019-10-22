from sys import argv
import random

if __name__ == "__main__":
    assert len(argv) == 2, "Incorrect number of arguments"
    num_needed = int(argv[1])
    huge_list = []
    with open("/usr/share/dict/words", "r") as f:
        for line in f:
            huge_list.extend(line.split())
    str_output = ""
    for _ in range(num_needed):
        str_output += huge_list.pop(random.randint(0, len(huge_list)-1))
        str_output += " "
    str_output += "."
    print(str_output)