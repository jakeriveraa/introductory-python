

print("hello world from python")
print(2)
print(5+3)
print(True)

name = "jake"
age = 27
last_name = "rivera"
found = False

print(name)
print(last_name)

#concatenation
#casting -> convert a data type to another one (e.g. string (str) -> numbers (int)
# or numbers (int) -> string (str))
print("my name is:" + name + "and im " + str(age) + " years old" )
print("did he show up to the class?" + str(found))
#the f format
#f"" or f"""""""
print(f"my name is: {name}, and im {age} years old")
print(f"""
my name is {name}
    and this is an example 
    of a triple double quoted f format
""")

print(type(name))
print(type(found))
print(type(age))


new_age = int(input("enter a new age:"))
print(new_age + age)

x = int("enter a first value:")
y = int("enter a second value")
print(x+y)