
def mawjoud (a,t):
    b=False;k=0
    while k<len(t) and not(b):
        if t[k]==a: b=True
        else : k+=1
    return b
def effacer (x,y):
    return y[:y.find(x)]+y[y.find(x)+1:]
def anag (a,b):
    t=True
    while a!='' and t :
        if mawjoud (a[0],b):
            x=a[0]
            a=effacer(x,a)
            b=effacer(x,b)
            
        else :
            t=not(t)
    return t
#pp
ch1=str(input('ch1 :'))
ch2=str(input('ch2 :'))
print (anag(ch1,ch2))
            
    