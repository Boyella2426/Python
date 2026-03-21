"""========================================= Find the number IS +ve, -ve EVEN AND +ve -ve ODD ===================================
"""
num1,num2,num3=map(int,input().split())
if (num1<num2<num3):
   print("num1 is smaller")
elif (num1>num2<num3):
   print("num2 is smaller")
elif(num1>num2>num3):
   print("num3 is smaller")
else:
   print("all are equal")
"""


"""
if num1>num2 and num1>num3:
    print("num1 is bigger")
elif num2>num3:
    print("num2 is bigger")
else:
    print("num3 is bigger")

"""


"""=========================================================  FIND A NUM IS +EV,-EV OR +ODD,-ODD   ======================================="""
"""
a = int(input())
if (a < 0) and a % 2 != 0:
    print("Negitive odd number ")
elif (a > 0) and a % 2 != 0:
    print("Positive odd number")
elif (a >= 0) and a % 2 == 0:
    print("Positive even number")
elif (a < 0) and a % 2 == 0:
    print("Negative even number")
else:
    print("print a valid number")
"""

"""=========================================================   WHICH OF 3 NUMS IS SAMLLER   ======================================="""

"""
num1=int(input())
num2=int(input())
num3=int(input())

if (num1<num2<num3):
    print("num1 is smaller")
elif (num1>num2<num3):
    print("num2 is smaller")
elif (num1>num2>num3):
    print("num3 is smaller")
else:
    print("all r equal")
"""

"""=================================================   WHICH OF 3 NUMS ID SAMLLER USING (MAP,SPLIT()  ==============================================="""
"""
num1,num2,num3 = map(int, input().split())

if (num1<num2<num3):
    print("num1 is smaller")
elif (num1>num2<num3):
    print("num2 is smaller")
elif (num1>num2>num3):
    print("num3 is smaller")
else:
    print("all r equal") #--------------------- not working , it no giving error but giving wrong print statement  
"""

"""=======================================  print which num is smaller among 3 numbers using (map, split())   ========================================"""
"""
num1,num2,num3 = map(int, input().split())

if (num1<num2) and (num1<num3):
    print("num1 is smaller")
elif (num1>num2) and(num2<num3):
    print("num2 is smaller")
elif (num1>num3) and(num2>num3):
    print("num3 is smaller")
else:
    print("all r equal")
"""

"""=======================================  print which num is smaller among 3 numbers using nested if   ========================================"""
"""
n = int(input())
if n>=0:
    if n % 2 == 0:
        print("postive even number")
    else :
        print("positive odd number")
else:
    if n % 2 !=0 :
        print("negative odd number")
    else :
        print("negative even number")
"""

"""----------------------------------  print which num is smaller among 3 EVEN 2 NUMBERS ARE EQUAL numbers using nested if   ------------------------------

num1,num2,num3 = map(int, input().split())

if (num1<=num2) and (num1<=num3):
    print("num1 is smaller")
    if (num1>=num2) and(num2<=num3):
        print("num2 is smaller")
elif (num1>=num3) and(num2>=num3):
    print("num3 is smaller")
else:
    print("all r equal")
"""


"""------------------------------------------  print which num is bigger among 3 numbers using if,elif even num are    ----------------------------------------------
n1,n2,n3 = map(int,input().split())
if n1 >= n2 and n1>= n3:
    print("n1 is big")
elif n2>= n3:
    print("n2 is big")
else:
    print("n3 is big")


"""






















    

