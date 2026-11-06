class Item():
    def __init__(self, 
                 name: str, 
                 description: str = None, 
                 price: float = None, 
                 tax: float = None):
        self.name = name
        self.description = description
        self.price = price
        self.tax = tax
    