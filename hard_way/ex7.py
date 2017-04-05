# -*- coding: utf-8 -*-

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
#this will print . for 10 times
print "." * 10 #what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#wantch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6, #connect first 6 single-char-string together,and next string on the 
#same line but after a blank
print end7 + end8 + end9 + end10 + end11 + end12 #the second string
print "%s %s" %(end1 + end2 + end3 + end4 + end5 + end6,
                end7 + end8 + end9 + end10 + end11 + end12)
print end7*20 + end5*2
