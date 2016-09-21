#!/usr/bin/python2
#single line comments start with a bash
"""Multiline strings can be written 
    using three "'s, and are often used
    as comments
"""

####################################################
### 1, Primitive data types and operators
####################################################

#you have numbers
3 #=>3

#Math is what you would expect
1 + 1
8 - 1
10 * 2
35 / 5

#Division is a bit tricky . It is integer division and floors and results
#automatically
5 / 2 #=>2

#to fix division we need to learn about float
2.0
11.0 / 4.0

#enforce precedence with  parenthese
(1 + 3) * 2 #=>8

#boolen values are primitives
True
False

#negate with not
not True
not False

#Equality is ==
1 == 1
2 == 1

#Inequality is !=
1 != 1
2 != 1

#more comparison
1 < 10
2 > 10
2 <= 10
2 >= 10

#comparison can be chained!
1 < 2 < 3
2 < 3 < 4

#strings are created with " or '
"this is a string"
'this is also a string'

#strings can be added too
"hello" + "world!" #=>"hello world!"

#a string can be treated like a list of characters
"this is a string"[0] #=>'t'

# % can be used to format strings , like this
"%s can be %s"%("strings", "interpolated")

#a newer way to format strings is the format method
#this method is the preferred way
"{0} can be {1}".format("strings" , "formatted")

#you can use keywords if you don't want to count
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

#None is an object
None #=>None

#don't use the equality '==' to compare objects with None
#use 'is' instead
"etc" is None
None is None

#the is operator tests for object identity. This isn't
#very useful when dealing with primitive values,
#but is very useful when dealing with objects

#None, 0, emtpy strings and lists all evaluate to False
#all other values are true

0 == False
"" == False

#######################################################
##variables and collections
#######################################################

#printing is pretty easy
print "I'm Python, nice to meet you!"


#no need to declare variables before using them
some_var = 5
some_var #=>5

#accessing a previously unassigned variable is an exception
#see control flow to learn more about exception handling
#some_other_var #raise an exception

#if can be used as an expression

print "yahoo!" if 3 > 2 else 2 #=>"yahoo!"

#lists store a sequence
li = []

other_li = [4,5,6]

#add stuff to the end of list with append
li.append(1)
li.append(2)
li.append(4)
li.append(3)

#remove from the end with pop
li.pop()

#let's put it back
li.append(3)

#access a list like you would any array
li[0] #=>1
#look at the last element
li[-1] #=>3

#looking out of bounds is an IndexError
#li[4] #Raise an IndexError


#you can look at ranges with slice syntax
li[1:3] #=>[2,4]
#omitting begins
li[2:] #=>[4,3]
#omitting the end
li[:3] #=>[1,2,4]

#remove arbitrary elements from a list with del
del li[2] #li  is now [1,2,3]

#you can add lists
li + other_li #=> [1,2,3,4,5,6]

#contatenate lists with extend
li.extend(other_li) #now li is [1,2,3,4,5,6]

#check for existence in a list with in
1 in li #=>True

#examine length  with len
len(li) #=>6

#tuples are like lists but immutable
tup = (1,2,3)
tup[0] #=>1
#tup[0] = 3 #Raise a TypeError

#you can do all those list things on tuple too
len(tup) #=>3
tup + (4,5,6) #=>(1,2,3,4,5,6)
tup[:2] #=>(1,2)
2 in tup

#you can unpack lists or tuples into variables
a,b,c = (1,2,3)

#tuples are created by default if you leave out parenthese
d,e,f = 4, 5, 6

#now look how easy it is to swap two values
e,d = d,e

#dictionaries store mapping
emtpy_dict = {}
#here is a prefilled dictionary
filled_dict = {"one":1, "two":2, "three":3}

filled_dict["one"] #=> 1
filled_dict.keys() #=>["three","two","one"]
#Note: dictionary key ordering is not guaranteed

filled_dict.values() #=>[3,2,1]

#checking for existence of keys in a dictionary with in
"one" in filled_dict #=>True
1 in filled_dict #=>False

#looking up a non-existence key is a KeyError
#filled_dict["four"] #KeyError

#use get method to avoid the key error
filled_dict.get("one") #=>1
filled_dict.get("four") #=>None

#the get method supports a default argument when the value is missing
filled_dict.get("one",4) #=>1
filled_dict.get("four",4) #=>4

#set default method is a safe way to add key-value pairs
filled_dict.setdefault("five",5) #filled_dict["five"] is set to 5
filled_dict.setdefault("five",6) #filled_dict["five"] is still  set to 5



