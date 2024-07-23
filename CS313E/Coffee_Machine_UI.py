from Coffee_Machine import Beverage
from Coffee_Machine import Tea
from Coffee_Machine import Latte
from Coffee_Machine import Condiment

def main():

    #Customer picks their drinks
    print("Welcome to the best coffee machine!")

    print("")
    print("We have six drink options to pick from:")
    print("  1. Black Tea")
    print("  2. Green Tea")
    print("  3. Yellow Tea")
    print("  4. Espresso")
    print("  5. Americano")
    print("  6. Latte Macchiato")
    print("")

    drink = int(input("Enter the number corresonding with your drink of choice: "))

    #creating my drinks
    black_tea = Tea(name = 'Black Tea', price = 2.50, caffeine = 90, calories = 80, color = 'black')  
    green_tea = Tea(name = 'Green Tea', price = 3.00, caffeine = 70, calories = 65, color = 'green')
    yellow_tea = Tea(name = 'Yellow Tea', price = 2.50, caffeine = 0, calories = 80, color = 'yellow')
    espresso = Beverage(name = 'Espresso', price = 3.50, caffeine = 90, calories = 80)
    americano = Beverage(name = 'Americano', price = 4.00, caffeine = 90, calories = 80)
    latte_machiatto = Latte(name = 'Latte Machiatto', price = 5.00, caffeine = 90, calories = 80, lactose = 15)


    #printing the drink stats
    if drink == 1:
        print(black_tea.__str__())
        print(black_tea.brew())
    elif drink == 2:
        print(green_tea.__str__())
        print(green_tea.brew())
    elif drink == 3:
        print(yellow_tea.__str__())
        print(yellow_tea.brew())
    elif drink == 4:
        print(espresso.__str__())
        print(espresso.brew())
    elif drink == 5:
        print(americano.__str__())
        print(americano.brew())
    else:
        print(latte_machiatto.__str__())
        print(latte_machiatto.brew())

    #add condiments
    print("")
    while True:
        sugar = input("Please pick a sugar level from 0 to 3: ")
        con1 = Condiment(name = 'sugar', amount = sugar)
        if con1.addCondiment() == 'You have entered an invalid amount of sugar':
            print(con1.addCondiment())
            continue
        else:
            print(con1.addCondiment())
            break

    print("")
    
    while True:
        milk = input("Please pick a milk level from 0 to 3: ")
        con2 = Condiment(name = 'milk', amount = milk)
        if con2.addCondiment() == 'You have entered an invalid amount of milk':
            print(con2.addCondiment())
            continue
        else:
            print(con2.addCondiment())
            break

    print("")
    print("Your drink is ready!")
    print("")
    print("")

main()
keep_going = input("If you want to order another drink enter 1, otherwise enter any other value: ")

while True:
    if keep_going == "1":
        main()
    else:
        print("Thank you")
        break
    print("")
    keep_going = input("If you want to order another drink enter 1, otherwise enter any other value: ")
    print("")


    

    

    



