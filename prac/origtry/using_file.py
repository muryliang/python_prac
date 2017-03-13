#!/usr/bin/python2
#filename:using_file.py

poem='''\
programing is fun
when the work is done
if you wanna make your work also fun:
    use Python!
'''
lines=0

f=file('poem.txt','w') #open for write
f.write(poem) #write text to file
f.close()

f=file('poem.txt')
#if no mode is specified, read mode is default
while True:
    line=f.readline()
    if len(line)==0: #Zero length indicates EOF
        break
    print line,
    lines+=1
    #Notice comma to avoid automatic newline added by Python
f.close()
print 'line number is',lines
