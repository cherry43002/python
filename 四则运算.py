# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:48:47 2019

@author: Alin
"""
#导入random模块
import random

#定义产生真分数的函数
def fraction():
    while(True):
        a=random.randint(1,100)
        b=random.randint(1,100)
        if a/b<1:
            return str(a)+"/"+str(b)
            break
        

#定义产生带括号运算函数 
def brackets():
    a="("
    e=")"
    b=str(random.randint(1,100))
    c=random.choice('+-*/')
    d=fraction()
    if eval(b+c+d)>0:
        return a+b+c+d+e


#生成并打印四则运算表达式
for i in range(30):
    a= brackets()
    b=str(random.choice('+-*/'))
    c=fraction()
    if eval(a+b+c)>=0:
        print(a,b,c,"=","        答案:",eval(a+b+c))
