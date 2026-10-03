

# create a class student that takes name and marks of a three students as a argument in constructor.. then create a method to caculate the average


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def avg_Calc(self):
#         sum = 0
#         for val in self.marks:
#             sum+= val

#         print(self.name ,"your average is :",sum/3)   
           
# s1 = Student("Sasin", [88,88,88])
# s1.avg_Calc()

# s2 = Student("prabin", [99,99,99])
# s2.avg_Calc()

# s3 = Student("ashok", [20,76,76])
# s3.avg_Calc()






# create account class with 2 attribute - balamce and account number .creat a method for debit , credit and & print the current balance 

class Account:
    def __init__(self,balance,acc_no):
         self.balance = balance
         self.acc_no = acc_no
         print("your current balance of aac no ",self.acc_no," is : ",self.balance)

    def credit(self,amount):
        self.balance += amount
        print("current balance of ",self.acc_no," after credit is:", self.balance)

    def debit(self,amount):
        self.balance -= amount
        print("current balance of ",self.acc_no," after debit is: ",self.balance)


acc1 = Account(0,987654321)
acc1.credit(1000) 
acc1.debit(500)


acc2 = Account(1000,123456789)
acc2.debit(100)
acc2.credit(100)


