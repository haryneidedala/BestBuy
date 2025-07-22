from products import Product
from store import Store

def setup_initial_inventory():
    """Creates and returns a Store with default inventory"""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    return Store(product_list)

def list_all_products(store):
    """Lists all active products in the store"""
    print("\nAvailable Products:")
    for i, product in enumerate(store.get_all_products(), 1):
        print(f"{i}. ", end="")
        product.show()

def show_total_amount(store):
    """Shows total quantity of all products in store"""
    print(f"\nTotal amount in store: {store.get_total_quantity()}")

def make_order(store):
    """Handles the order process"""
    products = store.get_all_products()
    if not products:
        print("No products available!")
        return
    
    list_all_products(store)
    shopping_list = []
    
    try:
        while True:
            print("\nEnter product number and quantity (or 'done' to finish):")
            choice = input("> ").strip().lower()
            
            if choice == 'done':
                break
            
            try:
                product_num, quantity = map(int, choice.split())
                if 1 <= product_num <= len(products) and quantity > 0:
                    product = products[product_num - 1]
                    shopping_list.append((product, quantity))
                    print(f"Added {quantity} of {product.name} to order")
                else:
                    print("Invalid product number or quantity")
            except ValueError:
                print("Invalid input. Please enter 'product_number quantity' or 'done'")
        
        if shopping_list:
            total = store.order(shopping_list)
            print(f"\nOrder successful! Total price: ${total:.2f}")
        else:
            print("No items ordered")
    except Exception as e:
        print(f"\nError processing order: {e}")

def start(store):
    """Main menu interface"""
    while True:
        print("\nStore Menu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        
        choice = input("Please choose an option (1-4): ").strip()
        
        if choice == '1':
            list_all_products(store)
        elif choice == '2':
            show_total_amount(store)
        elif choice == '3':
            make_order(store)
        elif choice == '4':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4")

def main():
    """Entry point of the program"""
    best_buy = setup_initial_inventory()
    start(best_buy)

if __name__ == "__main__":
    main()