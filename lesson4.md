```py
number1 = 5
number2 = 6
total = number1 + number2 
print(total) # Print 11  // # to run mathematical operations in VSCode, variables need to be created
# number1 + number2 -- Does not work in non-IDLE environments

# Other Mathetical Operators
# Multiplication
number1 = 2
number2 = 3
total = number1 * number2
print(total) # Print 6

# Division
number1 = 10
number2 = 5
total = number2 / number1
print(total) # When a variable is set to the result of a division operation, the value of the variable becomes a float // Prints 0.5
total = number1 / number2
print(total) # prints 2

# Subtraction
number1 = 11
number2 = 5
total = number1 - number2
print(total) # Prints 6

# RPG
import time 
import sys 

# print("Only do lowercase answers and for yes/no questions, write "y" or "n")

print("A very tall man is knocking at your door. ")

time.sleep(2)

wizardName = input("Choose his name: ")
time.sleep(0.75)
print(wizardName + " is knocking at your door.")

openDoor1 = input("Do you want to open the door? ")

if openDoor1 == "y":
    print(wizardName + " is friendly")
if openDoor1 == "n":
    print("He kills you lol")    # could also use else
    exit()

print(wizardName + " sits down on your best couch")

"""
if openDoor1 == "n":
    print("He still kills you lol")    
    """
    ```
