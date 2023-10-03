#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        """
        prints the numbers from 1 to 100 separated by a space

        prints `Fizz` instead of number for multiples of three
        prints `Buzz` instead of number for multiples of five
        prints `FizzBuzz` instead of number for multiples of three and five
        """
        if (number % 3 == 0) and (number % 5 == 0):
            print("FizzBuzz", end=" ")
        elif (number % 3 == 0):
            print("Fizz", end=" ")
        elif (number % 5 == 0):
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
