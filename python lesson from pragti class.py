 #THIS IS PROGRAM WHICH I RUN 

#TRANGLE OF STAR
print("\n*")
print("*" * 2)
print("*" * 3)
print("*" * 4)
print("*" * 5)

# DATA TYPE AND CONVERTING THEM
a = 9
b = 1
c = 2
d = 3
e = 5
print("\n",a)
print(type(a))
print(float(a))
print(b)
print(type(b))
print(float(b))
print(c)
print(type(c))
print("int in float",str(c))
print(e)
print(type(e))
print(float(e))

#5 INPUT AND THERE CONVERSION ON OTHER DATA TYPE
print("\nint in complex",complex(a))
print("int in complex",complex(b))
print("int in complex",complex(c))
print("int in complex",complex(d))
print("int in complex",complex(d))

print("\nint in string",str(a))
print("int in string",str(b))
print("int in string",str(c))
print("int in string",str(d))
print("int in string",str(e))
f=True
g=False


# ADDITON OF DIFFERENT TYPE OF DATA
a = int(input("Enter number"))
b = int(input("Enter number"))
c = int(input("Enter number"))
d = int(input("Enter number"))
e = int(input("Enter number"))
print(a+b+c+d+e)

f = input("Enter string")
g = input("Enter string")
h = input("Enter string")
i = input("Enter string")
j = input("Enter string")
print(f+g+h+i+j)

k = complex(input("Enter complex number"))
l = complex(input("Enter complex number"))
m = complex(input("Enter complex number"))
n = complex(input("Enter complex number"))
o = complex(input("Enter complex number"))
print(k+l+m+n+o)

p = float(input("Enter float number"))
q = float(input("Enter float number"))
r = float(input("Enter float number"))
s = float(input("Enter float number"))
t = float(input("Enter float number"))
print(p+q+r+s+t)

