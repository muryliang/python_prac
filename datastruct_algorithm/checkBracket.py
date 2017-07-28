import sys

import stack

def match(item, sym):
    opens = "{[("
    closes = "}])"
    return opens.index(item) == closes.index(sym)

chklist = input("input string: ")
s = stack.Stack()
for char in chklist:
    if char in "([{":
        s.push(char)
    elif char in ")]}":
        if  s.isEmpty():
            print ("False")
            sys.exit()
            print ("False")
        item = s.pop()
        if not match(item, char):
            print ("False")
            sys.exit()
if not s.isEmpty():
    print ("False")
    sys.exit()
else:
    print ("True")

