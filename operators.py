# arithmetic
# assignment
# comparison
# logical
# identity
# membership

# arithmetic operator - used with numeric values to persorm common math


x = 1
y = 2
res = 0
res = x + y
print(res)

res = x - y
print(res)

res = x / y
print(res)

res = x % y
print(res)

res = x ** y
print(res)

res = x // y
print(res)

print("-----------------")

# assignment operators - used to assign values to variables

x = 5 
x += 5 # x = x + 5
x -= 3 # x = x - 3
x *= 3 # x = x * 3
x /= 3 # x = x / 3

print(x)

print("-----------------")

# comaprison- used to compare two values same as if_else

# logical operators - used to combine conditional operators
x = 3 
y = 2
z = 2

print(x == y and y == z) # both conditions to be true
print(x == y or y == z) # one condition to be true
print(not x == y)
print("----------------")

# identity operators - used to compare the objects, not if they're equal
# but if they're actually the same object with the same memory location

x = 3
y = 3
print(x is y) # true is both variables are the same object
print(x is not y) 
print("----------------")

# membership - used to test if a sequence is in an object

x = [1, 2, 3, 4, 5] # this is a list

print(3 in x)
print(9 not in x)