x = int(input("enter the first number"))
y = int(input("enter the second number"))

if x == y:
    print("theyre the same")
else:
    print("they are different")

    #short hand if-else (ternary operators or conditional expressions)
    print("they're the same") if x == y else print("they're different")