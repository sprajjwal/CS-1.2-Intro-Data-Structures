from sys import argv

def reverse_list(input_list):
    output_list = []
    for item in reversed(input_list):
        if len(item) > 1:
            listed_item = list(item)
            output_list += reverse_list(listed_item)
            output_list += " "
        else:
            output_list += item
    output_str =  ('').join(output_list)
    return output_str

if __name__ == "__main__":
    del argv[0] # deleting file name
    assert len(argv) != 0, "No arguments were given" # no arguments given
    
    output_str = reverse_list(argv)

    print(output_str)