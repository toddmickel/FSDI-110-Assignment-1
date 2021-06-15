# description
"""
Triple double-quotes allow multi-line comments.
PyCalc: Simply calculator
Author: Todd Mickel
Date: 6/14/2021
Functionality:
  - Simple mathematical operations (sum, subtraction, division, multiplication)
"""

# imports
from decimal import *

# global variables


# functions

def print_menu():
    print("")
    print("-----------------------------------")
    print("--       Welcome to PyCalc!      --")
    print("-----------------------------------")
    print("--  1 - Sum                      --")
    print("--  2 - Subtract                 --")
    print("--  3 - Multiplication           --")
    print("--  4 - Division                 --")
    print("--  5 - Modulo                   --")
    print("--  6 - Even or Odd?             --")
    print("--  7 - Print a message N times  --")
    print("--  Q - Quit                     --")
    print("-----------------------------------")
    print("")


def clear():
    print("\n\n\n\n\n")


def print_msg():
    msg = input("What message would you like to print? ")
    num_times = input("How many times would you like to print it? ")

    if (num_times.isnumeric() == False or int(num_times) < 1):
        print(f"\n{num_times} isn't a whole number greater than 0, dummy!")
    elif int(num_times) > 100:
        print(f"\nI think {num_times} is too many times to print any message!")
    else:
        print("")
        num_times = int(num_times)
        for num_times in range(0, num_times, 1):
            print(f"{msg}")


def even_or_odd():
    test_num = input("Enter a whole number you would like to test: ")
    if (test_num.isdigit()) or (test_num.startswith("-") and test_num[1:].isdigit()):
        if int(test_num) % 2 == 0:
            print(f"\n{test_num} is an even number.")
        else:
            print(f"\n{test_num} is an odd number")
    else:
        print(f"\n{test_num} is not a whole number, dummy!")

    # instructions
operation = ""
while operation.upper() != "Q":
    clear()
    print_menu()

    operation = input("Select an option: ")
    if operation.upper() == "Q":
        break

    if operation != "6" and operation != "7":
        first_num = input("First Number: ")
        second_num = input("Second Number: ")

        try:
            first_num = Decimal(first_num)
            second_num = Decimal(second_num)
        except:
            print("\nYou didn't enter two numbers. Try again!!")
            operation = ""

    if operation == "1":
        print(f"\n{first_num} + {second_num} = {first_num + second_num}")

    elif operation == "2":
        print(f"\n{first_num} - {second_num} = {first_num - second_num}")

    elif operation == "3":
        print(f"\n{first_num} * {second_num} = {first_num * second_num}")

    elif operation == "4":
        if second_num == 0:
            print(f"\nYou must not divide by 0 or all-out nuclear war will result!")
        else:
            print(f"\n{first_num} / {second_num} = {first_num / second_num}")

    elif operation == "5":
        if second_num == 0:
            print(f"\nYou must not divide by 0 or all-out nuclear war will result!")
        else:
            print(f"\n{first_num} % {second_num} = {first_num % second_num}")

    elif operation == "6":
        even_or_odd()

    elif operation == "7":
        print_msg()

    else:
        print(f"\n{operation} is not a valid selection")

    input("\nPress Enter to continue")

print("\nSee ya!")
