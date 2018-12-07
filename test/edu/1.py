#coding=utf8
'''
Created on 2018年9月20日

@author: Administrator
'''

import sys
import weakref


class A():
    def __del__(self):
        print(hex(id(self)),' is dead!')
    
    def test(self):
        print('test')
    
    def __str__(self):
        return 'xxx'
    def __repr__(self):
        return 'yyy'
    
def callback(ref):
    print(hex(id(ref)),'dead callback!')

if __name__ == '__main__':
    a = A()
    print(sys.getrefcount(a)) #为啥一开始就是2呢？
    
    #弱引用不增加对象的refcount
    r1 = weakref.ref(a)
    r1().test()      #test
    print(r1() is a) #True
    print(weakref.getweakrefcount(a))  #2
    
    r2 = weakref.ref(a)
    print(r1 is r2) #未指定不同的回调函数时，这两个弱引用是相同的,True
    print(r1() is r2() is a)#True
    print(weakref.getweakrefcount(a))  #2
    
    r3 = weakref.ref(a,callback)
    print(r1 is r3)  #False
    
    #获取对象的弱引用对象个数
    print(weakref.getweakrefcount(a))  #2
    #获取对象的所有弱引用
    print(r1,r3)
    #(<weakref at 01B282D0; to 'instance' at 01B25A58>, <weakref at 01B28360; to 'instance' at 01B25A58>)
    print(weakref.getweakrefs(a)) 
    #[<weakref at 01AF82D0; to 'instance' at 01AF5A58>, <weakref at 01AF8360; to 'instance' at 01AF5A58>]
    
#     del a
    #('0x1bd9360', 'dead callback!') 回调函数先被调用
    #('0x1bd5a58', ' is dead!')
    
#     r4 = weakref.proxy(a)
#     print(weakref.getweakrefs(a)) 
#     r4.test()