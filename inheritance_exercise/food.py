from inheritance_exercise.product import Product


class Food(Product):
    def __init__(self, name: str) -> None:
        super().__init__(name, 15)

