# System audit
import os
from datetime import date

today = date.today()

name = input("What is your first name? ")
surname = input("What is your last name? ")
ID = input("What is your ID number? ")

directory = today
print(directory)
parent_dir = "/home/sgtuser/homework5"
path = os.path.join(parent_dir, directory)

#def make_directory() :
if not path.exists(today):
    makedirs(today)

filename = ID + ".txt"
#def create_file() :
with open(filename, "a") as f:
    f.write(name + surname + ID)

#def output() :
for file in os.listdir(path):
    with open(path.join(today_date, file), "r") as f:
        print(f.read())


