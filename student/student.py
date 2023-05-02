class Student:

    def __init__(self, name):

        self.name = name
        self.cijfers = []

    def add_grade(self, cijfer):

        self.cijfers.append(cijfer)
    
    def average(self):
        return sum(self.cijfers) / len(self.cijfers)
    

if __name__=="__main__":
    name = input("Student name? ")
    student = Student(name)
    while True:
        grade = int(input("Grade? "))
        student.add_grade(grade)
        print("Average is", student.average())
        keep_going = input('Want to continue?: (y/n)')
        if keep_going == 'n':
            break