#!/usr/bin/env python
#coding:utf-8
_author__ = 'geiao'

def binary_search_while(mylist,find):
    left=0
    right=len(mylist)-1
    while left<=right:
        midpoint=(left+right)/2
        if find==mylist[midpoint]:
            return midpoint+1
        elif find<mylist[midpoint]:
            right=midpoint-1
        else:left=midpoint+1
test_list=[1,5,2,3,4,11,43,12]
test_list.sort()
print "数组长度:%d"%len(test_list)
print test_list
print "位置为:%d"%binary_search_while(test_list,3)