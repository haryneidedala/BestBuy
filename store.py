from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = products  # List to store all products

    def add_product(self, product: Product):
        """Add a product to the store"""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store"""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns total quantity of all products in store"""
        total = 0
        for product in self.products:
            if product.is_active():
                total += product.get_quantity()
        return total

    def get_all_products(self) -> List[Product]:
        """Returns all active products in the store"""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Makes an order with a shopping list of products and quantities
        Returns total price of the order
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"Product {product.name} not in store")
            total_price += product.buy(quantity)
        return total_price


def main():
    from products import Product
    
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)]
    
    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main__":
    main()