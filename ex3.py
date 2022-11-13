def saisir():
    t=False
    while not t :
        n=int(input('n='))
        t= n>=1
    return n

def U (n):
    if n==1 :
        return 7
    if n==2:
        return 13
    a=7
    b=13
    c=0
    for i in range (2,n):
        c=2*b-a
        a=b
        b=c
    return c
#pp
n=saisir()
print(U(n))