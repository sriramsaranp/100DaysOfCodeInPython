from calendar import month_name
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_over = False
menu = Menu()
#menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while is_over != True :
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if(choice == "off") :
        is_over = True
    elif (choice == "report") :
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        #Check if resources are sufficient
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) == True :
            if money_machine.make_payment(drink.cost) :
                coffee_maker.make_coffee(drink)
            # print(coffee_maker.report())
            # print(money_machine.report())  
            

