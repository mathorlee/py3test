#coding=utf8
'''
Created on 2018年9月20日

@author: Administrator
'''

import weakref

class ExpensiveObject(object):
    def __del__(self):
        print '(Deleting %s)' % self
        
def callback(reference):
    """Invoked when referenced object is deleted"""
    print 'callback(', reference, ')'

obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print 'obj:', obj
print 'ref:', r
print 'r():', r()

print 'deleting obj'
del obj
print 'r():', r()