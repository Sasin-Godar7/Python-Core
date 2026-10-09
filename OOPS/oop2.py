
class User:


    def __init__(self,name,password,email):
        self.name = name
        self.__password = password
        self.email = email


    def __str__(self):
        # return "User Object"
        return f"{self.name}"
     
    @property
    def password(self):
        return "*"*len(self.__password)

    def show_info(self):
        print("name is :",self.name)
        print("password is :",self.password)
        print("email is :",self.email)
      
    
User1 =  User("Sasin Godar","sassu@123","sasin@gmail.com")

# User.show_info(User1)  



print(User1.password)


