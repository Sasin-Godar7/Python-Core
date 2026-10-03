

# wrapping data and function into a single unit(object)  is encapsulation

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
