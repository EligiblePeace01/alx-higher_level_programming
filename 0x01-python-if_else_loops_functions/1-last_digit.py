#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Deal with negative number (because of negative modulo error issues)
if (number < 0):
    # convert negative number to positive, then find modulo
    l_digit = (-1 * number) % 10
    l_digit *= -1  # convert back to negative remainder

else:
    l_digit = number % 10  # for positive numbers

if (l_digit > 5):
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
elif (l_digit == 0):
    print(f"Last digit of {number} is {l_digit} and is 0")
if (l_digit < 6 and l_digit != 0):
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
