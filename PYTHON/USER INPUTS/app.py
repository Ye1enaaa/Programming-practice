## Create a List of Favorite Food
foodList = []
print("Hello!! Welcome to Food List!!")
print("Type x to exit")
food = ''
while food != 'x':
    food = input('Input your desired food ')
    foodList.append(food)

if food == 'x':
    foodList.pop()
    for food in foodList:
        letterCapitalize = food[0]
        letCap = letterCapitalize.capitalize()

print(foodList)