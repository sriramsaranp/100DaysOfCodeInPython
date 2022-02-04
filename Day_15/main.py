MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

def print_report():
    print(f'water : {resources["water"]}ml')
    print(f'milk : {resources["milk"]}ml')
    print(f'coffee : {resources["coffee"]}g')
    print(f'money : ${round(money,2)}')

def AreResourcesSufficient(var,resources,MENU):
    """Check if the resources are sufficient for the order"""
    if var in MENU:
        for key, value in MENU[var]["ingredients"].items():
            if resources[key] < value:
                print("Sorry, not enough " + key)
                return False
        return True
    else:
        return False

def askMoney():
    """Return the total money entered by the user"""

    while True:
        try:
            print("Please insert coins")
            quarter = int(input('Enter the number of quarters: '))
            dimes = int(input('Enter the number of dimes: '))
            nickels = int(input('Enter the number of nickels: '))
            pennies = int(input('Enter the number of pennies: '))
            amount_entered = quarter * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            return amount_entered
            break
        except ValueError:
            print('Incorrect input')   
isOver = False
while(isOver != True) :
    var = input("What would you like? (espresso/latte/cappuccino): ")
    if(var == "off") :
        isOver = True
    elif (var == "report") :
        print_report()
    else :
        #Check if resources are sufficient before you give the item;
        if (AreResourcesSufficient(var,resources,MENU)) :
            amount_entered = askMoney()
            if (amount_entered >= MENU[var]["cost"]) :
                print("I have enough resources, making you a coffee!")
                print(f"Here is your {var}!")
                for key, value in MENU[var]["ingredients"].items():
                    resources[key] -= value
                money += MENU[var]["cost"]
                change = round(amount_entered - MENU[var]["cost"], 2)
                print(f"Here is your change: ${change}")
                #print_report()
            else :
                print("Sorry, not enough money")
