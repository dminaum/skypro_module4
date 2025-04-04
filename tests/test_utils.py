import pytest

from src.utils import Category, Product


def test_product_initialization():
    """Проверка инициализации объекта класса Product"""
    product = Product(
        name="Ноутбук", description="Игровой ноутбук", price=1200.00, quantity=5
    )

    assert product.name == "Ноутбук"
    assert product.description == "Игровой ноутбук"
    assert isinstance(product.price, float)
    assert product.price == 1200.00
    assert isinstance(product.quantity, int)
    assert product.quantity == 5


def test_category_initialization():
    """Проверка инициализации объекта класса Category"""
    product1 = Product(
        name="Ноутбук", description="Игровой ноутбук", price=1200.00, quantity=5
    )
    product2 = Product(
        name="Мышь", description="Беспроводная мышь", price=50.00, quantity=10
    )
    category = Category(
        name="Гаджеты",
        description="Электроприборы и техника",
        products=[product1, product2],
    )

    assert category.name == "Гаджеты"
    assert category.description == "Электроприборы и техника"
    assert isinstance(category.products, str)
    assert category.total_products == 2


def test_total_categories():
    """Проверка правильности подсчета категорий"""
    Category.total_categories = 0  # обнуляем перед тестом

    product1 = Product(
        name="Ноутбук", description="Игровой ноутбук", price=1200.00, quantity=5
    )
    product2 = Product(
        name="Мышь", description="Беспроводная мышь", price=50.00, quantity=10
    )

    category1 = Category(
        name="Гаджеты",
        description="Электроприборы и техника",
        products=[product1, product2],
    )
    category2 = Category(
        name="Одежда", description="Мужская и женская одежда", products=[product1]
    )

    assert isinstance(Category.total_categories, int)
    assert Category.total_categories == 2


def test_add_valid_product():
    """Проверка добавления корректного продукта в категорию"""
    category = Category(
        name="Гаджеты", description="Электроприборы и техника", products=[]
    )
    product = Product(
        name="Ноутбук", description="Игровой ноутбук", price=1200.00, quantity=5
    )

    category.add_product(product)

    assert category.products.strip() == "Ноутбук, 1200.0 руб. Остаток: 5 шт."
    assert Category.total_products > 0  # Учитываем глобальный счётчик


def test_add_invalid_product():
    """Проверка вызова исключения, если передан не Product"""
    category = Category(
        name="Гаджеты", description="Электроприборы и техника", products=[]
    )

    with pytest.raises(TypeError, match="Ожидается объект класса Product"):
        category.add_product("не продукт")  # Ошибка, не объект Product


def test_category_total_products():
    """Проверяем, что общий счётчик продуктов обновляется корректно"""
    initial_products = Category.total_products
    category = Category(
        name="Электроника",
        description="Техника",
        products=[
            Product(name="Телефон", description="Смартфон", price=500, quantity=10)
        ],
    )
    category.add_product(
        Product(name="Планшет", description="Гаджет", price=700, quantity=5)
    )

    assert Category.total_products == initial_products + 2


def test_product_add():
    """Проверка сложения двух продуктов"""
    product1 = Product("Товар A", "Описание A", 100, 10)
    product2 = Product("Товар B", "Описание B", 200, 2)

    assert product1 + product2 == 1400  # 100 * 10 + 200 * 2 = 1400


def test_product_add_invalid():
    """Проверка исключения при сложении с объектом другого типа"""
    product = Product("Товар A", "Описание A", 100, 10)

    with pytest.raises(
        TypeError, match="Складывать можно только объекты класса Product"
    ):
        product + "не продукт"


def test_product_str():
    """Проверка строкового представления продукта"""
    product = Product("Товар A", "Описание A", 100, 10)

    assert str(product) == "Товар A, 100 руб. Остаток: 10 шт."


def test_category_str():
    """Проверка строкового представления категории"""
    Category.total_products = 0
    category = Category("Гаджеты", "Электроприборы и техника", [])

    assert str(category) == "Гаджеты, количество продуктов: 0 шт."

    product1 = Product("Ноутбук", "Игровой ноутбук", 1200, 5)
    product2 = Product("Смартфон", "Флагманский смартфон", 800, 3)

    category.add_product(product1)
    category.add_product(product2)

    assert str(category) == "Гаджеты, количество продуктов: 8 шт."
