class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
    
    def get_quantity(self) -> int:
        return self.quantity
    
    def set_quantity(self, quantity: int):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()
    
    def is_active(self) -> bool:
        return self.active
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")
    
    def buy(self, quantity: int) -> float:
        if not self.active:
            raise Exception("Product is not active")
        if quantity <= 0:
            raise Exception("Quantity must be positive")
        if quantity > self.quantity:
            raise Exception("Not enough quantity available")
        
        total_price = self.price * quantity
        self.quantity -= quantity
        
        if self.quantity == 0:
            self.deactivate()
        
        return total_price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()