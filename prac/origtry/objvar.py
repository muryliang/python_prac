#!/usr/bin/python2
#filename:objvar.py

class Person:
    '''represents a person'''
    population=0

    def __init__(self,name):
        '''initializes the person's data'''
        self.name=name
        print '(Initializing %s)'%self.name

        #when this person is created , he/she
        #adds to the population
        Person.population+=1

    def __del__(self):
        '''I am dying'''
        print '%s says goodbye'%self.name
        Person.population-=1
    
        if Person.population==0:
            print "I am the last one"
        else:
            print "there are still %d people left"%Person.population

    def sayhi(self):
        '''Greeting by the person
            
        Really that's all  it does'''

        print "Hi, my name is %s"%self.name

    def howmany(self):
        '''prints the current person'''
        if Person.population==1:
            print 'I am the only person here'
        else:
            print 'we have %d people here'%Person.population

swaroop=Person('Swaroop')
swaroop.sayhi()
swaroop.howmany()

kalam=Person('Kalam')
kalam.sayhi()
kalam.howmany()

swaroop.sayhi()
swaroop.howmany()

print 'about to delete'
del kalam

haha=Person('haha')
haha.sayhi()
haha.howmany()



    
        
