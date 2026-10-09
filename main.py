#print("Hello, World!")
#sher="mahis coder"
#print(sher[0:6:2])

#a=10
#=bool(a)
#print( a)
#name="mahi"
#age=20
##print("Hello, ",name, "your age is", age)
#print (f"Hello {name} your age is {age}")
#input("Enter your name: ")
"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print (f"Hello {name} your age is {age}")

a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b%a)
print(a//b)
print(b//a)
print(a**b)
print(3**3)
#compound assignment operator
a=5
b=5
a += 5
b -= 5
print(a)
print(b)
c=13
if c>33:
  print("c is greater than 33")
elif c==33:
   print("c is equal to 33")
else:
   print("c is less than 33")

 
 
 
d = range(1,20,1)

for i in d:
    print(i)

  

for i in range(20,51):
    print(i)

n=int(input("Enter a number: "))
for i in range(n,n*2):
    print(i)
e="mahi"
for i in e:
    print(i)
for i  in range(len(e)):
    print(e[i])
def sum(a,b):
     print(f"the sum of {a} and {b} is {a+b}")  

sum(5,10)


a=[1,2,3,45,True,False,"mahi",print()]

print(a[0:5])
for i in range(len(a)):
     print(a[i])

a.append("mahis")
a.insert(2,"mahi")
print(a)
a.extend([1,2,3,4])
print(a)
a.remove(2)
print(a)

l=[1,2,3,4,5,6,7,8,9]
sum=0
for i in l:
    sum+=i
print(sum/len(l))


l=[12.3,4.5,15.5]
largest=l[0]
index=0
for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index=i
print(largest)
print(index)



l=[12,16,13,19,17]
largest=l[0]
second_largest=l[0]
for i in l:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i

print(largest)
print(second_largest)

a=[1,4,3,4,5,6,7,8,9]
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        continue
        
    else:
        print("not sorted")
        break
else:
    print("sorted")


a=(3,4,5,5,5,6)

ind= a.index(5)
print(ind)
count=a.count(5)
print(count)

b,c,d,c=(1,2,3,4)
print(b)
print(c)
print(d)
print(c)
 

s= {1:"hello",2:56,"mahi":True}

s.update({3:"mahis",4:56})

s[40]="ma"
s[1]="peck"
del s[2]
print(s)


s={10:200,20:400,30:600}

for i in s:
    print(s[i])

for i in s.values():
    print(i)




a=[1,2,3]
b=a
#b[0]=100
print(a)

b=a.copy()
b[0]=100    
print(a)

d={1:"mahi",2:"mahis",3:"mahi"}
d2=d.get(2)
print(d2)
print(d.items())


d1={10:200,20:400,40:600}
d2={40:800,50:1000,60:1200}

a=[1,1,1,2,1,2,2,1,3,4,5,4]
d={}

for i in d2:
    d1[i]=d2[i]

print(d1)

sum=0
for i in d1:
    sum+=d1[i]  
print(sum)


for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)

 
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i] 
        print(d1)

        
a= int(input("Enter a number: "))
try:
    print(10/a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("This code will always execute.")

a= int(input("Enter a number: "))
try:
    print(10/a)
except Exception as e:
    print(f"Error: {e}")

else:
    print("No exception occurred.")
finally:
    print("i will run no matter what.")


age= int(input("Enter your age: "))
try:
    if age<10 or age>18:
        raise ValueError("Age must be between 10 and 18.")
    else:
         print("Age is valid for club.")

except ValueError as e:
      print(f"Error: {e}")

print("The club will start soon.  ")


p=open(r'C:/Users/Afzal Kabir/Desktop/dfd.txt')

print(p.read())
p=open('superman.txt','a')
p.write("addd apende.\n")
p.close()

     
class Factory():
    def __init__(self,material,zips,pockets):
        self.material=material
        self.zips=zips
        self.pockets=pockets
    def show(self):
        print(f"Material:{self.material},Zips:{self.zips},Pockets:{self.pockets}")
       


              





reebok= Factory("leather", 5, 2)

campus= Factory("canvas", 3, 4)

reebok.show()
campus.show()


"""

class Animal:
    name="lion" #class attribute

    def __init__(self,age):
        self.age=age #instance attribute
    def show(self):    #instance method
        print(f"Age is {self.age}")
    @classmethod
    def hello(cls):
        print("how are you")
    @staticmethod
    def static():
        print ("how are you")

obj=Animal(12)
obj.show()
obj.hello()
obj.static()

