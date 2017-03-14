#-*- coding: utf-8 -*-

formatter = "%r %r %r %r"

#now format is in a stirng , just use
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
#formatter string at trailing will just as a normal string for one %r at front
print formatter % (formatter, formatter, formatter, formatter)
print "%s %s %s %s" % (formatter, formatter, formatter, formatter)
print formatter
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
)
#this will print s 5 times as a string
print "%s"%'s'*5
print "%d "%2
print "chinese %s"%"哈哈"
