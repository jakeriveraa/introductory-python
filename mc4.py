product_cart = [100, 200, 300, 400, 500]

# Function to calculate total
def calculate_total(cart):
    total = 0
    for value in product_cart:
        total += value
    return total

# Function to calculate average
def calculate_average(total, length):
    return total / length

# Calculate total and average
total = calculate_total(product_cart)
avg = calculate_average(total, len(product_cart))

print(f"The total is {total} and the average is: {avg}")