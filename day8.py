# class Student:
#     data member
#     a=10
#     b=20
    # self is default argument
#     def add(self):
#         print(self.a+self.b)
# object reation
# obj=Student()
# obj.add()
# print(obj.a)
# class NewClass:
#     def __init__(self): #constructor declaration (called automatically)
#         print("constructor always execute first")
#     def show(self): #member function inside of class(it is user define function)
#         print('welcome to class level programming')
# obj=NewClass() #creating a object
# print(obj)
# obj.show()
# obj1=NewClass()

# class Hod:
#     def __init__(self):
#         self.name="prashant"
#         self.age=53
#         self.empid=1001
#     def info(self):
#         print("My name is:",self.name)
#         print("My age is:",self.age)
#         print("My employee id is:",self.empid)

# obj=Hod()
# obj.info()

# class Hod:
#     def __init__(self ,name,age,rollno):
#         self.name=name
#         self.age=age
#         self.rollno=rollno
#     def show(self):
#         print("name=",self.name)
#         print("age=",self.age)
#         print("roll no=",self.rollno)

# obj=Hod('sakshii',21,76)
# obj.show()
# class Student:
#     def __init__(self):
#         self.s_name="prashant"#instace varialbe
#         self.s_rollno=53
#         self.s_branch="EC"
#     def getdata(self):#instance method
#         self.s_mb=223346487629#instance variable
# obj=Student()
# obj.getdata()
# obj.s_branch="EC"
# print(obj.__dict__)
# print(obj.s_mb)


# class New:
#     def __init__(self):
#         self.a=10
# Obj1=New()
# Obj2=New()
# Obj3=New()
# Obj1.a=20
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)


# class New:
#     a=10
#     def __init__(self):
#         self.name="sakshi"
# obj1=New()
# obj2=New()
# obj3=New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a=20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# class Student:
#     def __init__(self ,name,rollno,mob):
#         self.name=name
#         self.rollno=rollno
#         self.mob=mob
#     def display(self):
#         print(self.name," ",self.rollno," ",self.mob)
# stud=Student("prashant",1001,9846475347)
# stud.display()

#static method
# class Student:
#     by using class name we can access static method
#     @staticmethod  #decorator
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail=",firstname,lastname)
#     @staticmethod
#     def contact_detail(mobile_no,rollno):
#         print("your contact datail=",mobile_no,rollno)
# Student.get_personal_detail("sakshi","rengate")
# Student.contact_detail(74534563495739,1001)

  #single level inheritance
# class College:
#   def college_name(self):
#     print("Modern collage")
# class Student(College):
#     def Student_info(self):
#         print("Name:madhura kivande")
#         print("Branch:ece")
# obj=Student()
# obj.college_name()
# obj.Student_info()

# class College:
#   def college_name(self):
#     print("Modern collage")
# class Student(College):
#     def Student_info(self):
#         print("Name:madhura kivande")
#         print("Branch:ece")
# class Exam(Student):
#     def subject(self):
#         print("subject1:Designer Engeneering")
#         print("subject2:Math")
#         print("subject3:C-language")

# obj=Exam()
# obj.college_name()
# obj.Student_info()
# obj.subject()
# class SubjMarks:
#     math=int(input("Enter the marks of math:"))
#     DE=int(input("Enter the marks of design engeneering:"))
#     c=int(input("Enter the marks of c programming:"))
#     english=int(input("Enter the marks of english:"))
# class PractMarks:
#     pract=int(input("Enter the practical marks:"))
# class Result(SubjMarks,PractMarks):
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.pract>=20:
#             print("pass")
#         else:
#             print("fail")
# obj=Result()
# obj.total()

class Principal:
    def role(self):
        print("I am managing all activity of collage")
class Dean:
    def role(self):
        print("I am decision making person")
class Hod:
    def role(self):
        print("I am handle the faculties")
class Faculity:
    def role(self):
        print("I am managing all activity of collage")
def func(obj):
    obj.role()
campus=[principal






























