# -*- coding: utf-8 -*-

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A pullze for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(multiply(height, 1), multiply(divide(weight,1 ), divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

div_res = divide(iq, 2)
mul_res = multiply(weight, div_res)
sub_res = subtract(height , mul_res)
add_res = add(age, sub_res)

print "result is ", subtract(add(24,divide(34, 100)), 1023)
