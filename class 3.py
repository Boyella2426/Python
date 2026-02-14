Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # float in string type is converted into int type
... """
... num = "5.5"
... print(int(float(num)))  
... 
... 
... num = "5.8"
... print(float(num))
... num1 = num
... print(int(num1))
... 
... """
... 
... """==============================================================   CONDITIONAL STATEMENTS ================================="""
... 
... #-----------------------------------------check if num is zero
... """
... num = int(input())
... if num == 0:
...     print("num is 0")
... print("Program completed")
... """
... 
... #-----------------------------------------check if num is zero or not
... """
... num = int(input())
... if num == 99:
...     print("num is 99")
... else:
...     print("num is not 99")
... print("Program completed")
... """
... 
... """
... num = int(input())
... if num != 99:
...     print("num is not 99")
... else:
...     print("num is 99")
... print("Program completed")
... """
... 
... #--------------------------------check which number is greater or smaller
... """
... num1 = int(input())
... num2 = int(input())
if num1 < num2:
    print("num1 is lesser")
elif num1 > num2:
    print("num2 is smaller")
print("END")
"""

"""
find weather num is even or odd
find num is divisible with 5 or not
check wether is divisible with both(5 and 3) or not
check num is divisible with any one num of (4 or 6) or not"""

"""=============================================================   PRACTICE   ==========================================================="""
#-----------------------------------find weather num is even or odd
"""
num1 = int(input())
if num1 % 2 == 0:
    print("yes its an even")
else:
    print("its odd")
print("END")
"""

#-----------------------------------find num is divisible with 5 or not
"""
num1 = int(input())
if num1 % 5 == 0:
    print(" divisible by 5")
elif num1 % 5 != 0:
    print("its not divisible by 5")
print("END")
"""

#-----------------------------------find wether is divisible with both(5 and 3) or not
"""
num1 = int(input())
if num1 % 5 == 0:
    print("divisible by 5")
if num1 % 3 ==0:
    print("divisible by 3")
elif num1 % 5 != 0:
    print("its not divisible by 5")
elif num1 % 3 != 0:
    print("its not divisible by 3")
print("END")
"""

#----------------------------------- check num is divisible with any one num of (4 or 6) or not

num1 = int(input())
if num1 % 4 == 0:
    print("divisible by 4")
if num1 % 6 ==0:
    print("divisible by 6")
elif num1 % 4 != 0:
    print("its not divisible by 4")
elif num1 % 6 != 0:
    print("its not divisible by 6")
