def forLoopsIndex():
    fruits = ['dragonfruit', 'banana', 'durian']
    for fruit in range(len(fruits)):
        print(fruits[fruit])

    fruits = ['apple', 'mango', 'watermelon']
    for fruit in fruits:
        print(fruit)

def listComprehend():
    cart = ['Shoes', 'Bags', 'Wallet']
    sell = []

    for items in cart:
        if "s" in items:
            sell.append(items)
    
    print(sell)

def checkOutItems():
    check = []
    cart = [
        {
            'item': 'Shoes',
            'status' : 0
        },
        {
            'item': 'Bag',
            'status': 1
        },
        {
            'item': 'Wallet',
            'status': 1
        }
    ]
    for item in cart:
        status = item["status"]
        if status == 1:
            check.append(item)
    
    print(check)

checkOutItems()