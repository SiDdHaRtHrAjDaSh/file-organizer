# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:54:16 2020

@author: SIDDHARTH RAJ DASH
"""

import os
import re
import shutil
os.getcwd()
os.chdir('C:/Users/ATMSI/Downloads')
print(os.getcwd())
print(os.listdir())

list1=os.listdir()
l2=[]
substr="Reference_Material"
for i in list1:
    if substr in i:
        l2.append(i)
list1
J=[]
sem=[]
subject=[]



for i in range(len(l2)):
    k=l2[i]
    j=k.split("_")
    sem.append(j[0])
    str1=j[0]
    str2=j[1]
    strn=str1+"_"+str2
    subject.append(strn)
    del j[3:8]
    j.append(l2[i])
    J.append(j)
    j=[]
    


for i in range(len(J)):
    t=J[i]
    str1=""
    for k in t[3:-1]:
        str1=str1+k+" "
    del J[i][3:-1]
    J[i].insert(3,str1)    

    
subject
SUBJECT=list((set(subject)))

SUB=[]
print(SUBJECT)

for i in SUBJECT:
    n=i.split("_")
    SUB.append(n)
    n=[]
print(SUB)

print(sem)
SEM=list(set(sem))
print(SEM)

COMPONENT=['ETH','ELA','EPJ']

for i in SEM:
    try:
        os.mkdir(i)
    except FileExistsError:
        continue
    
for i in SUB:
    os.chdir(i[0])
    try:
        os.mkdir(i[1])
    except FileExistsError:
        print("exists")
    os.chdir('C:/Users/ATMSI/Downloads')
    

for i in range(len(J)):
    path='C:/Users/ATMSI/Downloads'
    path1='C:/Users/ATMSI/Downloads'
    path1=path1+"/"+J[i][0]+"/"+J[i][1]
    
    try:
        os.rename(path+"/"+J[i][-1],path+"/"+J[i][-2])
        shutil.move(path+"/"+J[i][-2],path1+"/"+J[i][-2])
    except FileExistsError:
        continue
    os.chdir(path)
    
