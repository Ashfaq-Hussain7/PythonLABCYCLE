# -*- coding: utf-8 -*-
"""BasicPGM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZuVnUdOMkEKmetTKpvTa1FrK1J27wl9i
"""

print("hello world")

a=5.5
print(type(a))

a=5
print(type(a))

print(type("hello"))

b=True
print(type(b))

t=5+3j
print(type(t))

a=7
b=3
ab_sum=a+b
print(ab_sum)

a=9
b=1
ab_diff=a-b
print(ab_diff)

a=5
b=2
pro=5*2
print(pro)

a=1000
b=3
quotient=a//b
print(quotient)
rem=a%b
print(rem)
pow=a**b
print(pow)

a=10
b=20
c=30
avg=(a+b+c)/3
print(avg)

#name
name=input("Enter The Name Of The Student")
course=input("Enter The Name Of The Course")
semester=input("The Semester Number")
admission=input("Enter The Year Of Admission")
address=input("Enter The Address Of The Student")
print("The Details Are: \n"
      "Name:",name.capitalize(), "\n"
      "Course:",course, "\n"
      "Semester:",semester, "\n"
      "Admission:",admission, "\n"
      "Address:",address, "\n")

#replace
s1=input("enter a word")
print(s1.replace("o", "e"))

#length
word=input("enter a word")
print(len(word))

#split
s2=input("Enter a word")
print(s2.split("o"))

#while loop
m=int(input("L"))
n=int(input("U"))
step=int(input("step"))
i=m
while i<=n:
 print(i)
 i=i+step

for i in range(5):
 print(i)

#if-else
s3=int(input("Enter a number"))
if s3>99 and s3<1000:
  print("s3 is 3 digit number")
else: 
  print("s3 is not a 3 digit number")

#reverse a list
list1=[]
x=int(input("Enter how many terms you want to enter= "))
while x>0:
  y=int(input("Enter the element= "))
  list1.append(y)
  x=x-1
list1.reverse()
print(list1)

#concate two list
list1=[]
list2=[]
list3=[]
x=int(input("Enter the required number of terms= "))
t=x
while x>0:
  y=str(input("Enter the elements= "))
  z=str(input("Enter the elements= "))
  list1.append(y)
  list2.append(z)
  x=x-1

print(list1) 
print(list2) 

for i in range(0,t):
  list3.append(list1[i]+list2[i])

print(list3)

#square of elements in a list
list1=[]
for i in range(0,11):
  list1.append(i**2)
print(list1)

#remove empty string from list of stirngs
list1=[" ","My"," ","Name"," ","Is","Ashfaq"]
while(" " in list1):
  list1.remove(" ")
print(list1)

#finding a particular item and replacing it with its sqaure
list1=[1,3,10,12,13]
item=int(input("Enter the number to replace "))
try:
  n=list1.index(item)
  print(item,"is",n,"element in the list")
  list1[n]=int(list1[n])*int(list1[n])
  print(list1)
except ValueError:
  print("The item is not in the list")

#remove all occurence of a specific item from the list
list1=[1,3,10,12,10,13]
item=int(input("Enter the number to replace "))
while(10 in list1):
  list1.remove(10)
print(list1)

#create a tuple with different datatype and reverse it
tuple1=(7,'ronaldo',10,'messi')
print("Before reversing",tuple1)
tuple2=tuple1[::-1]
print("After reversing",tuple2)

#count number of occurence of an item from a tuple
t1=(1,2,3,4,1,5,6,1,1,7,8,1)
item=int(input("Enter the term required "))
count=0
for i in t1:
  if i==item:
    count+=1
print(count)

#unpack tuple into several variables
t1=(10,12,14,16,18,20)
for i in range(len(t1)):
  x=t1[i]
  print(x)

#element wise sum of tuple
x=(10,12,3,4)
y=(2,4,6,8)
z=[i+j for i,j in zip(x,y)]
z=tuple(z)
print(x)
print(y)
print(z)

#tuple to dictionary
a=(10,12,14,16)
b=(range(1,len(a)+1))
a=dict(zip(a,b))
print(a)

#remove an item from a set if present
s1=set([10,12,14,16,18])
item=int(input("Enter the item that should be removed "))
print("set before= ",s1)
x=[i for i in s1 if i!=item]
x=set(x)
print("set after= ",x)

#intersection of sets
s1={10,13,15,16,20,18,24,28}
s2={13,15,16,21,23,18,25,27}
s3=(s1.intersection(s2))
print(s3)

#maximum and minimum value in a set
set1={10,15,100,50,2}
print(set1)
print("The maximum value in the set: ",min(set1))
print("The minimum value in the set: ",max(set1))

#to check if two sets have any common elements
set1={1,5,9,20,17,24}
set2={2,7,12,19,25,30}
for i in set1:
  for j in set2:
    if i==j:
      print("There is a common element")
      break;
    else:
      print("There is no common element")
      break;

#sort a dictionary by value
d1=[3,2,6,7,1,9,8,5,4]
print(d1)
sorted_d1=sorted(d1)
print("The sorted value: ",sorted(d1))

#concatinate a dictionary to create new one
d1={7,10,11,9,12,30}
d2={8,13,17,21,19,14}
print("Dictionaries before concatenation:")
print(d1)
print(d2)
d1.update(d2)
print("The concatenated dictionary: ")
print(d1)

#dictionary of squares of the keys
d1=dict()
for i in range(10,21):
  d1[i]=i**2
print("The dictionary of square of the keys is: ")
print(d1)

#remove duplicate from dictionary
d1={"a":5, "s":2, "h":3, "f":4, "a":1, "q":6}
d2=[]
res=dict()
for key, val in d1.items():
  if val not in d2:
    d2.append(val)
    res[val]=key
print(res)

#create a dictionary from string
string=str(input("Enter a string"))
d1=dict()
for i in range(len(string)):
  d1[i]=string[i:i+1]
print(d1)

#square of elements in a list
list1=[i**3 if i%3==0 else i**2 if i%2==0 else i for i in range(0,11)]
print(list1)