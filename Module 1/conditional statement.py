#1. Write a program to check whether a year is a leap year or not. 
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# 2. Write a program to find the largest among three numbers using nested conditional statements. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is", largest)

# 3. Write a program to check whether a character is an uppercase letter, lowercase letter, digit, or special character. 
char = input("Enter a character: ")
if char.isupper():
    print(char, "is an uppercase letter.")
elif char.islower():
    print(char, "is a lowercase letter.")
elif char.isdigit():
    print(char, "is a digit.")
else:
    print(char, "is a special character.")

# 4. Write a program to calculate electricity bill using different unit slabs. 
units = float(input("Enter the number of units consumed: "))
if units <= 100: 
    bill = units * 0.5
elif units <= 200:
    bill = 100 * 0.5 + (units - 100) * 0.75
elif units <= 300:
    bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.20
else:
    bill = 100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50
print("Electricity bill: $", bill)


# 5. Write a program to determine whether a triangle is Equilateral, Isosceles, or Scalene.
side1 = float(input("Enter the length of first side: "))
side2 = float(input("Enter the length of second side: "))
side3 = float(input("Enter the length of third side: "))
if side1 == side2 == side3:
    print("The triangle is Equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")

# 6. Write a program to create a simple calculator using if-elif-else. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"
print("Result:", result)

# 7. Write a program to calculate income tax according to salary ranges. 
salary = float(input("Enter your salary: "))
if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = (salary - 250000) * 0.05
elif salary <= 750000:
    tax = (salary - 500000) * 0.1 + 12500
elif salary <= 1000000:
    tax = (salary - 750000) * 0.15 + 37500
else:
    tax = (salary - 1000000) * 0.2 + 75000
print("Income tax:", tax)


# 8. Write a program to check login authentication using username and password conditions. 

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Login failed. Invalid username or password.")

# 9. Write a program to determine whether a point lies in First quadrant, Second quadrant, Third quadrant, Fourth quadrant, On axis, or At origin. 

x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
if x > 0 and y > 0:
    print("The point lies in the First quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the Second quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the Third quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the Fourth quadrant.")
elif x == 0 and y == 0:
    print("The point is at the origin.")
else:
    print("The point lies on the axis.")


# 10. Write a program to assign grades based on marks and display distinction for high scores. 
marks = float(input("Enter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)

if marks >= 90:
    print("Distinction")
