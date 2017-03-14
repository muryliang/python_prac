#-*- coding: utf-8 -*-

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* fishies
\t* Catnip\n\t* Grass
"""

thin_cat = '''
I'll do a list:
\t* Cat food
\t* fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print thin_cat
print 'haha\bhehe'
#print 'aa\fbb\ncc\fcc'
print 'aaaaa\r\b\b\b\bbbb'
print 'aa\vbb\vcc'
print u'\U0001F47E'
#while True:
#        for i in ["/","-","|","\\","|"]:
#            print "%s\r" % i,
print "now print :%r:"%"haha\nhehe\thihi\rhan"
print "now print :%s:"%"haha\nhehe\thihi\rhan"
