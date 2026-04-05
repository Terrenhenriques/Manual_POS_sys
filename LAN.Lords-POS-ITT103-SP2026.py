"""
BEST BUY RETAIL STORE
POINT OF SALE (POS) SYSTEM
"""
# -------------------------------------------------- SECTION 1 ---------------------------------------------------------
# This program starts by defining a function
def manual_entry_pos():
    """
    Inventory in the form of a dictionary,
    to store each item name, each item price,
    and the stock which is the amount of each item.
    """
    inventory = {
                "sardine": {"price": 500, "Stock": 10, "display": "sardine"},
                "tin mackerel": {"price": 200, "Stock": 10, "display": "tin mackerel"},
                "baked beans": {"price": 500, "Stock": 10, "display": "baked beans"},
                "foska oats": {"price": 300, "Stock": 10, "display": "foska oats"},
                "lasco food drink": {"price": 350, "Stock": 10, "display": "lasco food drink"},
                "excelsior crackers": {"price": 600, "Stock": 10, "display": "excelsior crackers"},
                "ketchup": {"price": 500, "Stock": 10, "display": "ketchup"},
                "milo": {"price": 500, "Stock": 10, "display": "milo"},
                "time and patient bread": {"price": 800, "Stock": 10, "display": "time and patient bread"},
                "chiffon butter": {"price": 350, "Stock": 10, "display": "chiffon butter"}
    }
    # Declaration my variables
    cart = []
    sub_total = 0
    tendered = 0
    change = 0
    low_stock = 5
    # This section is just printing a store name in the form of a header at the beginning.
    print("--------------------------------------------")
    print("---:) BEST BUY RETAIL STORE POS SYSTEM (:---")
    print("--------------------------------------------")

