import time
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

# Write a Python program to create a queue and display all the members and size of the queue. Go to the editor
# Expected Output:
# Members of the queue:
# 0 1 2 3
# Size of the queue:
# 4

#NOT DONE 

queue = []

def addOnQueue():
    num = 0
    number = num + 1
    while True:
        queue.append(number)
        time.sleep(1)
        print(queue)
        print(len(queue))

#addOnQueue()
#addNumber()