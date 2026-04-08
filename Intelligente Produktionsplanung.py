# SIMPLE  PRODUCTION  SYS BY ABAMAHDI ADAM 

orders = []

def add_order():
    name = input("Enter order name: ")
    priority = int(input("Enter priority (1 = high, 5 = low): "))

    orders.append((name, priority))
    print("Order added.\n")

def sort_orders():
    # sorting basic level
    for i in range(len(orders)):
        for j in range(i + 1, len(orders)):
            if orders[i][1] > orders[j][1]:
                temp = orders[i]
                orders[i] = orders[j]
                orders[j] = temp

def show_orders():
    if len(orders) == 0:
        print("No orders available.\n")
    else:
        print("\nOrder List:")
        for order in orders:
            print("Order:", order[0], "| Priority:", order[1])
        print()

def worker_view():
    print("\nNext orders for workers:")
    for order in orders:
        print("-", order[0])
    print()

# THE  PROCES
while True:
    print("1. Add order")
    print("2. Show orders")
    print("3. Sort orders")
    print("4. Worker view")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_order()

    elif choice == "2":
        show_orders()

    elif choice == "3":
        sort_orders()
        print("Orders sorted.\n")

    elif choice == "4":
        worker_view()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.\n")