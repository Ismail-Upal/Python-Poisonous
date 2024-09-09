class Student:
    def __init__(self, name, cur_class, id):
        self.name = name
        self.id = id
        self.cur_class = cur_class
    
    def __repr__(self)->str:
        return f'student with name: {self.name}, class: {self.cur_class}, id:{self.id}'

class Teacher:
    def __init__(self, name, subject, id) ->None:
        self.name= name
        self.subject = subject
        self.id= id

    def __repr__(self) ->str:
        return f'Teacher: {self.name}, subject: {self.subject}'
    
class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers =[]
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id : {id}, extra money {fee-6500}'
    
    def __repr__(self) -> str:
        print('welcome to ', self.name)
        print('-------OUR Teachers_-----')
        for teacher in self.teachers:
            print(teacher)
        print('------OUR students-------')
        for student in self.students:
            print(student)
        return 'all done for nowd'

# ranbee = Teacher('Douran beer', 'Algorithm', 101)
# alia = Student('alia torkari', 9, 1)

# print(ranbee)
# print(alia)

phitron = School('phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('airshh', 7000)
phitron.enroll('vaijan', 900000)

phitron.add_teacher('tom_cruise', 'algo')
phitron.add_teacher('decap','ds')
phitron.add_teacher('aj', 'database')

print(phitron)