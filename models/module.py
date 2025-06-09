class Product:
    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name

class User:
    def __init__(self, name: str, favorite: Product):
        self.name: str = name
        self.favorite: Product = favorite
