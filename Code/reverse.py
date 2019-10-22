from sys import argv

def reverse_word(word):
    output_str = ""
    for num in range(len(word)-1,-1, -1):
        output_str += word[num]
    return output_str

def reverse_list(list):
    output_str = ""
    for item in reversed(list):
        output_str += reverse_word(item)
        output_str += " "
    return output_str

if __name__ == "__main__":
    del argv[0] # deleting file name
    assert len(argv) != 0, "No arguments were given" # no arguments given
    
    if len(argv) == 1: #single word
        output_str = reverse_word(argv[0])
    else: # string
        output_str = reverse_list(argv)

    print(output_str)