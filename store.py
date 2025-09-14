from catalog import catalog


def print_header(text):
    print("-------------------")
    print(text)
    print("-------------------")



def print_menu():
    print("choose an option")
    print("1.- view catalog")
    # more options here
    print("")
    print("2.- search product")
    print("")
    print("P.- Quit")


def print_catalog():
    print_header("- Our catalog -")
    for prod in catalog:
        #print(str(prod["id"]) + " " + prod["title"] + " $" + str(prod["price"]))
        print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]} |")
    answer = input("type id to add (N to close): ")
    if answer == "n" or answer == "N":
        return # finis the fn
    else:
        add_product_to_cart(answer)



def add_product_to_cart(prod_id):

    found = False
    for prod in catalog:
        if str(prod["id"]) == prod_id:
            found = True
            print("found")

    if not found:
        print("**Error: Invalid ID")

def search_product():
    text = input("search text:")
    print(text)

### initialize
print_header("welcome to store xy")
print_menu()

option=input("choose an option")
#print("user selected " + option)

if option == "1":
    print_catalog()

elif option == "2":
  search_product()
elif option == "q" or option == "Q":
    print("goobye leave service!")
else:
    print("** Error: invalid option")