# -*- coding: utf-8 -*_

from sys import argv

script, input_file = argv

#print file's content
def print_all(f):
    print f.read()

#define a rewind function to reset pos of file to start
def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print line_count, f.readline(),
#print the line num and that line's content

current_file = open(input_file) #open file

print "First let's print the whole file:\n"

print_all(current_file) #print file's content

print "Now let's reiwnd, kind of like a tape."
rewind(current_file) #reset pos to 0

print "Let's print three lines:"

#print line and linenum , then add linenum by 1 and print again a line
#so linenum match content
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
