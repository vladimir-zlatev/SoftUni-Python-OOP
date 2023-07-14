from typing import List
from inheritance_exercise.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        res = [prod for prod in self.products if prod.name == product_name]

        if res:
            return res[0]

    def remove(self, product_name: str) -> None:
        res = self.find(product_name)

        if res:
            self.products.remove(res)

    def __repr__(self):
        return "\n".join([f"{prod.name}: {prod.quantity}" for prod in self.products])

