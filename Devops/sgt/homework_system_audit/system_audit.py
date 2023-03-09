# System audit
import os
import os
from datetime import date

today = date.today()

name = input("What is your first name? ")
surname = input("What is your last name? ")
ID = input("What is your ID number? ")

directory = today
parent_dir = "/home/sgtuser/Documents/Devops/sgt/homework_system_audit"
path = os.path.join(parent_dir, str(directory))

if not os.path.exists(path):
    os.makedirs(path)

filename = os.path.join(path,ID + ".txt")
with open(filename, "a") as f:
    f.write(name + surname + ID)

print("Files in directory: ", os.listdir(path))




