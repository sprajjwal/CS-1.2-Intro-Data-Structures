def histogram(words):
    """ Makes a histogram from a list of words"""
    hist = {}
    for word in words:
        word = word.lower()
        if word in hist.keys():
            hist[word] += 1
        else:
            hist[word] = 1
    return hist

# def lis(word_dict):
#     """ creates lists of lists with indices holding frequency"""
#     lis = []
#     for word in word_dict.keys():
#         if len(lis) <= word_dict[word]:
#             print(word_dict[word])
#             lis.extend(word_dict[word] - len(lis) + 1)
#         lis[word_dict[word]].append(word)
#     return lis

def unique_word(hist):
    """ counts number of unique words in a histogram"""
    return len(hist.keys())

def frequency(word, hist):
    """ gives the frequency of word in the histogram"""
    if word.lower() in hist.keys():
        return hist[word.lower()]
    else:
        return 0

def read_hist(f):
    """Reads a histogram type file into a dictionary """
    lines = f.readlines()
    hist = {}
    for line in lines:
        line = line.split()
        hist[line[0]] = line[1]
    return hist

def write_hist(file_name, hist):
    """ writes a histogram to a file"""
    with open(file_name, "w+") as f:
        for key in hist.keys():
            f.write(f"{key} {hist[key]}\n")

if __name__ == "__main__":
    with open("bro_code.txt", 'r') as f:
        words = f.read().split()
        hist = histogram(words)
        freq = lis(hist)
    print(hist["a"])
    print(unique_word(hist))
    print(frequency('a', hist))
    write_hist("bro_hist.txt", hist)
    print([items for items in freq if len(items) > 0])