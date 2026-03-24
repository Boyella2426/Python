
""" ======================================================== nested if =============================================================================="""

num1,num2,num3= map(int,input().split())
if (num1<num2<num3):
   print("num1 is smaller")
elif (num1>num2<num3):
   print("num2 is smaller")
elif(num1>num2>num3):
   print("num3 is smaller")
else:
   print("all are equal")
   
   


"""============================================================LOOPS============================================================================================
# LOOP : it a is repeatative task,it exceutiveswith different values Until unless it reaches to certain conditions.

 # TYPES OF LOOP:
  #1:FOR LOOP
  #2:WHILE LOOP

"""

"""
num1,num2,num3=map(int,input("enter numbers: ").split())
if num1 % 2==0:
    print(" num1 is even")
elif num2 %2!=0:
    print("num2 is odd")
elif num3 >=0 and num3 %2==0:
     print("num3 is odd")
else:
    print("all are even or all or odd")
"""


"""
lst=[11,12,13,14,15]
for ind in range(0,5,1):
    if lst[ind]% 2 == 0:
         print(lst[ind],"is even ")
    else:
         print(lst[ind],"is odd")

"""


"""
#print even numbers between 20 - 40


for num in range(20,41):
    if num %2==0:
        print(num)

for num in range(20,41,2):
    print(num)

"""


"""
#print 1-100 numbers

for num in range(1,101):
    print(num, end =" " )

"""


 
"""
#find sum of n natural numbers

n=int(input())
total=0
for num in range (1,n+1):
    total = total+num
    print (total)

"""








    
