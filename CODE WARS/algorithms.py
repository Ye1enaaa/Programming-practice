#Write a Python program to insert items into a list in sorted order.
#Original List:
numbers = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
origNumbers = numbers.copy()
def addNumber():
    
    number = ''
    while number != '00000':
        number = input("Enter a number ")
        numbers.append(int(number))
    
    numbers.pop()
    numbers.sort()

    print("Original List:")
    print(origNumbers)
    print("Sorted List")
    print(numbers)


addNumber()