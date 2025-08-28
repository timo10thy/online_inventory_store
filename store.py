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
        print('checking for my product',store)
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
       return "product does not exit"
       current_stock = store_dict[name][quantity]
       price = store_dict[name]["price"]
       if quantity > current_stock:
            return f "error: NOt available
        store_dict[name]["quantity"] -=quantity
        return f"product:{name} is updated"
        print("checking if name exit",name)
print("update")
def start():
    while True:
        print('''
            1. Add product
	    2. Update stock
	    3. Sell product
        ''')
        user_options = int(input("use choice\n>>"))
        user_choice(user_options)


start()

