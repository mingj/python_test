__author__ = 'geiao'

import Fclass


class Sub_class(Fclass.Father_class):
    def __init__(self,x,y):
        Fclass.Father_class.__init__(self,x)
        self.y=y
    def print_sub_class(self):
        print 'sub print x:%s'%self.x
        print 'sub print y:%s'%self.y
        print 'sub print x:%s,y:%s'%(self.x,self.y)






a=Fclass.Father_class(2)
print a.print_father_class()

b=Sub_class(3,4)
b.print_sub_class()

