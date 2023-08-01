def insertFruit():
    fruits = ['dragonfruit', 'banana', 'durian']
    fruits.insert(0, 'melon')
    return fruits
    print(fruits)

def addFruitsToList():
    fruits = ['apple', 'mango', 'watermelon']
    fruits.append('grapes')
    return fruits
    print(fruits)

def extendListOfFruits():
    fruit1 = insertFruit()
    fruit2 = addFruitsToList()
    fruit1.extend(fruit2)
    return fruit1
    print(fruit1)

def clearListOfFruits():
    listChecker = extendListOfFruits()
    if len(listChecker) == 8:
        listChecker.clear()
    print(listChecker)

clearListOfFruits()
#addFruitsToList()