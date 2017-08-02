def int2base2(num, base):
    assert base >= 2 and base <= 16
    """ return: s  string"""
    if num == 0:
        return ""
    return int2base2(num // base, base) + str("0123456789abcdef"[num % base])

num = int(input("input your number: "))
base = int(input("input your base: "))
print (int2base2(num, base))
