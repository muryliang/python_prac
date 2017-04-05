#!/usr/bin/python2
#filename:inherit.py

class SchoolMember:
    '''represents any school member'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print '(initialized school member %s)'%self.name

    def tell(self):
        '''tell my details'''
        print 'Name:"%s" Age:"%s"'%(self.name,self.age),

class Teacher(SchoolMember):
    '''represents a teacher'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print 'Initialized Teacher:%s'%self.name

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary:"%d"'%self.salary
        print 'teacher\' selfage is',self.age

class Student(SchoolMember):
    '''represents a student'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print '(initialized Student: %s)'%self.name

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks:%d'%self.marks


t=Teacher('Mrs. Shrividya',40,30000)
s=Student('Swaroop',22,75)

print #prints a blank line

members=[t,s]
for member in members:
    member.tell()
