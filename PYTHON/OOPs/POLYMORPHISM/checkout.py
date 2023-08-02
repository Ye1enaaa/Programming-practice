
class Checkout:
    def __init__(self, itemName, status):
        self.itemName = itemName
        self.status = status
    
    def stats(self):
        print("1")

class Cart:
    def __init__(self, itemName, status):
        self.itemName = itemName
        self.status = status
    
    def stats(self):
        print("1")

check = Checkout('Shoes', '1')
cart = Cart('Wallet', '1')

for same in (check, cart):
    same.stats()