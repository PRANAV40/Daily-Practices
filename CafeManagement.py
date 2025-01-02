meanu = {
    'Pizza': 49,
    'Pasta':59,
    'Chat':39,
    'Chai': 29,
    'Coffee':89,
    'Burger':59
}

print("Welcome to PM Restro!!!!")
print("Pizza: 49\nPasta: 59\nChat: 39\nChai: 29\nCoffee: 89\nBurger: 59")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in meanu:
    order_total += meanu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!!")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in meanu:
        order_total += meanu[item_2]
        print(f"Item {item_2} has been added to order!!")
    else:
        print("fOrdered item {item_2} is not available yet!!")

print(f"Total amount of items to pay is {order_total} ")