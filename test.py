# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:48:47 2019

@author: Alin
"""
import random

def fraction():
    while(True):
        a=random.randint(1,100)
        b=random.randint(1,100)
        if a/b<1:
            return str(a)+"/"+str(b)
            break
        
def brackets():
    a="("
    e=")"
    b=str(random.randint(1,100))
    c=random.choice('+-*/')
    d=fraction()
    if eval(b+c+d)>0:
        return a+b+c+d+e
    
for i in range(10):
    a= brackets()
    b=str(random.choice('+-*/'))
    c=fraction()
    d=a+b+c
    if eval(d)>=0:
        print(a,b,c,"=")
