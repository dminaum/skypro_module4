import pytest
from src.utils import Product
from src.utils import Category


def test_product_initialization():
    # Проверка инициализации объекта класса Product
    product = Product(name="Ноутбук", description="Игровой ноутбук", price=1200.00, quantity=5)

    assert product.name == "Ноутбук"
    assert product.description == "Игровой ноутбук"
    assert product.price == 1200.00
    assert product.quantity == 5


def test_category_initialization():
    # Проверка инициализации объекта класса Category
    product1 = Product(name="Ноутбук", description="Игровой ноутбук", price=1200.00, quantity=5)
    product2 = Product(name="Мышь", description="Беспроводная мышь", price=50.00, quantity=10)
    category = Category(name="Гаджеты", description="Электроприборы и техника", products=[product1, product2])

    assert category.name == "Гаджеты"
    assert category.description == "Электроприборы и техника"
    assert len(category.products) == 2
    assert category.products[0].name == "Ноутбук"
    assert category.products[1].name == "Мышь"


def test_total_categories():
    # Проверка правильности подсчета категорий
    Category.total_categories = 0  # обнуляем перед тестом

    product1 = Product(name="Ноутбук", description="Игровой ноутбук", price=1200.00, quantity=5)
    product2 = Product(name="Мышь", description="Беспроводная мышь", price=50.00, quantity=10)

    category1 = Category(name="Гаджеты", description="Электроприборы и техника", products=[product1, product2])
    category2 = Category(name="Одежда", description="Мужская и женская одежда", products=[product1])

    assert Category.total_categories == 2


def test_total_products():
    # Проверка правильности подсчета продуктов
    Category.total_products = 0  # обнуляем перед тестом

    product1 = Product(name="Ноутбук", description="Игровой ноутбук", price=1200.00, quantity=5)
    product2 = Product(name="Мышь", description="Беспроводная мышь", price=50.00, quantity=10)

    category1 = Category(name="Гаджеты", description="Электроприборы и техника", products=[product1, product2])
    category2 = Category(name="Одежда", description="Мужская и женская одежда", products=[product1])

    assert Category.total_products == 3  # всего 3 продукта: 2 из категории "Electronics" и 1 из "Clothing"
