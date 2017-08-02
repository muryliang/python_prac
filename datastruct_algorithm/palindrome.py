import deque
import signal
import sys

def handle(signum, frame):
    print ("\njust exit", signum)
    sys.exit()

def isPalindrome(string):
    """check if the given string is a palindrome
        return: boolean
    """

    d = deque.Deque()
    for char in string:
        d.addFront(char)

    times = d.size() // 2
    for _ in range(times):
        if not d.removeFront() == d.removeRear():
            return False
    return True

if __name__ == "__main__":
    """my doc"""
    signal.signal(signal.SIGQUIT, handle)
    signal.signal(signal.SIGINT, handle)
    while True:
        string = input("input string: ")
        print (isPalindrome(string))



