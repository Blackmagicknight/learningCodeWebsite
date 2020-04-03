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
