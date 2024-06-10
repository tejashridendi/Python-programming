# -*- coding: utf-8 -*-
"""Python_Essentials.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PFgVEVuSqgkbq08qyRZ6UG7f_TOTbxBe
"""

print('I\'m Monty Python.')

print("I'm Monty Python.")

print(True > False)
print(True < False)

print("\"I'm\"\n""\"\"learning\"\"\n\"""\"\"Python\"\"\"")

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

print(-6 // 4)
print(6. // -4)

print(14 % 4)

print(12 % 4.5)

print(-4 + 4)
print(-4. + 8)

print(-4 - 4)
print(4. - 8)
print(-1.1)

print(+2)

print(9 % 6 % 2)

print(2 ** 2 ** 3)

print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

print(2 * 3 % 5)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)


var = var + 1
print(var)

"""# Mathematical problems"""

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print("Total number of apples:",total_apples)

peter = 12.5
suzy = 2
print(peter / suzy)
print("Total number of apples:", total_apples)

x=1
x = x * 2
sheep=1
sheep = sheep + 1

x *= 2
sheep += 1

var = 2
var = 3
print(var)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

"""# Operators & Expressions"""

x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

a = '1'
b = "1"
print(a + b)

a = 6
b = 3
a /= 2 * b
print(a)

"""# Comments"""

# This is a test program.
x = 1
y = 2
# y = y + x
print(x + y)

uncomment_me = 1
uncomment_me_too = 3
uncomment_me_also = 5

print(uncomment_me, uncomment_me_too, uncomment_me_also, sep="\n")
a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds)

# This program prints
# an introduction to the screen.
print("Hello!")  # Invoking the print() function
# print("I'm Python.")

# print("String #1")
print("String #2")

"""This is
a multiline
comment. """

print("Hello!")

"""# Interaction with the **user**"""

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

"""# Type casting (type conversions)"""

anything = int(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

2 == 2
1 == 2
#var == 0

var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)

n = int(input("Enter a number: "))
print(n >= 100)

"""# Conditional execution"""

name = input("Enter flower name: ")

if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")

x = 10

if x == 10: # condition
    print("x is equal to 10")  # Executed if the condition is True.

x = 10

if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10: # condition three
     print("x is equal to 10")  # Executed if condition three is True.

x = 10

if x == 10: # True
    print("x == 10")

if x > 15: # False
    print("x > 15")

elif x > 10: # False
    print("x > 10")

elif x > 5: # True
    print("x > 5")

else:
    print("else will not be executed")

x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")

"""# While loop"""

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

"""

```
Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen.
```

"""

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

"""Create a while loop that counts from 0 to 10, and prints odd numbers to the screen."""

x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

""" Create a for loop that counts from 0 to 10, and prints odd numbers to the screen."""

for i in range(0, 11):
    if i % 2 != 0:
        print(i)

"""# Logical & bit operators"""

# Example 1:
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))

i = 1
j = not not i
print(j,end="\n")

i = 15
j = 22
log = i and j
print(log, end="\n")

bit = i & j
print(bit, end="\n")

logneg = not i
print(logneg, end="\n")

bitneg = ~i
print(bitneg, end="\n")

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right, sep=" & ", end="\n ")

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)