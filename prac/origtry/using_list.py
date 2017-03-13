#!/usr/bin/python2
#filename:using_list.py

#This is my shopping list
shoplist=['apple','mango','carrot','banana']

print 'I have',len(shoplist),'item to purchase'
print 'These item are:', #notice the comma at the end of the line
for item in  shoplist:
    print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list now ',shoplist

print 'I will sort my list now'
shoplist.sort()
print 'sorted shoplist is',shoplist

print 'the first item I will buy is',shoplist[0]
olditem=shoplist[0]
del shoplist[0]
print 'I bought the',olditem
print 'My shoplist now',shoplist
