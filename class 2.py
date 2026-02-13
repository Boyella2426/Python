Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
"""num = input()
print(type(num))
print(num)"""

"""------------------------------------implicit type convertion"""

          
"""num1 = int(input())
val = float(input())
print(type(num1),type(val))
res = num1+val
print(res)"""

"""num1 = input()
print(type(num1))
res = num1 + 10
print(res)"""

"""--------------------------------------type error"""
"""--------------------------------------can only concatinate same datatype"""
"""--------------------------------------explicit type convertion"""

"""num1 = input()
print(type(num1))
res = int(num1) + 10
print("res = ",res)"""


"""--------------------------------------coverting int to float,str and bool"""

"""nnum = 12
print(float(num))
print(str(num))
print(bool(num))"""

"""===================================================================================  PRACTICE   ====================================================================================================="""
"""
float----> int str bool
str----> int float bool list tuple set  
list---->tuple set str
tuple----> list set str
set---->list tuple str"""

"""==========================================float----> int str bool=========================================="""
"""num1 = 55.5
print(int(num1))
print(str(num1))
print(bool(num1))"""


"""==========================================str----> int float bool list tuple set=========================================="""
"""num2 = "55"
print(int(num2))
print(float(num2))
print(bool(num2))
print(list(num2))
print(set(num2))
print(tuple(num2))"""
"""------------------------------------this worked when data is in numbers"""
"""num2 = "ram"
print(int(num2))
print(float(num2))
print(bool(num2))
print(list(num2))
print(set(num2))
print(tuple(num2))"""
""""---------------------------------the same throws error bcz the data is in letters, that cant be printed in integer"""


"""==========================================list---->tuple set str=========================================="""
"""num2 = [1,2,58,57,48]
num1 = [1,2,58,57,48,1,2,"hi","it me"]
print(str(num1))
print(set(num1))
print(tuple(num1))
... print(type(str(num1)))
... print(type(set(num1)))
... print(type(tuple(num1)))
... print(str(num2))
... print(set(num2))
... print(tuple(num2))
... print(type(str(num2)))
... print(type(set(num2)))
... print(type(tuple(num2)))"""
... """------------------------------------list can have duplicate , list acceptes int and str values"""
... 
... """==========================================tuple----> list set str=========================================="""
... """
... num1 = (1,2,5,64,5,"hi","me")
... num2 = (1,2,5,64,5,1,2,"hi","me")
... print(str(num1))
... print(set(num1))
... print(tuple(num1))
... print(type(str(num1)))
... print(type(set(num1)))
... print(type(tuple(num1)))
... print(str(num2))
... print(set(num2))
... print(tuple(num2))
... print(type(str(num2)))
... print(type(set(num2)))
... print(type(tuple(num2)))
... """
... """------------------------------------tuple can have duplicate , tuple acceptes int and str values, if any duplicates those values are printed again"""
... 
... """==========================================set---->list tuple str=================================="""
... """num1 = {1,2,5,64,5,"hi","me"}
... num2 = {1,2,5,64,5,1,2,"hi","me"}
... print(str(num1))
... print(list(num1))
... print(tuple(num1))
... print(type(str(num1)))
... print(type(list(num1)))
... print(type(tuple(num1)))
... print(str(num2))
... print(list(num2))
... print(tuple(num2))
... print(type(str(num2)))
... print(type(list(num2)))
... print(type(tuple(num2)))
... """
