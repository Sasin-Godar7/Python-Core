

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
    def check_password(password,name):
        if len(password)<8:
                raise Exception("password must me more the 8 character")  

        has_special_char = any(not char.isalnum() for char in password)

        if password.isalnum() or password.digit() or not has_special_char:
            raise Exception("password must be in alphanumerix + special character")

        if name.lower() or password.lower():
             raise Exception("password mustnot be personal info")

        return True


User1 =  User("Sasin Godar","sassu@123","sasin@gmail.com")

User.show_info(User1)   
# print(dir(User1))


User1.save()