import datetime

class Restaurant:
    def __init__(self, open_time, close_time, tables, staff, menu):
        self.open_time = open_time
        self.close_time = close_time
        self.tables = tables
        self.staff = staff
        self.menu  = menu

    def __str__(self):
        lst = []
        lst.append('Welcome to JazzyPlace!')
        lst.append('There are {0} tables in our restaurant'.format(len(self.tables)))
        lst.append('The menu includes {0}'.format(', '.join([dish.name for dish in self.menu])))
        return '\n'.join(lst)

    def open_close(self):
        lst = str(datetime.datetime.now()).split()[1].split(':')
        now = int(lst[0]+lst[1])
        
        opentime = int(''.join(self.open_time.split('.')))
        closetime = int(''.join(self.close_time.split('.')))

        if opentime <= now <= closetime:
            print("Come in! We're opened\n")
        else:
            print("Sorry, we're closed\n")

    def add_dish(self, new_dish):
        if new_dish in self.menu:
            print('The dish "{0}" is already in menu\n'.format(new_dish.name))
            return
        self.menu.append(new_dish)
        print('Now the dish "{0}" is in menu'.format(new_dish.name))

    def pop_dish(self, old_dish):
        if old_dish not in self.menu:
            print('There is no dish named "{0}" in menu\n'.format(old_dish))
            return
        for i,e in enumerate(self.menu):
            if e == old_dish:
                self.menu.pop(i)
                break

    def change_dish(self, name, new_name):
        for dish in menu:
            if dish.name == name:
                dish.name = new_name

    #def work:
    #    return
    

class Dish:
    def __init__(self, name, price, ingredients, weight, caloricity):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.weight = weight
        self.caloricity = caloricity

    def __str__(self):
        lst = []
        lst.append('{0} costs {1} rubles'.format(self.name, self.price))
        lst.append('it weights {0}g and has {1} callories'.format(self.weight, self.caloricity))
        lst.append('{0} consists of {1} and {2}'.format(self.name, ', '.join(self.ingredients[:-1]), self.ingredients[-1]))
        return '\n'.join(lst)

    def change_price(self, price):
        self.price = price

    def change_ingredients(self, ingredients):
        self.ingredients = ingredients

    def change_weight(self, weight):
        self.weight = weight

    def change_caloricity(self, caloricity):
        self.caloricity = caloricity

"""menu=[]
menu.append(Dish('latte', 200, ['coffee', 'milk', 'water'], 500, 80))
menu.append(Dish('lemonade', 150, ['water', 'sugar', 'lemon'], 200, 100))

r = Restaurant('9.00', '14.00', [1, 2, 3, 4, 5, 6], 'staff', menu)
print(r, '\n')
r.open_close()

new_dish = Dish('pizza', 500, ['pepperoni', 'tomatoes', 'cheese', 'pastry'], 500, 1600)
r.add_dish(new_dish)
r.pop_dish('coffee')

r.change_dish('lemonade', 'lime lemonade')
print(r, '\n')

print(menu[1], '\n')
menu[1].change_caloricity(180)
print(menu[1])
"""

class Person:
    def __init__(self, FIO, age):
        self.FIO = FIO
        self.age = age
        

class Staff(Person):
    def __init__(self, FIO, age, experience, salary, timetable):
        self.experience = experience
        self.salary = salary
        self.timetable = timetable
        super(Staff, self).__init__(FIO, age)

    def __str__(self):
        lst = []
        lst.append('{0}, {1} y.o.'.format(self.FIO, self.age))
        
        s = 'year'
        if self.experience != 1:
            s += 's'
        lst.append('Works for {0} {3}, timetable is {2}, salary equals {1}$'.format(self.experience, self.salary, self.timetable, s))
        
        return '\n'.join(lst)


class Manager(Staff):
    def __init__(self, FIO, age, experience, salary, timetable, tables, cash):
        self.tables = tables    #список всех столов в зале
        self.cash = cash
        super(Manager, self).__init__(FIO, age, experience, salary, timetable)

        def count_money(self):
            print('We have {0}$'.format(self.cash))

        def book_table(self, table):
            print('Table {0} is booked'.format(table))

        def unbook_table(self, table):
            print('Table {0} is unbooked'.format(table))

        def solve_conflicts(self, table):
            print('I will help you, table {0}'.format(table))


manager1 = Manager('Manager Katya', 32, 7, 45000, '5/2', [1, 2, 3, 4, 5, 6, 7, 19], 900)
manager1.count_money()
    
from collections import Counter
class CleaningManager(Staff):
    def __init__(self, FIO, age, experience, salary, timetable, tools):
        self.tools = tools
        super(CleaningManager, self).__init__(FIO, age, experience, salary, timetable)

    def check_tool(self):
        print(dict(Counter(self.tools)))

    def clean_floor(self):
        if 'bucket' in self.tools and 'mop' in self.tools:
            print('I will clean the floor')
        elif 'bucket' not in self.tools:
            print('There is no bucket')
        elif 'moph' not in self.tools:
            print('There is no mop')
        else:
            print('There is no bucket neither mop')

"""clean1 = CleaningManager('Mr. Proper', 40, 1, 50, '3/4', ['mop', 'bucket', 'bucket', 'rag', 'ball'])
clean1.check_tool()
clean1.clean_floor()"""

#человек, работник, официант, менеджер, уборщица

                                       



p = Staff('Harry Potter', 25, 15, 200, '5/2')
print(p)





