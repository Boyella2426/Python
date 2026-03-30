'''=============================================================== SLICING  ==============================================================='''

s = "codegnan"
print("1", s [5:0:-1])    #finite slice
print("2", s [5:8:-1])
print("3", s [5:100:-1])  #infinite slice
print("4", s [ : :-1])
print("4", s [0:5: ])
print("5", s [: :2])
print("6", s [-2:5:1])    #convert to step type
print("7", s [6:5:1])

'''==================================================================== string ==================================================================='''

###  STRING OPERATIONS:
# string concatenation ( + )
# string repetation ( * )

#concatenation
s1 = "code" 
s2 = "gnan"
print(s1+s2)

#concatenation
s1 = "code" 
s2 = "gnan" #space
print(s1+" "+ s2)
print(s1 + s1)
print(s1 * 5)
print((s1 +" ")  * 5)
print((s1 +" ") ,(s2 +" ")  * 5)
print((s1 +" ") * 5 ,(s2 +" ")  * 5)


### Attendence Management
n = 9
absent = present = 0
for i in range(1,n+1):
    val = int(input(f"enter Roll no:{i} absent:"))
'''================================================================== FUNCTIONS ==========================================================================='''

### FUNCTIONS:

def eve_or_odd(x):
    if x%2==0:
        return 'even'
    else:
        return 'odd'
n=int(input())
res=eve_or_odd(n)
print(res)
print(eve_or_odd(n))


def eve_or_odd(x):
    if x%2==0:
        print ('even')
    else:
        print ('odd')
n=int(input())
res=eve_or_odd(n)
print(res)
print(eve_or_odd(n))

'''--------------------------------------------------------------------------------------------------------------------------'''

def sum_of_ele(list):
    temp = 0
    for i in range(len(list)):
        temp += list[i]
    return temp
list=[1,2,3,4,5]
print(sum_of_ele(list))

'''------------------------------------------------------------------------------------------------------------------------------'''

def add(x,y):
    return x+y
b1=int(input())
b2=int(input())
print(add(b1,b2))

'''-----------------------------------------------------------------------------------------------------------------------------------'''

def sum_of_twonumbers(x):
    temp = 0 
    for num in a:
        temp += 

'''------------------------------------------------------------------------------------------------------------------------------------'''

def sub(x,y):
    return x-y
b1=int(input())
b2=int(input())
print(sub(b1,b2))  #positional arguments
print(sub(b2,b1))  #position based operation 

'''----------------------------------------------------------------------------------------------------------------------------------------'''

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

sel = int(input("Select operation (1-4): "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if sel == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif sel == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif sel == 3:
    print(n1, "*", n2, "=", mul(n1, n2))
elif sel == 4:
    print(n1, "/", n2, "=", div(n1, n2))
else:
    print("Invalid input")