'''Suppose you want to write a program which has to keep track of the teachers and students in a college. 
They have some common characteristics such as name, age and address. 
They also have specific characteristics such as salary, courses and leaves for teachers and,
 marks and fees for students.'''

class SchoolMember:
    
    def __init__(self, name, age):

        # Initialise techers and students:

        
        self.name = name
        self.age = age
        
    
    def tell(self):
        print('Name : {} , Age : {}'.format(self.name, self.age))


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        
        self.salary = salary

        SchoolMember.__init__(self, name, age)

        print('Initialised Teacher : {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {:d}'.format(self.salary))


class Student(SchoolMember):

    def __init__(self, name, age, grade):
        
        self.grade = grade

        SchoolMember.__init__(self, name, age)                # Importing from SchoolMember

        print('Initialised Student : {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)                              # Running code in Student

        print('Grade: {:d}'.format(self.grade))

Ash = Student('Ash', 20, 88)
Bob = Teacher('Bob', 45, 50000)


print()

members = [Ash, Bob]

for member in members:
    member.tell()