#OPERATOR BASIC ARITHMATIC 
a=int(input('enter noumber : '))
b=int(input('enter noumber : '))
print('using + operater ',a+b)
print('using - operater ',a-b)
print('using * operater ',a*b)
print('using / operater ',a/b)
print('using % operater ',a%b)
print('using // operater ',a//b)

#MARKS AND PERSENTAGE
a=int(input('enter marks of 1 subject : '))
b=int(input('enter marks of 2 subject : '))
c=int(input('enter marks of 2 subject : '))
d=int(input('enter marks of 2 subject : '))
e=int(input('enter marks of 2 subject : '))
total=a+b+c+d+e
per=total/500*100
print('total marks :',total)
print('percentage : ',per)

# CONVERT INTO DEGREE 
a=int(input('enter number : '))
b=(a * 9/5) + 32 
print(b)

#HOUR INTO DAY AND HOURS
a=int(input('enter no'))
b=a%24
c=a//24
print('day',c)
print('hours',b)

#CONPARISION OPERATOR
a=int(input('enter the number'))
b=int(input('enter the number'))
print('using > operater',a>b)
print('using < operater',a<b)
print('using == operater',a==b)
print('using >= operater',a>=b)
print('using <= operater',a<=b)
print('using != operater',a!=b)

#USE OF AND , OR OPERATOR
a=int(input('enter the number'))
b=int(input('enter the number'))
c=int(input('enter the number'))
d=int(input('enter the number'))
e=int(input('enter the number'))
print('if all no. is grater then 50 then it will print true \n ',a>50 and b>50 and c>50 and d>50 and e>50)
print('if any  no. is grater then 50 then it will print true \n  ',a>50 or b>50 or c>50 or d>50 or e>50)

# bitwise operator
h=int(input("enter number "))
b=int(input("enter number "))

print('using << operator',h<<1)
print('using >> operator',h>>1)
print('using ~ operator',~h)
print('using & operator',h&b)
print('using | operator',h|b)
print('using ^ operator',h^b)


#3digit input addition
a=int(input('enter three digit number'))
c=int(input('enter three digit number'))
b=int(input('enter three digit number'))
d=a+b+c
print(d)


#inches into feet
a=int(input('enter inch'))
print('in feet',a/12)

#adding gst in bill 
a=int(input('enter the bill'))
a+=(18/100)*a
print('bill after adding 18% gst',a)

#GST + AMOUNT =TOTAL
a=int(input('enter the bill'))
b=a
a-=(18/100)*a
print('bill after adding 18% gst then bill is ',a)
c=b-a

#list 
a=[12,23,34,45,56,67,78,89,90]
b=[12,23,34,45,56,67,78,89,90]

#accening values
print(a,"\n",b)
print(a[2:7])
print(b[-8:-3])
print(a[2:7])=98,87,76,65,54
print('after arith matic operation of 2 list')
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

#  remove by  pop
a.pop()
a.pop()
a.pop()
b.pop()
b.pop()
b.pop()

# remove by values
a.remove(12)
print(a)

#list second day
a=[1,2,3,4,5,6,7,8]
print(a)
a.insert(8,9)
print(a)
a.reverse()
print(a)
a.clear()
print(a)
print('bill after adding 18% gst is ',c)

#list product
a=['cpu','mouse','monitor','printer','speaker']
b=[5,5,5,5,5]
c=[7000,200,3000,5000,4000]

print('item \t\t qty \t price \t\t total\n')
print(a[0],'\t\t',b[0],'\t',c[0],'\t\t',b[0]*c[0])
print(a[1],'\t\t',b[1],'\t',c[1],'\t\t',b[1]*c[1])
print(a[2],'\t',b[2],'\t',c[2],'\t\t',b[2]*c[2])
print(a[3],'\t',b[3],'\t',c[3],'\t\t',b[3]*c[3])
print(a[4],'\t',b[4],'\t',c[4],'\t\t',b[4]*c[4])
print("\n\n total bill  is ",b[0]*c[0]+b[1]*c[1]+b[2]*c[2]+b[3]*c[3]+b[4]*c[4])


# by using tuple list
a=('cpu','mouse','monitor','printer','speaker')
b=(5,5,5,5,5)
c=(7000,200,3000,5000,4000)

print('item \t\t qty \t price \t\t total\n')
print(a[0],'\t\t',b[0],'\t',c[0],'\t\t',b[0]*c[0])
print(a[1],'\t\t',b[1],'\t',c[1],'\t\t',b[1]*c[1])
print(a[2],'\t',b[2],'\t',c[2],'\t\t',b[2]*c[2])
print(a[3],'\t',b[3],'\t',c[3],'\t\t',b[3]*c[3])
print(a[4],'\t',b[4],'\t',c[4],'\t\t',b[4]*c[4])
print("\n\n total bill  is ",b[0]*c[0]+b[1]*c[1]+b[2]*c[2]+b[3]*c[3]+b[4]*c[4])  


# by using user define list
a=[0,0,0,0,0]
b=[0,0,0,0,0]
c=[0,0,0,0,0]
a[0]=(input('enter item '))
b[0]=int(input('enter quentity '))
c[0]=int(input('enter price'))
print('\n')
a[1]=(input('enter item '))
b[1]=int(input('enter quentity '))
c[1]=int(input('enter  price '))
print('\n')
a[2]=(input('enter item '))
b[2]=int(input('enter quentity '))
c[2]=int(input('enter  price '))
print('\n')
a[3]=(input('enter item '))
b[3]=int(input('enter quentity '))
c[3]=int(input('enter  price '))
print('\n')
a[4]=(input('enter item '))
b[4]=int(input('enter quentity '))
c[4]=int(input('enter  price '))
print('\n')

print('item \t qty \t price \t\t total\n')
print(a[0],'\t',b[0],'\t',c[0],'\t\t',b[0]*c[0])
print(a[1],'\t',b[1],'\t',c[1],'\t\t',b[1]*c[1])  
print(a[2],'\t',b[2],'\t',c[2],'\t\t',b[2]*c[2])
print(a[3],'\t',b[3],'\t',c[3],'\t\t',b[3]*c[3])
print(a[4],'\t',b[4],'\t',c[4],'\t\t',b[4]*c[4])
print("\n\n total bill  is ",b[0]*c[0]+b[1]*c[1]+b[2]*c[2]+b[3]*c[3]+b[4]*c[4])



#set list operation
a={1,2,3,4,5}
b={4,5,6,7,8}
c={3,4,5,6,7,8,9}
print(a)
print(b)
a.update(c)
print(a)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.intersection_update(b))
print(a.difference_update(b))
print(a.symmetric_difference_update(b))
print(a.symmetric_difference(b))
a={1,2,3,4,5}
b={4,5,6,7,8}
a.remove(1)
print(a)
a.discard(4)
print(a)
a.clear()
print(a)


  
#if condition for move 
a=int(input('choose option\n1.Bollywood\n2.Tollywood\n3.Hollywood'))
if a==1:
    b=int(input('\nchoose option\n1.bazigar\n2.we meet\n3.uri\n'))
    if b==1:
        print('har kar jitne wale ko bazigar kehte hai')
    elif b==2:
        print('mai apni hi favrot hu')
    elif b==3:
        print('how\'s the josh')
    else:
        print('invalid option')