# -------------------------------------------------- SECTION 2 ---------------------------------------------------------

    # 2. Main loop starts here. It keeps the system running until it is shutdown.
    while True:
            print(" ")
            # I created this section to give the user simple options to choose which executes whatever operation is associated with it.
            operation = input("Select Operation: [A]dd, [R]emove, [V]iew Cart, [C]ash Out, [P]rint Receipt, [E]xit: ").upper()
            print(" ")

            # --------------------------------------------- SECTION A ----------------------------------------------
            # This section is the 'EXIT' operation. It shuts down the POS system.
            if operation == 'E':
                confirm = input("Continue? (y/n): ").lower()
                if confirm == 'y':      # It utilizes a confirmation logic in the form of an if statement.
                    print("Good Bye!")  # It requires a action from the user for confirmation to terminate.
                    break
                else:
                    print("Exit cancelled.")
                    continue

            # --------------------------------------------- SECTION B ----------------------------------------------
            # This section executes the 'VIEW CART' operation. It allows the user to view there current cart
            elif operation == 'V':
                if not cart: # This checks if the cart is empty first before continuing in loop.
                    print("Your cart is currently empty.")
                else:
                    print(" ")
                    print("---- Current Cart ----")
                    for i, item in enumerate(cart, 1): # This section numbers each item in the cart starting at 1.
                        unit_price = item['total'] / item['qty']
                        print(f"{i}. {item['qty']} {item['name']} @ ${unit_price:.2f} ea")
                        print(f"                 - ${item['total']:.2f}")
                    print(" ")
                    print(f"Subtotal:        - ${sub_total:.2f}")

            # --------------------------------------------- SECTION C ----------------------------------------------
            # This section executes the 'REMOVE' operation. It allows the user to remove items from their cart.
            elif operation == 'R':
                if not cart: # This checks if the cart is empty first before continuing in loop.
                    print("Your cart is empty")
                    continue

                for i, item in enumerate(cart, 1): # This section numbers each item in the cart starting at 1.
                    print(f"{i}. {item['name']} (qty: {item['qty']})")

                try:
                    idx = int(input("Enter item number to remove: ")) - 1
                    if 0 <= idx < len(cart):
                        removed = cart.pop(idx) # 'pop' is used to remove the item from the list
                        item_key = removed['name'].lower()
                        inventory[item_key]['Stock'] += removed['qty'] # This section restores the item to the inventory.
                        sub_total -= removed['total'] # Subtract the removed items cost from the customers subtotal.
                        print(f"Removed {removed['name']}. Stock restored.")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Please enter a valid number.") # This section handles errors where letters are entered instead of numbers.

            # --------------------------------------------- SECTION D ----------------------------------------------
            # This section executes the 'ADD' operation. It allows the user to add items to their cart.
            elif operation == 'A':

                search_name = input("Enter Product Name: ").lower().strip()
                # This section checks if the item entered exists in the inventory dictionary.
                if search_name in inventory:
                    item_data = inventory[search_name]
                    try:
                        # This section asks the user to input the quantity in the form of an integer and stores it.
                        qty = int(input(f"Enter the amount of {item_data['display']}: "))
                        available = item_data['Stock']

                        # This section from the 'if' to the following 'elif'
                        # checks if the quantity entered is more than 0. It deducts from the cart list,
                        # calculate cost, and update the cart list.
                        if qty <= 0:
                            print("There must be at least one item.")
                        elif qty <= available:
                            item_data['Stock'] -= qty
                            item_price = item_data['price'] * qty
                            # THis section store what is inside the cart as a dictionary for the final receipt.
                            cart.append({"name": item_data['display'], "qty": qty, "total": item_price})
                            sub_total += item_price # THis section adds each item price
                            print(f"Added {qty} {item_data['display']}(s).")

                            # Low stock alert code
                            if item_data['Stock'] < low_stock:
                                print("-" * 25)
                                print("!!! Low Stock Alert !!!")
                                print(f"Note: {item_data['Stock']} {item_data['display']}(s) left!")
                                print("-" * 25)
                        else:
                            # This section handles errors from low stock to incorrect input.
                            print(f"Insufficient stock. {available} available.")
                    except ValueError:
                        print("Invalid amount. Enter a valid number.")

            # --------------------------------------------- SECTION E ----------------------------------------------
            # This section executes the 'CASH OUT' operation. It allows the user to close the sale.
            elif operation == 'C':
                if not cart:
                    print("Your cart is empty.")
                    continue
                # THis section calculates the sales tax then adds it to the subtotal.
                sales_tax = sub_total * 0.10
                total_taxed = sales_tax + sub_total
                # This section uses an if statement to check and calculate discounts.
                if total_taxed >= 5000:
                    discount = total_taxed * 0.05

                else:
                    discount = 0.0
                grand_total = total_taxed - discount

                # While any of the discounted conditions are true it goes on to printing a 'CASH OUT' section.
                # This section displays subtotal, sales tax of 10%, total after tax, and discount if any.
                while True:
                    try:
                        print("=" * 30)
                        print(f"{" "}    {'- READY TO CASH OUT -'}")
                        print("=" * 30)
                        print(f"SUB TOTAL:           $ {sub_total:.2f}")
                        print(" ")
                        print(f"{'Sales Tax:':<20} % {'10'}")
                        print(f"{'TOTAL:':<20} $ {total_taxed:>2.2f}")
                        print(f"DISCOUNT:            $ {discount:.2f}")
                        print(" ")
                        print(f"{'TOTAL DUE:':<20} $ {grand_total:>2.2f}")
                        tendered = float(input("Enter amount received: "))
                        # It also allows the cashier to input the amount of money received and uses an if state. to calculates change.
                        if tendered >= grand_total:
                            change = tendered - grand_total
                            print(f"{'Change:':<20} $ {change:.2f}")
                            print("=" * 30)
                            break
                        else:
                            print(f"!!!Insufficient amount tendered!!!")
                    except ValueError: # It also handles errors where insufficient amount is tendered or incorrect input.
                        print("Sorry wrong selection.")

            # --------------------------------------------- SECTION F ----------------------------------------------
            # This section executes the 'PRINT RECEIPT' operation. It allows the user to print the customers receipt.
            elif operation == 'P':
                if not cart:
                    print("Your cart is empty.")
                    continue

                while True:

                    try: # This section organizes and print a receipt based on items in cart.
                        print(" ")
                        print("=" * 33)
                        print("----- BEST BUY RETAIL STORE -----")
                        print(f"{" "}          {"POS SYSTEM"}")
                        print(f"{" "}     {"123 St. James Street"}")
                        print(f"{" "}          {"Montego Bay"}")
                        print(f"{" "}           {"Jamaica"}")
                        print("---------------------------------")
                        from datetime import datetime
                        now = datetime.now()
                        form_time = now.strftime("%m/%d/%Y  %I:%M %p")
                        print(form_time)
                        print("=" * 33)
                        print(f"{"QTY"}   {"NAME"}             {"PRICE"}")
                        for item in cart:
                            unit_price = item['total'] / item['qty']
                            # For each item in the cart, the quantity, name and unit price will be printed.
                            print(f"{item['qty']:>2}    {item['name']:<12.12}     $ {unit_price:>6.2f}")

                        print("-" * 33)
                        print(f"{'SUBTOTAL: ':<20}   $ {sub_total:>6.2f}")
                        print(" ")
                        sales_tax = sub_total * 0.10
                        print(f"{'TAX: ':<8} {'Sales Tax: ':<2}   $ {sales_tax:>6.2f}")
                        total_taxed = sub_total + sales_tax
                        print(f"{'TOTAL:':<20}   $ {total_taxed:>6.2f}")
                        if discount > 0: # This part checks if discount was added and prints it.
                            print(f"DISCOUNT:              $ {discount:.2f}")
                        print(" ")
                        print(f"{'GRAND TOTAL:':<20}   $ {grand_total:>6.2f}")
                        print("-" * 33)
                        print(f"{'AMOUNT TENDERED:':<20}   $ {tendered:>6.2f}")
                        print(f"{'CHANGE:':<20}   $ {change:>2.2f}")
                        print("=" * 33)
                        print("---- THANK YOU FOR SHOPPING! ----")
                        print("----------- Come Again ----------")
                        print("      :) Official Receipt (:     ")
                        print("=" * 33)
                        break
                    except ValueError:
                        print("Sorry wrong selection.")

            # --------------------------------------------- SECTION G ----------------------------------------------
                # This section resets the variables for the next customers
                cart = []
                sub_total = 0
                print(" ")
                print(" ")
                print("--------------------------------------------")
                print("----- BEST BUY RETAIL STORE POS SYSTEM -----")
                print("--------------------------------------------")
                print("-------------- Next Customer ---------------")

if __name__ == "__main__":
        manual_entry_pos()