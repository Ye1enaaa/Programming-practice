## Basics

##Classes and Inheritance
class Sample:
    data = 5

#print(Sample.data)

class Cart:
    def __init__(self, item, status):
        self.item = item
        self.status = status

    def printItems(self):
        print(self.item)

items = Cart("Shoes", 1)

items.printItems()
#print(items.item)
#print(items.status)