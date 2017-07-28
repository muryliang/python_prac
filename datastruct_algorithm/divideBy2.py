from stack import Stack

def divideBy2():
    s = Stack()

    num = int(input("input your number: "))

    while True:
        s.push(num % 2)
        num = num // 2
        if num == 0:
            break

    value = ""
    while not s.isEmpty():
        value = value + str(s.pop())

    print ("the value is %s"%(value))

divideBy2()

