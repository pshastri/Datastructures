#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print arr
i=len(arr)-1
print i
arr1=[]
while i>-1:
	arr1.append(arr[i])
	i-=1
print str(arr1)