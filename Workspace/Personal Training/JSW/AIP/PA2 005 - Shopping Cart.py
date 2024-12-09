# main.py
# from cart import *

# def main():
#     shopping_cart = []
#     action = ""

#     while action != "QUIT":
#         action = input().upper()
#         if action == "ADD":
#             item_name, price, quantity = input().split()
#             price = float(price)
#             quantity = int(quantity)
#             add_item(shopping_cart, item_name, price, quantity)
#         elif action == "VIEW":
#             view_cart(shopping_cart)
#         elif action == "UPDATE":
#             item_name, price, quantity = input().split()
#             price = float(price)
#             quantity = int(quantity)
#             update_item(shopping_cart, item_name, price, quantity)
#         elif action == "REMOVE":
#             item_name = input()
#             remove_item(shopping_cart, item_name)
#         elif action == "TOTAL":
#             cost_total = calc_total(shopping_cart)
#             print(f"Total cost of items in cart: ${cost_total:.2f}")
            
#     print("Bye!")

# if __name__ == "__main__":
#     main()



def add_item(cart, item_name, price, quantity):
    cart.append((item_name, price, quantity))
    print(f"{item_name} added with {quantity} units at ${price}.")
    return cart
    
    
def remove_item(cart, item_name):
    for i, element in enumerate(cart):
        name, price, quantity = element
        if name == item_name:
            del cart[i]
            break
    print(f"{item_name} removed from the cart.")
    
def update_item(cart, item_name, price, quantity):
    
    print(f"{item_name} updated to {quantity} units at ${price}.")
    
def view_cart(cart):
    print("Items in your cart:")
    for item_name, price, quantity in cart:
        print(f"- {item_name}: {quantity} units at ${price}")
    
def calc_total(cart):
    result = 0
    for _, price, quantity in cart:
        result += price * quantity
    return result