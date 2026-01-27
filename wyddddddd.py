'''
#smile face
zime=input("izvēlies :), :(, :/, :>, :| ")
#definēt funkciju convert
def convert(zime):
    if zime==":)":
        print("😁")
    elif zime==":(":
        print("😖")
    elif zime==":|":
        print("😑")
    elif zime==":/":
        print("😞")
    elif zime==":>":
        print("🙂")
    else:
        print("🤡🤡🤡🤡🤡🤡")

convert(zime)


for x in range (10): #no 1 līdz 10
    print(x+1)
for x in range (1,10+1): #no 1 līdz 10
    print(x)
for x in range (1,11): #no 1 līdz 10
    print(x)

#uzdevums dilstošā secībā
for n in range(20,0,-1):
    print(n)


for x in range(1,10):
    y=x**2+3*x-2
    print(f'ja x={x}, tad y{y}')


import random
#brīvi ģenerētais skaitlis
x=random.randint(0,8)
y=random.randint(0,8)
print(x)


#a)
#bibliotēka brīvi ģenerēta skaitļa izveidei
import random
#skaitļu skaits m
m=int(input("m: "))

for i in range(m):
    #ģenerēs skaitli
    sk=random.randint(0,60)
    print(f'{i+1}. {sk}')

#b)
import random
m=int(input("m: "))

for i in range(m,0, -1):
    sk=random.randint(0,60)
    print(f'{i}. {sk}')

#skaitļu skaits
c=int(input("skaitļu skaits: "))
summa=0#sākotnēja summas vērība
for k in range(c):
    sk=int(input("sk: "))
    summa+=sk
    print(summa)#starprezultāts
print("sum=",summa)#gala rezultāts

import math #importēju math bibliotēku
for n in range(7,13):
    #print(n**2)#kāpināšanas zīme
    print(math.pow(n,2))

import math
#kvadrātsaknes
for q in range(27,17,-1):
    print(math.sqrt(q))#kvadrātsakne
    #print(k**0.5)#kvadrātsakne ar pakāpi

for s in range(1,50):
    if s%3==0 or s%5==0:
        print(s)
    else:
        print("nedalās ne ar 3, ne ar 5")

n=int(input("n: "))
if n>1:
    for d in range(1,n):
      print(d,d**2)
else:
    for d in range(n,1):
      print(d,d**2)

for s in range (1,20):
    if s%2==0:
        continue
    else:
        print(s,"ir nepāra")

n=int(input("n: "))#skaitļu skaits
sum=0
for i in range(n):#atkārto n reizes
    sk=int(input("sk: "))#pieprasa ievadīt skaitli
    if sk>=0: #vai skaitlis ir pozitīvs
        sum+=sk
    else:
        break #pārtraukt ciklu
print("pozitīvo skaitļus summa",sum)

n=int(input("n: "))

for i in range(n):
    if i%3==0:
        print("dalās ar 3")
    elif i%5==0:
        print("dalās ar 5")

#1. uzd
while True: #bezgalīgais cikls
    sk=int(input("sk: "))#pieprasa ievadīt skaitli
    if sk%3==0 or sk%5==0: #pārbauda vai dalās ar 3 vai ar 5
      break #apstādina ciklu
    elif sk%4==0:
      continue#izlaiž darbību,bet turpina ciklu
    else:
      print("nedalās ne ar 3, ne ar 5, ne ar 4.")

#2. uzd
#(k,n)
k=int(input("k: "))#sākotnējā vērtība
n=int(input("n: "))#beigu vērtība

while k<=n:
   print(k)
   k+=1
#3 uzd
k=int(input("k: "))#sākotnējā vērtība
n=int(input("n: "))#beigu vērtība

if k<n:
    while k<n:
        print(k)
        k+=1
elif n<k:
    while n<k:
        print(k)
     k-=1
else:
    print("k=n")

import random
m=int(input("m: "))#beigu vērtība

s=0#sākotnējā vērtība
while s<m:
    sk=random.randint(0,20)
    print(sk)
    s+=1

#1lats=1.42 eur
lats=1.42
latusk=float(input("cik latu?: "))
def pelmenis(lats,latusk):
   print(f'{lats*latusk:.2f} eur.')

pelmenis(lats,latusk)
'''
zero_pepsi=50#viena pepsas pudele
summa=0

def automats(zero_pepsi,summa):
    nauda=int(input("naudas daudzums= "))
    while summa<=50:
        if nauda==20 or nauda==10 or nauda==5:\
        #cik iemests iekšā
            summa += nauda
            print(f"iemaksāts: {summa}")
            if zero_pepsi-summa>=0:
            #cik vēl ir jāsamaksā
                print(f"vēl trūkst {zero_pepsi-nauda}")
            else:
                print(f"atlikums {zero_pepsi - summa}centi")
        else: #uz naudu,kas nav 10,20 vai 5
            print("automāts naudu ņam ņam")
automats(zero_pepsi,summa)