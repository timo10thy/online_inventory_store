store = { 
        "laptop":{"price":1200, "quantity":5},
        "headphone":{"price":150, "quantity":10},
        "mouse":{"price":40, "quantity":20}
        }
def user_choice(user_options):
    if user_options == 1:
        name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        msg = add_product(store, name, price, quantity)
        print(msg)
        print('checking for my product',store)
    elif user_options ==2:
        name = input("Product name: ")
        quantity =  int(input("Quantity: "))
        msg = update_stock(store, name, quantity)
        print(msg)
    elif user_options == 3:
        name = input("product name: ")
        quantity = int(input("Quantity: "))
        msg = sell_product(store, name, quantity)
        print(msg)
        print('checking for my product',store)
    elif user_options == 4:
        total = display_inventory(store)
        print(f"Displayed {total} products.")
    elif user_options == 5:
        msg = most_expensive_product(store)
        print(msg)
    elif user_options == 6:
        msg = total_potential_sales(store)
        print(msg)
    elif user_options == 7:
        exit_program()
    else:
        print("\n Invalid option, please choose between 1–7.\n")




def add_product(store_dict, name, price, quantity):
    if name in store_dict:
        
        return "Product exist"
        #store_dict[name]["quantity"] += quantity
        #store_dict[name]["price"] = price
        return f"Updated {name} already in store:"
    else:
        store_dict[name] = {"price": price, "quantity": quantity}
        return f"Added {name}: {store_dict[name]}"
def update_stock(store_dict, name, quantity):
    if name in store_dict:
        store_dict[name]["quantity"] += quantity
        return f"product:{name} is updated"
    else:
        return f"{name} does not exist in the store!"
def sell_product(store_dict, name, quantity):
    if name not in store_dict:
        return "Opps: product does not exit"
    stock_valuation = store_dict[name]["quantity"]
    price = store_dict[name]["price"]
    if quantity > stock_valuation:
        return f"Opps: NOt available {stock_valuation} {name} available"
    store_dict[name]["quantity"] -=quantity
    total_price = price * quantity
    return f"Sold {quantity} {name}(s) for ${total_price}. Remaining stock: {store_dict[name]['quantity']}"

def display_inventory(store_dict):
    if not store_dict:  # check if empty
        print("Inventory is empty.")
        return 0

    count = 0
    print("\n--- Store Inventory ---")
    for name, details in store_dict.items():
        price = details["price"]
        quantity = details["quantity"]
        print(f"{name} -> Price: ${price}, Quantity: {quantity}")
        count += 1

    print(f"Total products: {count}")
    return count

def most_expensive_product(store_dict):
    if not store_dict:  # check if empty
        return "Inventory is empty."

    max_price = 0
    expensive_product = ""

    for name, details in store_dict.items():
        if details["price"] > max_price:
            max_price = details["price"]
            expensive_product = name

    return f"Most expensive product is '{expensive_product}' with price ${max_price}"
def total_potential_sales(store_dict):
    total = 0
    for name, details in store_dict.items():
        total += details["price"] * details["quantity"]

    return f"Total potential sales value is ${total}"
def exit_program():
    print("Exiting the store program. Goodbye!")
    exit()

print("update")
def start():
    while True:
        print('''
            1. Add product
	    2. Update stock
	    3. Sell product
	    4. Display inventory
	    5. most expensive product
	    6. total potential sales
	    7. exit


        ''')
        user_options = int(input("use choice\n>>"))
        user_choice(user_options)


start()

