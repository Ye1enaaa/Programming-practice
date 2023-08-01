#Datas
#list

fruits = ['apple', 'banana']

#print(fruits[0] + " "+ fruits[1])

#tuple
fruits = ('apple', 'banana')
#print(fruits[0])

#map / dict
x = {"name" : "John", "age" : 36}
#print(x["name"])

#map in a list
users = [
    {
        "name" : "John", 
        "age" : 36
    },
    {
        "name": "Hello",
        "age": 36
    }
]
for user in users:
    print(user["name"] , "is" , user["age"] , "years old")

#sets
fruits = {
    'apple', 
    'banana'
}
for fruit in fruits:
    print(fruit)