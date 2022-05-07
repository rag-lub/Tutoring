# @author 
# This program process an inventory and allows purchases to be made.
def main(): # Header for main COMPLETED
    # Menu choices COMPLETED
    SHOW_ITEM_INFORMATION = "1"
    BUY_ITEM = "2"
    QUIT = "3"
    
    # Create 3 empty, single-dimensions lists for variables named names,
    # prices, and quantities
    names = []
    prices= []
    quantities = []
    
    # Call the function named getInventory with "inventory.txt", and the
    # names, prices, and quantities empty lists
    getInventory("inventory.txt", names, prices, quantities)
    
    choice = "0" # COMPLETED
    while(choice != QUIT): # while header COMPLETED
        # Show the menu COMPLETED
        print("=========================")
        print("(1) Show Item Information")
        print("(2) Buy Item")
        print("(3) Quit")
        
        # Prompt for and get the user choice (string) by storing into 
        # the choice variable (Do not convert to an integer)
        choice = input("Choice? ")
        
        # Process the menu choice 
        if (choice == SHOW_ITEM_INFORMATION): # if header COMPLETED
            # Prompt for and retrieve the item name.
            itemName = input("Item name? ")
            
            # Call searchNames with the names list and the item
            # name just entered. Because searchNames returns an index
            # (integer), remember to assign the call to searchNames
            # to a descriptive variable name such as index.
            index = searchNames(names, itemName)
            
            # IF the name is found (index not -1), show the item's price
            # and the quantity in stock (Remember, they are
            # parallel arrays and you just found the index.), 
            # ELSE display that the item is not found.
            if index != -1 :
                print(f"Price: ${prices[index]:.2f}")
                print("Quantity in stock:", quantities[index])
            else:
                print(f'{itemName} not found.')

        elif (choice == BUY_ITEM): # elif header COMPLETED
            # Prompt for and retrieve the item name.
            itemName = input("Iten name? ")
            
            # Call searchNames with the names list and the item
            # name just entered. Because searchNames returns an index
            # (integer), remember to assign the call to searchNames
            # to a descriptive variable name such as index.
            index = searchNames(names, itemName)
            
            #IF the name is found then 
            #    IF there is enough quantity in stock?
            #       display that the item is purchased and 
            #       decrement the quantity in stock for that item; 
            #    ELSE display that the item is sold out.
            # ELSE display that the item is not found.
            if index != -1 :
                if quantities[index] > 0:
                    print(f"{itemName} purchased.")
                    quantities[index] -= 1
                else:
                    print(f"{itemName} sold out.")
            else:
                print(f"{itemName} not found.")
                    
        elif (choice != QUIT): #elif and print COMPLETED. (FYI: No else block)
            print("Invalid choice entered.")
            
    # Call saveInventory with "inventory.txt" and the names, prices, and
    # quantities lists. HINT: When building/testing the program, first
    # write to a different file name such as "inventoryNew.txt"; then when
    # you are sure it works and/or ready to submit, change it to
    # inventory.txt
    saveInventory("inventoryNew.txt", names, prices, quantities)

# getInventory reads comma-delimited item information into
# three different parallel lists
# @param filename The name of the input file
# @param items An empty list that will hold item names
# @param prices An empty list that will hold item prices (floating pt numbers) 
# @param quantities An empty list that will hold item quantities (integers)
def getInventory(filename, items, prices, quantities) :
    inFile = open(filename, "r")
    for line in inFile :
        line = line.split(',')
        items.append(line[0])
        prices.append(float(line[1]))
        quantities.append(int(line[2]))
    inFile.close()
# searchNames performs a case-insensitive linear search for 
# a name in a list of item names.
# REMEMBER: YOU ARE REQUIRED TO UTILIZE/MODIFY THE CODE FROM THE
# LINEAR SEARCH IN THE NOTES (SEE ~P. 69)
# @param names The list of item names
# @param name The name for which to search
# @return The index of the found item name or -1 if not found.
def searchNames(names, name) :
    for i in range(len(names)) :
            if (names[i].lower() == name.lower()) :
                return i
    return -1
        

# saveInventory writes each item's information in comma-delimited form
# to consecutive individual lines in the file indicated by filename
# @param filename The name of the output file
# @param items A list of item names
# @param prices A list of item prices
# @param quantities A list of item quantities
# @precondition items, prices, and quantities are parallel lists
def saveInventory(filename, items, prices, quantities) :
    outFile = open(filename, "w")
    for i in range(len(items)) :
        line = items[i]+","+str(prices[i])+","+str(quantities[i])+ "\n"
        outFile.write(line)
    outFile.close()
main()
