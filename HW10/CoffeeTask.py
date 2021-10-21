# До кави можна замовити різні заправки на кшталт молочної пінки, соєвого молока, мокко
# (під цією назвою в кавєярнях фігурує додання до кави гарячого шоколаду або шоколадного сиропу)
# та ще прикрасити все це збитими вершками. Заправки не безкоштовні,
# тому їх необхідно вбудувати в систему оформлення замовлень.
from abc import ABC, abstractmethod


def add_milk_foam(cls):
    def wrapper():
        def get_cost(self):
            return int(10)

        def get_name(self):
            return "milk foam"

        cls.get_cost = get_cost
        cls.get_name = get_name

        return cls

    return wrapper()


def add_soy_milk(cls):
    def wrapper():
        def get_cost(self):
            return int(15)

        def get_name(self):
            return "soy milk"

        cls.get_cost = get_cost
        cls.get_name = get_name

        return cls

    return wrapper()


def add_chocolate_syrup(cls):
    def wrapper():
        def get_cost(self):
            return int(20)

        def get_name(self):
            return "chocolate syrup"

        cls.get_cost = get_cost
        cls.get_name = get_name

        return cls

    return wrapper()


def add_whipped_cream(cls):
    def wrapper():
        def get_cost(self):
            return int(5)

        def get_name(self):
            return "whipped cream"

        cls.get_cost = get_cost
        cls.get_name = get_name

        return cls

    return wrapper()


class Coffee(ABC):

    def get_total_cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


@add_milk_foam
class HouseBlend(Coffee):
    def __init__(self, main_name="House Blend", cost=15):
        self.main_name = main_name,
        self.cost = cost,
        self.add_name = self.get_name(),
        self.cost_add = self.get_cost()

    def get_total_cost(self):
        return self.cost[0] + self.cost_add

    def description(self):
        description = f"{self.main_name[0]} with {self.add_name[0]}"
        return description


@add_soy_milk
class DarkRoast(Coffee):
    def __init__(self, main_name="Dark Roast", cost=15):
        self.main_name = main_name,
        self.cost = cost,
        self.add_name = self.get_name(),
        self.cost_add = self.get_cost()

    def get_total_cost(self):
        return self.cost[0] + self.cost_add

    def description(self):
        description = f"{self.main_name[0]} with {self.add_name[0]}"
        return description


@add_chocolate_syrup
class Decaf(Coffee):
    def __init__(self, main_name="Decaf", cost=15):
        self.main_name = main_name,
        self.cost = cost,
        self.add_name = self.get_name(),
        self.cost_add = self.get_cost()

    def get_total_cost(self):
        return self.cost[0] + self.cost_add

    def description(self):
        description = f"{self.main_name[0]} with {self.add_name[0]}"
        return description


@add_whipped_cream
class Espresso(Coffee):
    def __init__(self, main_name="Espresso", cost=15):
        self.main_name = main_name,
        self.cost = cost,
        self.add_name = self.get_name(),
        self.cost_add = self.get_cost()

    def get_total_cost(self):
        return self.cost[0] + self.cost_add

    def description(self):
        description = f"{self.main_name[0]} with {self.add_name[0]}"
        return description


if __name__ == "__main__":
    house_blend = HouseBlend()
    dark_rost = DarkRoast()
    decaf = Decaf()
    espresso = Espresso()
    print(f"{house_blend.description()} costs {house_blend.get_total_cost()}$")
    print(f"{dark_rost.description()} costs {dark_rost.get_total_cost()}$")
    print(f"{decaf.description()} costs {decaf.get_total_cost()}$")
    print(f"{espresso.description()} costs {espresso.get_total_cost()}$")