#sets store.. well sets
empty_set = set()
some_set = set([1,2,3,4]) #some_set is now set([1,2,3,4)]
print some_set

#since python 2. 7, {} can be used to declare a set
filled_set = {1,2,2,3,4} #=> {1,2,3,4}  #{} is a dict ,not an emtpy set, use set() insted

#add more items to a set
filled_set.add(5) #filled_set is now {1,2,3,4,5}

#do set intersection with &
other_set = {3,4,5,6}
filled_set & other_set #=>{3,4,5}

#do set union with |
filled_set | other_set #=>{1,2,3,4,5,6}

#do set difference with -
{1,2,3,4} - {2,3,5} #=>{1}

#check for existence in a set with in
2 in filled_set #=>True
10 in filled_set #=>False


#######################
##control flow
#######################
some_var = 5

#here is an if statement. Indentitation is significant in python!
#prints some var is small than 10

if some_var >= 10:
    print "some_var is totally bigger than 10"
elif some_var < 10:
    print "some_var is smaller than 10."
else:
    print "some_var is indeed 10"


"""
for loops iterate over lists
for xxx:
prints:
    xxx
    xxx
    xxx
"""
for animal in ["dog","cat","mouse"]:
    #you can use % to interpolate string
    print "%s is a mammal"%animal

"""
`range(number)` returns a list of numbers
from zero to given number
"""

for i in range(4):
    print i
#from 0 to 3

"""while loop go until
    a condition is nolonger met
"""

x = 0
while x < 4:
    print x
    x += 1

#handle exception with a try/exception block
#works for python 2.6 and up
try:
    raise IndexError("this is an index error")
except IndexError as e:
    pass #pass is just a non op ,usually you would do recovery here

##############################
##4, functions
##############################

#use def to create new function
def add(x,y):
    print "s is %s and y is %s"%(x,y)
    return x+y

add(5,6)
add(y=6,x=5)

#you can define a funciton that take variable number of args
def varargs(*args):
    return args

varargs(1,2,3) #=>(1,2,3)

#you can define funcs take variable number of keyword arguments
def keyword_args(**args):
    return args

keyword_args(big="foot",loch="ness") #=>{"big":"foot","loch":"ness"}

#you can do both at once,if you like
def all_the_args(*args, **kargs):
    print args
    print kargs
"""
all_the_args(1,2,a=3,b=4) prints:
    (1,2)
    {"a":3,"b":4}

"""

#when calling funcs , you can do the opposite of vaargs!
args = (1,2,3,4)
kargs = {"a":3,"b":4}
all_the_args(*args)
all_the_args(**kargs)
all_the_args(*args, **kargs)

#python has first class functions
def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_10 = create_adder(10)
add_10(3) #=> 13

#there are also anonymous funcs
(lambda x: x > 2)(3) #=>True

#there are built in high order funcs
map(add_10, [1,2,3]) #=>[11,12,13]
filter(lambda x: x > 5,[3,4,5,6,7]) #=>[6,7]

#we can use list comprehensions for nice maps and filters
[add_10(i) for i in [1,2,3]] #=>[10,11,12]
[x for x in [3,4,5,6,7] if x > 5] #=>[6,7]

######################
#5 class
######################

#we subclass from object to get a class
class Human(object):
    #a class attribute , it is shared by all instances of this class
    species = "H. sapies"
    #Basic initialization
    def __init__(self,name):
        self.name = name
    #an instance method; all methods take self as first arg
    def say(self,msg):
        return "%s: %s" %(self.name,msg)

    #a class method is shared by all instances
    #they are called with the calling  class as the first member
    @classmethod
    def get_species(cls):
        return cls.species

    #a static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"


#instantiate a class
i = Human(name="Ian")
print i.say("hi")

j = Human("Joel")
print j.say("hello")

#call our class method
print i.get_species()

Human.species = "H. neanerthalensis"
print i.get_species()
print j.get_species()

#call static method
print Human.grunt()


###################
#6. modules
###################

import math
print math.sqrt(16) #=>4

#you can get specific func from module
from math import ceil,floor
print ceil(3.7) #=>4.0
print floor(3.8) #=>3.0

#you can import all functions from a module
from math import *

#you can shorten module names
import math as m
print math.sqrt(16) == m.sqrt(16)

#python modules are just ordinary python files.
#you can write your own , and import them,
#then name of the module is the same as
#the name of the file

import math
print dir(math)
import sys,os
print dir(sys)
print dir(os)
