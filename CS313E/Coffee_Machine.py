#make a class for general beverages

class Beverage:
    def __init__(self,**kwargs):
        self.__name = kwargs.get('name')
        self.__price = kwargs.get('price')
        self.__caffeine = kwargs.get('caffeine')
        self.__calories = kwargs.get('calories')
    def __str__(self):
        return f'A {self.__name}, has {self.__calories} calories, and is ${self.__price:,.2f}'
    def brew(self):
        return f'{self.__name} is brewing'
class Tea(Beverage):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__color = kwargs.get('color')
    def __str__(self):
        return super().__str__() + ', the color is ' + str(self.__color) 
class Latte(Beverage):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__lactose = kwargs.get('lactose')
    def __str__(self):
        return super().__str__() + ', the lactose level is ' + str(self.__lactose)
class Condiment:
    def __init__(self,**kwargs):
        self.__name = kwargs.get('name')
        self.__amount = kwargs.get('amount')
    def addCondiment(self):
        if int(self.__amount) <= 3 and int(self.__amount) >= 0:
            return f'{self.__amount} levels of {self.__name} is being added to your drink'
        else:
            return f'You have entered an invalid amount of {self.__name}'

        
