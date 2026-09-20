# {"name": "Shubhendu", "age": 30, "city": "New York", "marks": 90}
## {"name": "Aman", "age": 20, "city": "WA", "marks": 80}
## {"name": "Ajay", "age": 25, "city": Blr", "marks": 70}




# self forces to store all the values along with its variable inside that 
# class object
class Student:
    # name 
    # age
    # city
    # marks
    def __init__(self, name, age, city, marks):
        self.name = name
        self.age = age
        self.city = city
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Marks: {self.marks}")

    def greetings(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old from {self.city}. I scored {self.marks} marks."


# Student.__init__()

student1 = Student("Shubhendu", 30, "New York", 90) #object creation ??
student2 = Student("Aman", 20, "WA", 80)


#student1.display_info()
greet_message = student1.greetings()
#print(greet_message)


student_list = []
student_list.append(student1)
student_list.append(student2)

for i in student_list:
    print(i.greetings())

#class : The keyword that start a brand-new blueprint defintion
# Student: The name you are giving to this blueprint
# def : define function
# __init__ : A special function , reserved method for automatically 
# initializing new objects, you dont call this function directly rather
#  it is called when you create a new instance of the class

#self : self is automatically filled by python