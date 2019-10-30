import requests
from sys import argv

if __name__ == "__main__":
    del argv[0] # deleting file name
    assert len(argv) != 0, "No arguments were given" # no arguments give
    query = argv[0]
    anagrams = requests.get("http://www.anagramica.com/all/:" + query).json()
    print([stuff for stuff in anagrams["all"] if len(stuff) == len(query) and stuff != query]) # list of ana
