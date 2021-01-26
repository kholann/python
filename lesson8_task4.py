# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Warehouse:
    def __init__(self, title):
        self.title = title
        self.lists = {}

    def take(self, equipment, number):
        self.lists.update({equipment.title: number})
        print(f"На склад {self.title} получено оборудование {equipment.title} в количестве {number}")

    def give(self, equipment, other, number):
        if self.lists.__contains__(equipment.title) and self.lists[equipment.title] - number >= 0:
            print(f"Передано оборудование {equipment.title} в подразделение {other.title} в количестве {number}")
            other.take(equipment, number)
            self.lists.update({equipment.title: self.lists[equipment.title] - number})
        else:
            print(f"Нет {equipment.title} в {self.title} в количестве {number}!")

    def validation(self, equipment, number):
        try:
            number = int(number)
            self.take(equipment, number)
        except ValueError:
            print(f"Не число для {equipment.title}!")

class Office_equipment:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return str(self.title)

class Printer(Office_equipment):
    def __init__(self, title, type):
        Office_equipment.__init__(self, title)
        self.type = type

    def __str__(self):
        return f"Принтер {self.title} с типом {self.type}"

class Scanner(Office_equipment):
    def __init__(self, title, serial_number):
        Office_equipment.__init__(self, title)
        self.serial_number = serial_number

    def __str__(self):
        return f"Сканер {self.title} с номером {self.serial_number}"

class Xerox(Office_equipment):
    def __init__(self, title, year):
        Office_equipment.__init__(self, title)
        self.year = year

    def __str__(self):
        return f"Ксерокс {self.title} с годом выпуска {self.year}"

s1 = Warehouse('Warehouse1')
s2 = Warehouse('Warehouse2')

pr1 = Printer('HP', 'laser')
sc = Scanner('Epson', 4000)
xe = Xerox('Brother', 2000)

print(pr1)
print(sc)
print(xe)

num_pr = input('Введите количество принтеров: ')
s1.validation(pr1, num_pr)

num_sc = input('Введите количество сканеров: ')
s1.validation(sc, num_sc)

num_xe = input('Введите количество ксероксов: ')
s1.validation(xe, num_xe)

s1.give(pr1, s2, 1)
s1.give(sc, s2, 2)
s1.give(xe, s2, 1)

print(s1.lists)
print(s2.lists)