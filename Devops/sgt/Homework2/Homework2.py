#Task1
def my_function (*numbers):
    return max(numbers)
print(my_function(14, 7, 3))

#Task2
word = input("Please input a word:")
for x in range(len(word) -1, -1, -1):
    print(word[x], end="")
#end means that all letters will be in one line and not below each other
print("\n")

print(x)

#Task3

def sum_numbers(*numbers: float) ->float:
    """"Sums all the numbers in the list"""
    return sum(numbers)
print(sum_numbers(1.1, 2.2, 5.5))

#word = input("Please input a word:")
#for x in range(len(word) -1, -1, -1):
    #print(word[x], end="")
    #end means that all letters will be in one line and not below each other
#print("\n")
#print empty line

#print(x)




