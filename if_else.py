#if else statement
#execute some logic or int=structions if (and only if) the conditon is met
#we can catch on else in case that the condition doesnt match  
# equals: a == b
# not equals: a != b
#less that a < b
#greater than: a > b 
#less than or equal: a <= b
# greater than or equal: a <= b
age = 100

if age < 100:
    if age < 23:
        print("you're a minor without access!")
    else:
        print("you're young")
elif age == 100:
    print("congrtulations, you got to live a century!")
else:
    print("sorry, youre getting old")

# exercise

x = 8
y = 8
if x > y:
    print("Hello")
else:
    print("welcome")    

x = "Hello"
y = "hello"
if x == y:
    print("its the same word")
else:
    print("they're different")
