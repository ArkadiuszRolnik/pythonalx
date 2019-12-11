from basket import Product
from basket import Basket


class TestBasket:

    def test_init(self):

        product = Product(1, "Woda", 10.00)
        assert product.id == 1
        assert product.name == "Woda"
        assert product.price == 10.00

    def test_create_basket(self):
        basket = Basket()
        assert True

    def test_add_product_to_basket(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        basket.add_product(product, 5)
        assert len(basket.items) == 1
        product2 = Product(2, "Chleb", 2)
        basket.add_product(product2, 2)
        assert len(basket.items) == 2

    def test_count_total_price(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        basket.add_product(product, 5)
        assert basket.count_total_price() == 50
        product2 = Product(2, "Chleb", 2)
        basket.add_product(product2, 2)
        assert basket.count_total_price() == 54

    def test_generate_report(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        basket.add_product(product, 5)
        expected = '''Produkty w koszyku:
- Woda (1), cena: 10 x 5
W sumie: 50'''
        assert basket.generate_report() == expected



