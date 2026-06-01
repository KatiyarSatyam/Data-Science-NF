a = "satyam's house "
b = '"Satyam"'
c = "'Satyam'"
print(a)
print("my name is", b)
print("my name is", c )

val1 = 3
val2 = 5
print(val1+val2)
print(val1-val2)
print(val1*val2)
print(val1//val2)

name = input("enter your name")
age = input("enter your age")
print("HELLO", name, "Your age is", age)

#index and slicing
a = "python"
print(a[1:5])
print(a[-5:-2])
print(a[1:5:1])
print(a[-1:-5:-1])
print(a[0:len(a)])

a = "trainer"
print(a.endswith("er"))
print(a.capitalize())
print(a.replace ("trainer", "python"))
print(a.find("i"))
print(a.count("i"))

a = "python"
print(a[0: ])
print(a[ : ])
print(a[-1:-5])
print(a[-1:-5:-1])

#conditional
n = 8

if True:
  print("True")
else:
  print("small number")
if False:
  print("False")
else:
  print("smll number")
if True:
  print("True")
else:
  print("small number")
if False:
  print("False")
else:
  print("small number")
if True:
  print("True")
else:
  print("small number")

#conditional
n = 0

if n >= 5:
  print("large number")
if n >= 4:
  print("large number")
if n >= 9:
  print("large number")
if n >= 6:
  print("large number")
if n >= 1:
  print("large number")
else:
  print("small number")

#and operator
age  = input("enter your age: ")
salary =input("enter your salary: ")

if age >= "18" and salary <= "25000":
  print("you are eligible")
else:
  print("you are not eligible")

#or operator
marks = input("enter your marks:")
if marks < "40" or marks > "90":
  print("you are an average")

#not operator   not changes true to false and false to true
its_raining = False
if not its_raining:
  print("its raining")
else:
  print("its not raining")

#GRADE SYSTEM
hindi   = int(input("Enter marks for Hindi: "))
english = int(input("Enter marks for English: "))
science = int(input("Enter marks for Science: "))
history = int(input("Enter marks for History: "))
math    = int(input("Enter marks for Math: "))

total_sum = hindi + english + science + history + math
percentage = (total_sum / 500) * 100
average = total_sum/5

print(f"Total Marks: {total_sum}/500")
print(f"Percentage: {percentage}%")
print(f"average: {average}")

if percentage >= 90 or percentage <= 100:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")

#check days
day_num = int(input("Enter a number (1-7): "))

if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Invalid input! Please enter a number between 1-7.")

username = input("Enter your username: ")
email = input("enter your email: ")
password = input("enter your password: ")
if email =="xyz@gmail.com":
    print(f"Welcome {username}")
else:
    print("Incorrect email")

n = 5

if n >2:
 print("larger than 2")
 if n>4:
  print("larger than 4")
  if n>6:
    print("larger than 6")
  else:
    print("smaller than 6 ")
 else:
    print("smaller than 4")
else:
    print("smaller than 2")

#LIST
mylist = [2,4,6,8,10]
mylist[2]
mylist[0]=5
mylist[-2: 3]

#LIST methods
list1 =[1,2,3,4,5]
list1.append(6)
print(list1)

list1.extend([7,8])
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.insert(2,18)
print(list1)

list1.remove(2)
print(list1)

list1.reverse()
print(list1)

list1.pop(6)
print(list1)

mylist=[2,4,6,8,10]
total = sum(mylist)
print("sum of list: ", total)

list1 = [2,16,8,20,1,2]
list1.sort()
print(list1)
list1[-2]
print("2nd least largest number is:", list1[-2])

list1 = [2,4,6,8]
list2 = [2,4,6,8,10]

mid = len(list2)//2
first =list2[:mid]
second =list2[mid:]
print(first)
print(second)

name1 = input("enter 1st student name: ")
name2 = input("enter 2nd student name: ")
name3 = input("enter 3rd student name: ")
student_name=[]
student_name.append(name1)
student_name.append(name2)
student_name.append(name3)
print(student_name)

list1 = [1,2,3,4]
if list1 == list1[::-1]:
 print("palondrom")
else:
  print("not palondrom ")

"""list1 = [ 1,2,3,2,1]
list2 = list1.copy()
list2.reverse()
if list1 == list2:
  print('pallandrom')
else:
  print("not pallondrom")
"""

marks = [ 10,12,14,16,8]
newmarks = a*a for a in marks
print(newmarks)

num = 1,2,3,4
a,*b,d = num
print(a)
print(b)
print(d)

a = 5
b = 6
a,b = b,a
print(a)
print(b)

#tuple methods
tup = (1,2,3,4)
index = tup.index(4)
count = tup.count(1)
print(index)
print(count)

#dictionary and set
myinfo ={
    "name": ["satyam", "rahul"],
    'age': 22,
    "cgpa": 8.5,
    "status": True,
    "empty":[]
    }

print(myinfo)

myinfo = {
    "name":"a",
    "name":"b",
    "name":"c",
    "name":"d",
    }
print(myinfo)

#dictionary and set
myinfo ={
    "name": "satyam",
    'age': 22,
    "cgpa": 8.5,
    "status": True,

    }

print(myinfo.get(2))

#nested dictionary

student={
    "name":"divya",
    "marks":{
        "phy":98,
        "chem":90,
        "math":90}
        }
        "roll no":5,
        {tudents:8
        }}

