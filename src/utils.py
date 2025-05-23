from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __str__(self):
        """Возвращает строку с описанием продукта"""

    def __add__(self, other):
        """Складывает продукты одного типа"""

    @property
    @abstractmethod
    def price(self):
        """Позволяет узнать цену продукта"""

    @price.setter
    @abstractmethod
    def price(self, new_price):
        """Позволяет устанавливать новую цену на продукт. Она должна быть больше 0"""


class LoggerMixin:
    def __init__(self, *args, **kwargs):
        print(
            f"Создан объект класса {self.__class__.__name__} с аргументами: {args}, {kwargs}"
        )
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})>"


class Product(LoggerMixin, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity, *args, **kwargs):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
        if type(self) is not type(other):
            raise TypeError("Складывать можно только продукты одного типа")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_dict: dict):
        name, description, price, quantity = (
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"],
        )
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    name: str
    description: str
    __products: list

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_products += len(products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его подклассов"
            )
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        products_info = ""
        for product in self.__products:
            products_info += f"{product}\n"
        return products_info

    def get_average_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            total_products = len(self.__products)
            return total_price / total_products
        except ZeroDivisionError:
            return 0

class Smartphone(Product):
    efficiency: str
    model: str
    memory: str
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.model}, {self.memory},"
            f"{self.color}) - {self.price} руб. Остаток: {self.quantity} шт."
        )


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.country}, {self.germination_period},"
            f"{self.color}) - {self.price} руб. Остаток: {self.quantity} шт."
        )
