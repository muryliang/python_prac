from stack import Stack

def in2post(string):
    """turn 1 + 2 * 3 into 1 2 3 * +

    should make an array to store every operator's 
    priviledge"""
    s = Stack()
    res = list()
    calculator = "+-*/%()"

    for item in string.split(" "):
        if item not in calculator: # just add to list 
            res.append(item)
        elif item == "(": # just push in
            s.push(item)
        elif item == ")": # pop until encounter "("
            tmp = s.pop()
            while tmp != "(":
                res.append(tmp)
                tmp = s.pop()
        elif item in "*%/":
            while not s.isEmpty() and s.peek() in "*%/":
                res.append(s.pop())
            s.push(item)
        else: #"+-"
            while not s.isEmpty() and s.peek() in "*%/+-":
                res.append(s.pop())
            s.push(item)

    while not s.isEmpty():
        res.append(s.pop())
    return res

string = input("input your calculation: ")
print ("result is: ",in2post(string))
