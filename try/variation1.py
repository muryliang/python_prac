import pprint

"""calculate the input files every character(ingore case) apprearance frequency"""
# in python3 raw_input is just input, so use input
inputFile = raw_input("File Name : ")
count = {}

with open(inputFile, 'r') as info:
    readFile = info.read()
    for character in readFile.upper():
        count.setdefault(character, 0)
        count[character] = count[character] + 1

value = pprint.pformat(count)
print(value)
