"""This module contains the Product class for managing store products."""

class Product:
    """A class representing a product in the store."""
    
    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a product with name, price, and quantity."""
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
    
    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity
    
    def set_quantity(self, quantity: int):
        """Set the product quantity and deactivate if quantity reaches zero."""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()
    
    def is_active(self) -> bool:
        """Check if the product is active."""
        return self.active
    
    def activate(self):
        """Activate the product."""
        self.active = True
    
    def deactivate(self):
        """Deactivate the product."""
        self.active = False
    
    def show(self):
        """Display product information."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")
    
    def buy(self, quantity: int) -> float:
        """Purchase a quantity of the product and return total price."""
        if not self.active:
            raise ValueError("Product is not active")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available")
        
        total_price = self.price * quantity
        self.quantity -= quantity
        
        if self.quantity == 0:
            self.deactivate()
        
        return total_price


def main():
    """Test function for Product class."""
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