

class User:
    def __init__(self,name,password,email):
        self.name = name
        self.password = password
        self.email = email



    def show_info(self):
        print("name is :",self.name)
        print("password is :",self.password)
        print("email is :",self.email)
      
    
    def save(self):
             print("saving to database")
             print("succesfully saved !! ")

    @staticmethod
    def check_password(password):
        if len(password)<8:
                raise Exception("password must me more the 8 character")  

        has_special_char = ""


User1 =  User("Sasin Godar","sassu@123","sasin@gmail.com")

User.show_info(User1)       