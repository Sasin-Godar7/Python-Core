
# class is a blueprint for object
# object is a real world element 

# class Student:
#     name="sasin"

# s1  = Student()
# # print(s1)
# print(s1.name) 

# class Car:
#     color="red"
#     brand="lambo"
# c1 = Car()
# print(c1.color)    
# print(c1.brand) 



 # -- init() function--
# all classes have __intit__() which is always executed when the object is initiated
# 
# # creating class 

# class Student:
#     name="sasin"
#     def __init__(self):
#             print("adding new student in database")

# s1 = Student()

class Student:

    collage_name = "abc collage" # class attribut(for all)

    # default constructor
    def __init__(self):
        pass


     #parameterized constructor       
    def __init__(self,name,marks):
        self.name= name    # obj attribute > class attr
        self.marks = marks
       

s1 = Student("sasin",99)
print(s1.name,s1.marks)

s2 = Student("krishna",34)
print(s2.name,s2.marks)

print(s2.collage_name)

