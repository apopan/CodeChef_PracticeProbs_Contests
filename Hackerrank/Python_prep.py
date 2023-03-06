# Hello World

if __name__ == '__main__':
    print("Hello, World!")
    
# Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if (n%2==0 and 2<=n<=5):
    print("Not Weird")
elif (n%2==0 and 6<=n<=20):
    print("Weird")
elif (n%2==0 and n>20):
    print("Not Weird")
else:
    print("Weird")

    
 
# Arithmatic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    

# Print Function

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        i=i+1
        print(i, end="")



# Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
    
    
# Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
        
      
# Write a function

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400 == 0:
        leap = True
    elif year%100 == 0:
        leap = False 
    elif year%4 == 0:
        leap = True
         
    return leap

year = int(input())
print(is_leap(year))


# List comprehension

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    matrix = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i+j+k != n]
    print(matrix)


    
# Find runner up score 
    # Method 1 : Finding ascending order of array and getting the second last element
    
 if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = list(set(arr))
    arr2.sort()
    print(arr2[-2])
    
    # Method 2 : Finding and delesting the largest element in the list and printing largest number in new list, which will actually be second largest for the old list
    
    if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = set(arr)
    arr2.remove(max(arr2))
    print(max(arr2))
    
    
# Nested List

student_grades = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grades.append([name, score])
        
graded_list = sorted(list(set([student[1] for student in student_grades])))

second_lowest_grade = graded_list[1]

students_with_second_lowest_grade = [student for student in student_grades
if student[1]==second_lowest_grade
]

students_with_second_lowest_grade.sort()

for student in students_with_second_lowest_grade:
    print(student[0])