elif a==2:
    b=int(input('\nchoose option\n1.bazigar\n2.we meet\n3.uri\n'))
    if b==1:
        print('har kar jitne wale ko bazigar kehte hai')
    elif b==2:
        print('mai apni hi favrot hu')
    elif b==3:
        print('how\'s the josh')
    else:
        print('invalid option')
elif a==3:
b=int(input('\nchoose option\n1.bazigar\n2.we meet\n3.uri\n'))
    if b==1:
        print('har kar jitne wale ko bazigar kehte hai')
    elif b==2:
        print('mai apni hi favrot hu')
    elif b==3:
        print('how\'s the josh')
    else:
        print('invalid option')
else:
    print('invalid option')





  a=0
  b=1
  while b<=5:
    a+=int(input('enter no'))
    b+=1
 print('addition',a)


# program fo min max sum avg
a=int(input("how many no. you want to enter\n"))
b=1 
d=0
f=min=max=int(input("Enter no."))
while b<a:
    c=0
    c=int(input("Enter no."))
    if c>max:
        max=c
    if c<min:
        min=c
    d+=c
    b+=1 
d+=f
print("sum ",d)
e=d/a 
print("average ",e)
print("max ",max)
print("min ",min)


# PROGRAM FOR ADDTION OF DIGIT      
n=int(input('enter no. for digit addition'))
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(sum)


# program for revers list and addition of it 
a=[1,2,3,4,5]
b=[1,2,3,4,5]
a.reverse()
c=0
while c<len(a):
     print(a[c],+b[c],a[c]+b[c],sep='  ')
     c+=1


 
a=[1,2,3,4,5]
# program for addition of starting and ending number
a=[1,2,3,4,5]
b=[1,2,3,4,5]
a.reverse()
c=0
d=len(a)-1
print("addition of starting and ending number")
while c<len(a):
     print(a[c],+b[c],a[c]+b[d],sep='  ')
     c+=1
     d-=1


  
# program for addition oof less then 1000 number
print(" addition  tilll the number is under 1000")
a=0
while a<1000:
    a=a+int(input("enter no")) 
    print(a)



#program for addition of user given matrix
a=[]
b=[]
c=0
while c<3:
    a.append([])
    print('')
    d=0
    while d<3:
        a[c].append(int(input("enter number : ")))
        d+=1 
    c+=1
c=0
while c<3:
    b.append([])
    print('')
    d=0
    while d<3:
        b[c].append(int(input("enter number : ")))
        d+=1 
    c+=1

print("first matric")
c=0
while c<3:
    d=0
    while d<3:
        print(a[c][d],end="\t")
        d+=1
    print('\n')
    c+=1
    
    print("second matric")
c=0
while c<3:
    d=0
    while d<3:
        print(b[c][d],end="\t")
        d+=1
    print('\n')
    c+=1

