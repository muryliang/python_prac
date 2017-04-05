def aa():
    global a 
    a = 2
    print "a is", a
    del a

a = 20
print "before aa(), a is", a
aa()
print "after aa(), a is", a
