import pandas as pd
print("Welcome Sir!!")

# Creating all the dictionaries for the Menu Card
hot_cool = {
    "Tea": 10,
    "Coffee": 20,
    "Cold Drink-200ml": 40,
    "Cold Drink-600ml": 60,
    "Lassi": 30,
    "M.Water": 20
}
hot_cool1 = {
    "Iteam": list(hot_cool.keys()),
    "Price": list(hot_cool.values())
}

cambo = {
    "Aloo Paratha": 30,
    "Pyaz Paratha": 30,
    "Ghobi Paratha": 35,
    "paneer Paratha": 50,
    "Rajma Rice": 75,
    "Dal Rice": 60
}
cambo1 = {
    "iteam": list(cambo.keys()),
    "price": list(cambo.values())
}

rice = {
    "Plain Rice": 40,
    "Jeera Rice": 60,
    "Veg Briyani": 80,
    "Briyani": 120
}
rice1 = {
    "Iteam": list(rice.keys()),
    "Price": list(rice.values())
}

dals = {
    "Dal Fry": 40,
    "Dal Fry Butter": 60,
    "Dal Makhani": 60,
    "Rajma": 55
}
dals1 = {
    "Iteam": list(dals.keys()),
    "Price": list(dals.values())
}

jawa = {
    "Roti": 7,
    "Roti Butter": 15,
    "Lacha Paratha": 20,
    "Naan": 20,
    "Tawa Roti": 5
}
jawa1 = {
    "Iteam": list(jawa.keys()),
    "Price": list(jawa.values())
}

# Creating a dict for all items
all_iteam = {**hot_cool, **cambo, **rice, **dals, **jawa}

# Function to show the menu to the customer
def show_menu():
    print("Please Select your choice:")
    print("1. Hot & Cool \n2. Cambo \n3. Rice\n4. Dals \n5. Jawa & Jandoor\n")
    print("Enter your choice:")
    n = int(input())
    
    match n:
        case 1:
            df = pd.DataFrame(hot_cool1)
            print(df.to_string(index=False))

        case 2:
            df = pd.DataFrame(cambo1)
            print(df.to_string(index=False))

        case 3:
            df = pd.DataFrame(rice1)
            print(df.to_string(index=False))

        case 4:
            df = pd.DataFrame(dals1)
            print(df.to_string(index=False))

        case 5:
            df = pd.DataFrame(jawa1)
            print(df.to_string(index=False))

        case _:
            print("Please enter a correct choice")

order_list = []
price = []

# Function to take order from the customer
def take_order():
    iteam = input("Enter your order: ").strip()
    if iteam in all_iteam:
        try:
            qty = int(input(f"How many {iteam}s? "))
            order_list.append(f"{iteam} x{qty}")
            price.append(all_iteam[iteam] * qty)
            print(f"Added {qty} {iteam}(s) - Rs. {all_iteam[iteam] * qty}")
        except ValueError:
            print("Invalid quantity! Please enter a number.")
    else:
        print("Please check the spelling, Sir!!")
    
# Function to delete an order
def delete_order():
    iteam = input("Enter your order to remove: ")
    if iteam in order_list:
        index = order_list.index(iteam)
        removed_price = price.pop(index)
        order_list.remove(iteam)
        print(f"Removed {iteam} - Rs. {removed_price}")
    else:
        print("Item not found in your order list, please check the spelling.")

# Function to show the ordered items
def show():
    if not order_list:
        print("No items ordered yet.")
        return
    
    total = sum(price)
    dic1 = {
        "Iteam": order_list,
        "Price": price
    }
    df = pd.DataFrame(dic1)
    print(df.to_string(index=False))
    print(f"The total amount is Rs. {total}")

# Main loop
while True:
    print("\n1. Show Menu\n2. Take Order\n3. Delete Order\n4. Create Bill\n5. Exit")
    print("Enter your Choice:")
    num = int(input())
    
    match num:
        case 1:
            show_menu()

        case 2:
            take_order()

        case 3:
            delete_order()

        case 4:
            show()

        case 5:
            print("Thank you for visiting! Have a great day!")
            break

        case _:
            print("Please Enter a valid Choice")
