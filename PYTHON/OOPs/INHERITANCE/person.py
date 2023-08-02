## INHERINTANCE
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printDetails(self):
        print(self.fname, self.lname)

person = Person('Hello', 'World')

person.printDetails()

##child class
class Student(Person):
    
    def printStudent(self):
        print(self.fname, self.lname)
        
student = Student('Print', 'Hello')

student.printStudent()

class Teacher(Person):
    def __init__(self, fname, lname, room):
        super().__init__(fname, lname)
        #self.room = "Office 1"
        self.room = room
    
    def printInfo(self):
        print(self.fname, self.lname, self.room)

teacher = Teacher('Maam', 'Maam', 'Office 1')
teacher.printInfo()