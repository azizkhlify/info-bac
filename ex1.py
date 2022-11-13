from numpy import array
from random import randint
def saisir ():
    n=int(input('n='))
    while n<0:
        n=int(input('n='))
    return n
def mawjoud (a,t):
    b=False;k=0
    while k<len(t) and not(b):
        if t[k]==a: b=True
        else : k+=1
    return b
def remplir1(n):
    t=array([int]*n)
    t[0]=int(input('case '+str(1)+' :'))
    for i in range (1,n):
        t[i]=int(input('case '+str(i+1)+' :'))
        while not(t[i] in range (1,n+1)) or (mawjoud(t[i],t[:i])):
            t[i]=int(input('case '+str(i+1)+' :'))
    return t
def remplir2 (n):
    t=array([str]*n)
    for i in range (n):
        t[i]=chr(randint(ord('a'),ord('z')))
    return t
def afichier ():
    t3=array([str]*n)
    for i in range (n):
        t3[t1[i]-1]=t2[i]
    for i in range (n):
        print (t3[i])
#prog princi
n=saisir()
t1=remplir1(n)
print('t2 -------------------')
t2=remplir2(n)
for i in range (n):
    print(t2[i])
print('t3 -------------------')
afichier()
