#Розробити клас Людина. Людина має:
#Ім'я
# Прізвище
# Вік (атрибут але ж змінний)
# Стать
# Люди можуть:
# Їсти
# Спати
# Говорити
# Ходити
# Стояти
# Лежати
# Також ми хочемо контролювати популяцію людства. Змінювати популяцію можемо в __init__.
# Треба сказати, що доступ до статичних полів класу з __init__ не можу іти через НазваКласу.статичий_атрибут,
# позаяк ми не може бачити імені класу. Але натомість ми можемо сказати self.__class__.static_attribute.

class Human:
    def __init__(self, first_name: str, last_name: str, age: int, sex, population=1):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.population = population

    def print_my_info(self):
        print(f"Hi! My first name is {self.first_name}, last name is {self.last_name}, I am {age} years old and i am "
              f"a {self.sex}.")

    @staticmethod
    def eat(self):
        print("I am eating")

    @staticmethod
    def talk(self):
        print("I am talking")

    @staticmethod
    def sleep(self):
        print("I am sleeping")

    @staticmethod
    def walk(self):
        print("I am walking")

    @staticmethod
    def lay(self):
        print("I am laying")

    @staticmethod
    def stay(self):
        print("I am staying")

    def born(self):
        self.population += 1
        self.age = 0
        print(f"I am newborn. Now population = {self.population}")

    def birthday(self):
        self.age += 1
        print(f"It's my birthday! Now i'm {self.age} years old")