print("addition of matric")
c=0
while c<3:
    d=0
    while d<3:
        print(a[c][d]+b[c][d],end="\t")
        d+=1
    print('\n')
    c+=1
   
#program for entered number to table
a=int(input("enter number "))

for b in range(1,11):
    print(a,"*",b,"=",a*b)


      # Payal bagul  : Matrix Addition.
m1=[]
m2=[]
for a in range(3):
    m1.append([])
    for b in range(3):
        m1[a].append(int(input("Enter Number : &quot")))

for a in range(3):
    m2.append([])
    for b in range(3):
        m2[a].append(int(input("Enter Number : ")))
        
print("Matrix 1:")       
for a in range(3):
    m1.append([])
    for b in range(3):
        print(m1[a][b],end="\t")
    print("")
        
print("Matrix 2: ")       
for a in range(3):
    for b in range(3):
        print(m2[a][b],end="\t")
    print("")
        
print("Addirion Matrix : ")       
for a in range(3):
    for b in range(3):
        print(m1[a][b]+m2[a][b],end="\t")
    print("")



def a1():
    b=0
    while b<=40:
        print("=",end="")
        b+=1

def a2():
    b=0
    while b<=40:
        print("-",end="")
        b+=1

def a3():
    b=0
    while b<=40:
        print("\\",end="")
        b+=1

def a4():
    b=0
    while b<=40:
        print("/",end="")
        b+=1

def a5():
    b=0
    while b<=40:
        print("*",end="")
        b+=1

a1()
print("")
a2()
print("")
a3()
print("")
a4()
print("")
a5()
print("")

a1=int(input("enterr no of col"))
b1=int(input("enter no of row"))
c1=int(input("enter no of martrix"))

m1=[]

for c in range(c1):
    for a in range(a1):
        m1.append([])
        for b in range(b1):
            m1[a].append(int(input("Enter Number :")))



      def p(a,*b):
    for c in b:
        a+=c
    print("addition:",a)
    
p(25,25,14,25)

class car:
      def car(model="m70",color="black",hight=50):
    print(" model ",model)
    print(" color ",color)
    print(" hight ",hight)
car(model="m72")

      class car:
      def brek(a)
          print("break")
   b.a()


      class bank:
    bb=0
    def d(self,a):
        self.bb+=a 
        print(&quot;amount in your account is &quot;,self.bb)
    def __init__(self,a):
        print(&quot;hello new user to this aacount \n your ba;ance is &quot;,a)
    def __del__(self):
        print(&quot;have a nice day&quot;)
asd=bank(5)
asd.d(50)


      

      //pip install matplotlib
      
import matplotlib.pyplot as p
import random as r
b=[]
p.subplot(1,2,1)
for c in range(10):
    b.append([])
    for a in range(10):
        b[c].append(r.randint(1,100))
    p.plot(b[c])


p.subplot(1,2,2)
d=[]
for c in range(10):
    d.append([])
    for a in range(10):
        d[c].append(r.randint(1,100))
    p.plot(d[c])
p.show()

      
import matplotlib.pyplot as p
a=[1,2,3,4,5]
b=[6,7,8,9,4]
p.barh(a,b)
p.show()

import matplotlib.pyplot as p 
import random as r

y=[]
for a in range(5):
    y.append(r.randint(1,10))
p.plot(y)
p.show() 




      
# increptiion and decreaption

a="abcdefghijklmnopqrstuvwxyz"
b="1234567890abcdefghijklmnop"
i=input(" entern password : ")
l=[]
for c in i:
    e1=a.index(c)
    l.append(e1)
    print(b[e1],end="")
for d in l:
    print(a[d],end="")




json to python vice
      sql phpmy admin

try: 
     a=int(input ("enter no"))
     if a%2==0:
     raise nameError
     
       print ("even")
     else:
       print ("odd")
except :
     print ("enter correct number")
else ://if successfully done
     print("done")
finally ://after its done
     print("thanks")
     


      