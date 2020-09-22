#var to hold dictionary
shoppingCart = {}

#print interface
print("""
      Shopping Options
      ----------------
      1: Add Item
      2: Remove Item
      3: View Cart
      0: EXIT
      """)

#prompt user and turn into integer
option = int(input("Select an option: "))

#while user doesn't exit program
while option != 0:
    if option == 1:
        #add item
        #prompt user for item and qty
        item = input("Enter an item: ")

        #if item already exists in cart
        if item in shoppingCart:
            print("Item already in cart")
            qty = int(input("Enter quantity: "))
            #update qty
            shoppingCart[item] += qty
        #if it does not
        else:
            qty = int(input("Enter quantity: "))
            #add qty to the item key
            shoppingCart[item] = qty

    elif option == 2:
        #remove item
        # prompt user for itme to be removed
        item = input("Enter an item: ")
        #remove it
        del (shoppingCart[item])

    elif option == 3:
        #loop through items in cart
        for item in shoppingCart:
            #print each item
            print(item, ":", shoppingCart[item])

    elif option != 0:
        #in case user enters invalid option
        print("Please enter a valid option")

    option = int(input("\n\nSelect an option: "))

#when loop breaks and exits
else:
    print("You closed the program...")
