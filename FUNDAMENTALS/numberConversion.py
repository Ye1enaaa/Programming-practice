import random

x = 1
y = 2
z = 3.12

def convertNumbers():
    print(complex(x))
    print(float(y))
    print(int(z))

def randomizeNum():
    list = [1, 2, 3, 4, 5]
    randomNumber = random.randrange(1,10)
    print(random.shuffle(list)) # returns None
    print(randomNumber)

#convertNumbers()
randomizeNum()