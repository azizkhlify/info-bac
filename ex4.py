def saisir():
    n=int(input('n='))
    if n>0: return n
    else : return saisir()
def div11(n):
    s1=0;s2=0;s=str(n)
    for i in range (len(s)):
        if i%2==0:
            s2+=int(s[i])
        else:
            s1+=int(s[i])
    return (s1-s2)%11==0
#pp
n=saisir()
print(div11(n))