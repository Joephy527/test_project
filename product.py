class Product:
    def __init__(self, name, price, quantity) -> None:
        if price < 0 or quantity < 0:
            raise ValueError('Price and quantity must be greater than 0')

        self.name = name
        self.price= price
        self.quantity = quantity
        
    def calculateTotal(self) -> int:
        return self.price * self.quantity