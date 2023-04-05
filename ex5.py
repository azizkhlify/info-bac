from random import randint
def generer():
   return randint(10000000,99999999)
def afichier(n):
   k=1;ch='________';s=str(n)
   while k<=5:
       c=str(input('chiffre:'))
       while len(c)!=1:
          c=str(input('chiffre:'))
       if s.find(c)!=-1: 
            ch=''
            for i in range(8):
                if s[i]==c: ch+=c
                else: ch+='_'
       print(ch)
       
                