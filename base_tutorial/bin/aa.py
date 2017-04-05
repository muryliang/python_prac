def aa(*tup, **dic):
    print "tup is",tup
    print "dic is",dic
    print "pass to subfunc"
    bb(*tup,**dic)

def bb(*tup, **dic):
    print "in bb tup is",tup
    print "in bb dic is",dic

def glo():
    aa=1
    bb=2
    globals()['gg']='two'
    print globals()
    print locals()
    print vars()

class mm(object):
    song = 2
    def sing(self):
        print self.song
    def modify(self,name):
        self.song=name
    def modify2(self,name):
        mm.song=name
    def base(self):
        print mm.__bases__

class nn(mm):
    pass

try:
    a = int(raw_input("one: "))
    b = int(raw_input("two: "))
    print a/b
except (ZeroDivisionError,TypeError,ValueError),e:
    print "error is :%s:"%e
