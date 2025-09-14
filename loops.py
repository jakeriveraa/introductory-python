 # loops: for and while
# is used for interating over a sequnce (or collections like list, tuples,
# dictionaris, set, string)
# keywords -> continue - jumps to the next interations and break - finish the loop
# for: for interating until a condition is met 
# while: iterating until a condition is met

students = ["reggie", "zane", "luis", "carlo", "kevin"]
found = False
iteration = 0
while not found: # True -> False
    print(iteration)
    if students[iteration] == "kevin": # students[0] == "reggie" -> True
        found = True
        print(f"hey {students[iteration]} is here")
    else:
        iteration+=1

fruits_list = ["apple", "banana","cherry","orange","banana"]

for fruit in fruits_list:
    if fruit == "banana":
        break
    else:
        print(fruit)

#range function - allows us to iterate through a start, stop and step values
# start it's INCLUSIVE
# stop it's EXCLUSIVE
# step are the increments (e.g. by 1, 2, 3 ... n)

for x in range(10): # using range with the stop parameter only
    print(x)
for x in range(5,10,1):
    print(x)

for x in range(0,len(fruits_list),1):
    print(fruits_list[x])

name = "reggie"

for x in name:
    print(x)