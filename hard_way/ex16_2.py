# -*- coding: utf-8 -*-

filename = raw_input("input a filename: ")
target = open(filename, 'r')
print target.read()
target.close()
