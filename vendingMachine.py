# a dictionary filled with all the drinks and their respective prices
drinks = {
    1: {"drinks": "Yeo's Grass Jelly", "price": 10},
    2: {"drinks": "Teh Tarik", "price": 30},
    3: {"drinks": "Coca-Cola", "price": 40},
    4: {"drinks": "100 Plus", "price": 33}
}

# money in RM
# assume logically that the user can insert RM100 as the 
# largest amount of money and only buy one drink at a time
rm = [100, 50, 20, 10, 5, 1]

def showDrinks():
    print("\nDrinks available :\n")
    for no in drinks:  
        drink = drinks[no]
        print(str(no) + ". " + drink['drinks'] + " = RM " + str(drink['price']))

def drinkChosen(chooseDrink, amountInserted):
    # catch exception when user insert the wrong drink choice
    if chooseDrink not in drinks:
        print("Invalid drink choice.")
        #return showDrinks()

    drink = drinks[chooseDrink]
    price = drink['price']
    if amountInserted < price:
        print("Please insert more money.")
        #return showDrinks()

    amountOfChange = amountInserted - price
    print("------------------------------")
    print("Drink Bought: " + drink['drinks'])
    print("Price: RM " + str(price))
    print("Total Amount of amountOfChange: RM " + str(amountOfChange))
    print("------------------------------")
    print("Amount of amountOfChange returned:")
    
    noOfNotes = 0

    # this for loop will iterate over each available note value in desc order to dispense the amountOfChange
    for n in rm:
        while amountOfChange >= n: # while the amountOfChange is less or equal to the amount of note
            print("RM " + str(n)) # display each of the note which are dispensed
            amountOfChange = amountOfChange - n # then minus the dispensed note from the amountOfChange
            noOfNotes += 1

    print("------------------------------")
    print("No of notes dispensed: " + str(noOfNotes))

showDrinks()
print()

# allows user to input their decision of drinks and amount of money inserted
chooseDrink = int(input("Please enter the number of the drink that you want: "))
amountInserted = int(input("Please enter the amount of money inserted (in RM): "))
print()

drinkChosen(chooseDrink, amountInserted)
