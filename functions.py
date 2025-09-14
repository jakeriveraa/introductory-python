# simple function 
def my_function():
    print("this is my function")

def other_function():
    print("this is another function")


my_function() # calling the function
other_function()

print("---------------")

# function with parameters
def print_full_name(fname, last_name):
    print("this name is: {fname} {last_name}")

# function that return something
def get_full_name(fname, last_name):
    return f"{fname} {last_name}"

#store the returned value in a variable
full_name = get_full_name("justin", "case")
print(full_name)

def subtract(x, y):
    return x-y

res = subtract(1, 3)
print(res)