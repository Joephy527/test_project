class ShoppingCart:
    def __init__(self) -> None:
        self.cart = []
        
    def addProduct(self, product):
        self.cart.append(product)
    
    def calculateTotal(self):
        total = 0
        
        for item in self.cart:
            total += item.calculateTotal()
        
        return total