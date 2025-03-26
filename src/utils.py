class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict):
        name, description, price, quantity = (
            product_dict['name'], product_dict['description'], product_dict['price'], product_dict['quantity'])
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print('Цена не должна быть нулевая или отрицательная')


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

    def add_product(self, product):
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        products_info = ""
        for product in self.__products:
            products_info += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_info
