class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self,item_name,price,quantity):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price':price,'quantity':quantity}
        print(f"{quantity} x {item_name} added to cart.")

    def remove_items(self,item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} removed from cart.")
        else:
            print(f"{item_name} not found in cart.")

    def get_total(self):
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        print(f"Total: ₹{total}")
        return total

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("Cart Contents:")
        for item_name,details in self.items.items():
            price = details["price"]
            quantity = details["quantity"]
            print(f"- {item_name}: ₹{price} x {quantity} = ₹{price * quantity}")


cart = ShoppingCart()
cart.add_item("Apple", 10, 2)
cart.add_item("Banana", 5, 5)
cart.show_cart()
cart.get_total()
cart.remove_items("Apple")
cart.show_cart()