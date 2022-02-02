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
    print(f'money : ${money}')
isOver = False
while(isOver != True) :gith
    var = input("What would you like? (espresso/latte/cappuccino): ")
    if(var == "off") :
        isOver = True
    elif (var == "report") :
        print_report()
    else :
        #Check if resources are sufficient before you give the item
        