#dictonary methods
myDict ={
    "name":"a",
    "name":"b",
    "name":"c",
    "name":"d",
         }
myDict.keys()
myDict.values()
myDict.items()
myDict.get("key")
newDict =myDict.update(newDict)

myDict ={
    "name": "satyam",
    'age': 22,
    "cgpa": 8.5,
    "status": True,
         }
keys = myDict.keys()
values = myDict.values()
items = myDict.items()
name = myDict.get("name")
age = myDict.get("age")
newName = myDict.update({"name":"farman"})
print(name)
print(age)
print(keys)
print(values)
print(items)
print(newName)

#set

num={1,2,3,4}
set2={1,2,2,1}
print(num)
print(set2)

#set methods

set.add()
set.remove()
set.clear()
set.pop()
set.union(set2)
set.intersection(set2)
set.difference(set2)

num={1,2,3,4}
num.add(5)
print(num)

num.pop()
print(num)

num.clear()
print(num)

a = {1,2,3,4,5}
b = {3,4,7,9,10}
u = b.union(a)
i = a.intersection(b)
d = a.difference(b)
rd = b.difference(a)
print(u)
print(i)
print(d)
print(rd)

a = {2,3,4,5}
b = {2,3,4}
c = {2,3}
ab = a-b-c
print(ab)

list1 = [2,4,6,8]
list2 = list1.copy()
list3 = list2.copy()
print(list2)
print(list3)

"""#Importing file

"""

#File Handling

from google.colab import files
upload = files.upload()

"""#Read File

"""

f = open("demo13356.txt", 'r')
data = f.read()
print(data)
print(type(data))
f.close()

"""Read upto 5 chracter

"""

f = open("demo13356.txt", 'r')
data = f.read(5)
print(data)
f.close()

"""Reading Line

"""

f = open("demo13356.txt", 'r')
l1 = f.readline()
l2 = f.readline()
print(l1)
print(l2)
f.close()

#Readline with strip
f = open("demo13356.txt", 'r')
l1 = f.readline().strip()
l2 = f.readline().strip()
print(l1)
print(l2)
f.close()

"""Write New Data

"""

f = open("demo13356.txt", 'w')
f.write("Team Present totally")
f.write("\n ai is good.")
f.close()

"""Create a new file

"""

f = open("dbz1.txt", 'w')
f.write("\n kamehameha.")
f.write("\n spirit bomb.")
print(f.read)
f.close()

"""Append"""

f = open("dbz1.txt", 'a')
f.write("\n Kakarot is monkey")
f.write("\n Monkey is kakarot")
f.close()
print(f.read)
f.close()

"""#open a file , read and write in it with "w"
"""

f = open("dbz1.txt", 'w')
f.write("\n Kakarot is monkey")
f.write("\n Monkey is kakarot")
f.close()
print(f.read)
f.close()

"""#open a file , read and write in it with "rt"
"""

f = open("dbz1.txt", 'r+')
f.write("\n Kakarot is monkey")
f.write("\n Monkey is kakarot")
f.close()
print(f.read)
f.close()

f = open("dbz.txt", 'r')
with open("dbz.txt",'r') as f:
 data = f.read()

