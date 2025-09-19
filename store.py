from catalog import catalog

cart = []

def print_header(text):
    print("\n\n\n")
    print("-------------------")
    print(text)
    print("-------------------")



def print_menu():
    print("choose an option")
    print("1.- view catalog")
    print("2.- search product")
    print("3.- view cart")
    print("4.- checkout")
    print("5.- clear cart")
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
            cart.append(prod)
            print(f'{prod["title"]} added to your cart. ')

    if not found:
        print("**Error: Invalid ID")

def search_product():
    text = input("search text:")
    found = False
    for prod in catalog: #checking every product 
        if text in prod["title"]:
            found = True
            print(f'found: ID {prod["id"]} | {prod["title"]} | ${prod["price"]}')
            choice = input("Do you want this item in your cart? y/n: ")
            if choice == "y":
                add_product_to_cart(prod["id"])

    if not found:
        print("Sorry, this item doesnt exist")
    

def view_cart():
    print_header("Your Cart")
    if not cart:
        print("Your cart is empty")
    else:
        #search all products in cart
        #print all products
        total = 0
        for prod in cart:
            print(f'found: ID {prod["id"]} | {prod["title"]} | ${prod["price"]}')
        cart_total()

def cart_total():
    total = 0
    for prod in cart:
        total += prod["price"]
    print(f"Total ${total}")

def checkout():

    if not cart:
        print("your cart is empty")
        return
    print_header("checkout")
    name = input("enter your name: ")
    email = input("enter your email: ")
    phone = input("enter your phone number: ")

    cart_total()
    print("Thank you for your purchase")

def clear_cart():
    cart.clear()
    print("your cart is now empty")

def product():
    try:
        prod_id = int(input("Enter your id: "))
        title = input("enter product title: ")
        price = float(input("enter product price: "))
        new_prod = {"id": prod_id, "title": title, "price": price}
        catalog.append(new_prod)
        print(f'product "{title}"product has been added"')
        
    except ValueError:
        print("ERROR")


### initialize
option = ""
while option != "q" and option != "Q":
    print_header("welcome to store xy")
    print_menu()

    option=input("choose an option")
    #print("user selected " + option)

    if option == "1":
        print_catalog()

    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "4":
        checkout()
    elif option == "5":
        clear_cart()
    elif option == "q" or option == "Q":
        print("goobye leave service!")
    else:
        print("** Error: invalid option")