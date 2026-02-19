"""
author: 
date: 
0.3 - Repetition Review Exercises
"""

# Task 1: Write a program to calculate the factorial of any number that the user enters
#  using a loop. Ex. 5! = 5*4*3*2*1 = 120
# Your code goes here

num = int(input("Enter number:"))

factorial = 1

for i in range(1, num + 1):

    factorial*= i

print(f"{num} = {factorial}")


# Task 2a: Write a program that asks for five marks and computes the average, 
# rounded to 1 decimal place.
# Your code goes here

count = 0

for i in range(5):

    mark = float(input("Enter mark:"))
    
    count = count + mark
    
average = count / 5

print(round(average , 1))


# 2b)  Modify the program from task 2a to also output the lowest and highest mark WITHOUT lists.
# Your code goes here

total = 0
lowest = 100
highest = 0


for i in range(5):
    mark = float(input("Enter mark:"))
    
    total = total + mark
    
    if mark > highest:
        highest = mark    


    if mark < lowest:
        lowest = mark


average = total / 5

print(round(average , 1))   
print(f"Lowest: {lowest}")
print(f"Highest: {highest}")
#bomboclat
# 2c)  Modify the program from task 2b to check if the mark entered is between 0 and 100. 
# Keep asking user for input until they give a valid grade.
# Your code goes here

count = 0
lowest = 100
highest = 0
total = 0

while count < 5:
    
    mark = float(input("Enter mark:"))
    
    if mark < 0 or mark > 100:
        print("Invalid")
        continue
    count = count + 1

    total = total + mark

    if mark > highest:
        highest = mark    


    if mark < lowest:
        lowest = mark

    
    
average = total / 5

print(round(average , 1))   
print(f"Lowest: {lowest}")
print(f"Highest: {highest}")


# 2d)  Modify the program to ask the user to enter -1 when done entering marks.
# Your code goes here

count = 0
lowest = 100
highest = 0
total = 0
mark = 0



while mark != -1:
    
    mark = float(input("Enter mark(-1 to stop):"))

    if mark < 0 or mark > 100:
        print("Invalid")
        continue
    count = count + 1

    total = total + mark

    if mark > highest:
        highest = mark    


    if mark < lowest:
        lowest = mark

    

    
    
average = total / count

print(round(average , 1))   
print(f"Lowest: {lowest}")
print(f"Highest: {highest}")




# Task 3a) Determine the largest of n positive integers entered the user.
# The program should loop until a negative value is read (aka, use Sentinel Value).
# Your code goes here

highest = 0
integer = 0




while True:
    if integer < 0:
        break
    
    integer = int(input("Enter numbers(this will stop if you put a negative number:)")) 
    
    if integer > highest:
        highest = integer




print(f"The highest is {highest}")


# 3b) Modify the program to find the two largest integers.
# Your code goes here

highest = 0
integer = 0
middle = 0 


while True:
    
    integer = int(input("Enter numbers(this will stop if you put a negative number:)"))
    
    if integer < 0:
        break
    
    if integer > highest:
        highest = integer
        
    elif integer > middle: 
        middle = integer
        


print(f"The highest is {highest}")
print(f"The second highest is {middle}")



# Task 4) Use the random module to choose a number between 1 and 100.
# Then print all the factors of that number.
# Ask the user if they wish to play again – loop until the user enters “No” (sentinel value).
# Your code goes here
import random

play = input("Do you want to take a chance?:").lower

while play != "no":
    
    store = random.randint(1 , 100) 

    for i in range(1,store + 1):

        if store % i == 0:
            
            print(f"The number {i} is a factor of {store}")

    play = input("Do you want to keep playing?:")          



# Task 5) One useful technique when analyzing a number is to use a loop and the modulus
#  operator to extract each digit from the end.
# Consider this code:

num = int(input("Enter a positive integer: "))

while (num >= 1):
    digit = num % 10
    num = num//10
    print(digit)

# Use this above code to do the following:
# Count the number of sevens in a positive integer.

count = 0

num = int(input("Enter a positive integer: "))

while (num >= 1):
    
    

    digit = num % 10
    
    num = num//10

    if digit == 7:
   
        count = count + 1

print(f"There are {count} seven digits in this number")


# Count the number of odd digits, and the number of even digits, in a positive integer.


count_even = 0
count_odd = 0
num = int(input("Enter a positive integer: "))

while (num >= 1):
    
    

    digit = num % 10
    
    num = num//10

    if digit % 2 == 0:
   
        count_even = count_even + 1

    else: 
        count_odd = count_odd + 1

print(f"There are {count_even} even digits and {count_odd} odd digits in this number")

