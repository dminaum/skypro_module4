from src.utils import Category, Product


def test_product_initialization():
    """ Проверка инициализации объекта класса Product """
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
    """ Проверка инициализации объекта класса Category """
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
    """ Проверка правильности подсчета категорий """
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


def test_total_products():
    """ Проверка правильности подсчета продуктов """
    Category.total_products = 0  # обнуляем перед тестом

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

    assert isinstance(Category.total_products, int)
    assert Category.total_products == 3  # всего 3 продукта: 2 из "Гаджетов" и 1 из "Одежды"
