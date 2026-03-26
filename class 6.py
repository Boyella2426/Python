#print 100 to 120 numbers :

for i in range(100, 121):
    print(i)  # here number will print line by line 

#print 100 to 120 numbers :
for i in range(100, 121):
    print(i, end=" ")   # here numbers will print side by side()


#find sum of even numbers b\w the range of n and m

n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))

total = 0

for i in range(n, m + 1):
    if i % 2 == 0:
        total += i

print("Total:", total)

"""
"""================================================================= PRACTISE =======================================================

# find the length of number:

num = int(input("Enter a number: "))

if num == 0:
    count = 1
else:
    count = 0
    while num != 0:
        num //= 10
        count += 1

print("Length:", count)


# sum of digits in a number using  a loop

num = int(input("Enter a number: "))
total = 0

while num != 0:
    digit = num % 10
    total += digit
    num = num // 10

print("Sum of digits:", total)

# sum of digits in a number using  a loop
                      # handle negative numbers:

num = int(input("Enter a number: "))
num = abs(num)   # convert to positive

total = 0
while num != 0:
    total += num % 10
    num //= 10

print("Sum of digits:", total)


# reverse of a number

num = int(input("Enter a number: "))
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reverse:", reverse)

# check whether thr number is palindrome or not
                       # using reverse logic

num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp != 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if reverse == num:
    print("Palindrome number")
else:
    print("Not a palindrome number")


# check whether thenumber is arm strong or not

num = int(input("Enter a number: "))
temp = num
order = len(str(num))
total = 0

while temp != 0:
    digit = temp % 10
    total += digit ** order
    temp //= 10

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
