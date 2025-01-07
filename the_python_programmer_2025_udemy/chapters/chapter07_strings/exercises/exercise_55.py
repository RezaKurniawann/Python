# Exercise 55 - Total Sales for Specific Products

# You are given a list of strings, each representing information about daily sales transactions.
# Each line contains a date, product name, and sales amount, separated by commas.
# Write a function that takes this list of sales transactions and returns the total sales for each product.

# For example:
# sales = [
#     "2021-01-01,apple,100",
#     "2021-01-01,orange,200",
#     "2021-01-02,apple,150",
#     "2021-01-02,orange,250",
#   ]
# The function should return: [("apple", 250), ("orange", 450)]

def calculate_product_sales(sales: list[str]) -> list[tuple[str, int]]:
    # Dictionary to store total sales for each product
    product_sales = {}
    
    for transaction in sales:
        # Split the transaction string into components
        date, product, amount = transaction.split(',')
        
        # Convert the sales amount to an integer
        amount = int(amount)
        
        # Update the total sales for the product
        if product in product_sales:
            product_sales[product] += amount
        else:
            product_sales[product] = amount
    
    # Convert the dictionary to a list of tuples
    return list(product_sales.items())
