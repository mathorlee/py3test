#coding=utf8
'''
Created on 2018年9月20日

@author: Administrator
'''

class C(object): 
    a = 'abc'
    def __getattribute__(self, *args, **kwargs): 
        print("__getattribute__() is called") 
        return object.__getattribute__(self, *args, **kwargs) 
    #    return "haha" 
    def __getattr__(self, name): 
        print("__getattr__() is called ") 
        return name + " from getattr"
      
    def __get__(self, instance, c): 
        print("__get__() is called", instance, c) 
        return self
      
    def foo(self, x): 
        print(x) 
  
class C2(object): 
    d = C() 

class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val

class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

if __name__ == '__main__': 
#     c = C() 
#     c2 = C2() 
#     print(c.a) 
#     print(c.zzzzzzzz) 
#     c2.d 
#     print(c2.d.a) 
    