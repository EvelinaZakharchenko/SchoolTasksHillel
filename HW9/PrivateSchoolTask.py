# - Підґрунтя
# Приватна школа надає непогані послуги по освіті. Прекрасн аудиторії, чисті туалети... Вмотивовані вчителі...
# Та за все треба платити...
# - Технічне завдання
# Розробити програму, яка підрахує на основі зарплат вчителів, директора, заучів та прибиральників,
# скільки дітей та з якою оплатою за навчання треба формувати класи на наступний навчальний рік....

class SchoolWorker:
    def __init__(self, position: str, salary: int, count: int):
        self.__position = position
        self.__salary = salary
        self.count = count

    @property
    def position(self):
        return self.__position

    @property
    def salary(self):
        return self.__salary

    def total_salary_of_position(self):
        total = self.salary * self.count
        return total


class Director(SchoolWorker):
    def __init__(self, count: int):
        super().__init__(
            position="Director",
            salary=30000,
            count=count
        )


class Teacher(SchoolWorker):
    def __init__(self, count: int):
        super().__init__(
            position="Teacher",
            salary=15000,
            count=count
        )


class HeadTeacher(SchoolWorker):
    def __init__(self, count: int):
        super().__init__(
            position="Head teacher",
            salary=20000,
            count=count
        )


class Cleaner(SchoolWorker):
    def __init__(self, count: int):
        super().__init__(
            position="Cleaner",
            salary=10000,
            count=count
        )


if __name__ == "__main__":
    cleaners_count = int(input("Input cleaners count: "))
    headteachers_count = int(input("Input head teachers count: "))
    teachers_count = int(input("Input teachers count: "))
    directors_count = int(input("Input directors count: "))
    students_count = int(input("Input expected students count: "))

    director = Director(directors_count)
    headteacher = HeadTeacher(headteachers_count)
    teacher = Teacher(teachers_count)
    cleaner = Cleaner(cleaners_count)
    students_invoice = (director.total_salary_of_position() + headteacher.total_salary_of_position()
                        + teacher.total_salary_of_position() + cleaner.total_salary_of_position())//students_count
    print(f"Expected invoice from each student is {students_invoice} UAH")

