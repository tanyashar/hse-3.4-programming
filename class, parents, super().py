class Person:
    def __init__(self, FIO, age):
        self.FIO = FIO
        self.age = age
        
    def __str__(self):
        return self.FIO + ' age = ' + str(self.age)
    
class Staff(Person):
    def __init__(self, FIO, age, experience, salary, timetable):
        self.experience = experience
        self.salary = salary
        self.timetable = timetable
        super(Staff, self).__init__(FIO, age)

#s = Staff('Ivanov Ivan Ivanovich', 24, 1, 10000, '5/2')
#print(s)

class Waiter(Staff):
    def __init__(self, FIO, age, experience, salary, timetable, menu, tables):
        self.menu = menu
        self.tables = tables
        super(Waiter, self).__init__(FIO, age, experience, salary, timetable)

    def clean_table(self, table):
        if table in self.tables:
            print('table ' + str(table) + ' cleaned')
        else:
            print('this is not my table')

    def get_menu(self):
        print('Here is your menu')
        return self.menu

    def take_order(self, order, table):
        print('Your order is taken')

    def bring_order(self, order, table):
        print('Order ' + str(order) + ' to table ' + str(table))

    def bring_check(self, check):
        print('Here is your check: ' + str(check))


"""waiter1 = Waiter('thing 1', 18, 0, 10000, '5/2', '-', [1, 2, 3])
waiter2 = Waiter('thing 2', 19, 0, 10000, '5/2', '-', [4, 5, 6])

waiter1.clean_table(4)
waiter2.clean_table(4)

waiter1.get_menu()
waiter1.take_order('mushrooms and wine', 2)
waiter1.bring_order('mushrooms and wine', 2)
waiter1.bring_check(300)"""

from collections import Counter
class CleaningManager(Staff):
    def __init__(self, FIO, age, experience, salary, timetable, tools):
        self.tools = tools
        super(CleaningManager, self).__init__(FIO, age, experience, salary, timetable)

    def check_tool(self):
        print(Counter(self.tools))

    def clean_floor(self):
        if 'bucket' in self.tools and 'moph' in self.tools:
            print('I will clean floor')
        elif 'bucket' not in self.tools:
            print('There is no bucket')
        elif 'moph' not in self.tools:
            print('There is no moph')
        else:
            print('There is no bucket neither moph')
            
"""clean1 = CleaningManager('woman 1', 40, 1, 5000, '3/4', ['moph', 'bucket', 'bucket', 'anything'])
clean1.check_tool()
clean1.clean_floor()"""     

class Manager(Staff):
    def __init__(self, FIO, age, experience, salary, timetable, tables, cash):
        self.tables = tables    #tables = список всех столов в зале
        self.cash = cash
        super(Manager, self).__init__(self, FIO, age, experience, salary, timetable)

        def count_money(self):
            print('We have ' + str(self.cash) + '$')

        def book_table(self, table):
            print('Table ' + str(table) + ' booked')

        def unbook_table(self, table):
            print('Table ' + str(table) + ' unbooked')

        def solve_conflicts(self, table):
            print('I will help you ' + str(table))
            

class Director(Manager):
    def __init__(self, FIO, age, experience, salary, timetable, tables, budget, phone):
        self.phone = phone
        super(Director, self).__init__(self, FIO, age, experience, salary, timetable, tables, budget)

    def __str__(self):
        return "I'm the director" 
        
manager1 = Manager('manager 1', 32, 7, 45000, '5/2', [1, 2, 3, 4, 5, 6, 7, 19], 900)

#director1 = Director()    
