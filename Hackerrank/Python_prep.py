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
