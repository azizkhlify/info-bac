def remplir ():
    t=[];i=0
    x=int(input('case N°'+str(i+1)+' :'))
    while x>=0:
        t.append(x)
        i+=1
        x=int(input('case N°'+str(i+1)+' :'))
    return t

def affichier(t):
    for i in range(len(t)):
        y=[]
        k=i;s=0
        while s!=20 and k<len(t):
            s=s+t[k]
            y.append(t[k])
            k+=1
        if s==20:
            print(y)
#pp
t=remplir()
print('les series 20 :')
affichier(t)