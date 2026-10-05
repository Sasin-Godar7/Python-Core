# from datetime import datetime


# today = datetime.today()
# today_date = today.date()

# birth_date = input("Enter your Birthdate [yyyy-mm-dd] : ")

# actual_birthdate = datetime.strptime(birth_date,"%Y-%m-%d").date()

# date_diff = today_date - actual_birthdate

# #print age
# print(date_diff)  # shows days gap and time but(0:00:00)

# years = date_diff % 365









#     OTP

# from datetime import datetime, timedelta
# import time

# otp={
#     "value" : "123456"
# }
# now = datetime.now()
# print("present time now is ",now)

# otp["created_at"] = now

# # expire_time = now + timedelta(minutes=5)
# expire_time = now + timedelta(seconds=3)

# otp["expire_time"] = expire_time

# print(otp)


# time.sleep(5)


# # otp verification

# if otp["expire_time"] < datetime.now():
#     print("expired")
#     #message()
# else:
#     print("verified")    




# random  --------------

# import random
# user_num = 7 

# gen_rand = random.randint(1,10)
# print(gen_rand)
# if user_num == gen_rand:
#     print("siuuuuu !!!")
# else:
#     print(" no siuuu")  



import random
secret_num = random.randint(1,10)

life = 5

while life > 0:
    print("life remaining -> ",life)
    user_guess =int(input("Enter your guess number "))

    if user_guess == secret_num:
        print("you won the game")
        break
    else:
        life-=1
        if life == 0:
            print(" sorry you lost ")
            print("secret number is ",secret_num)
            break
        print("wrong guess ! try again")
        print("\n")

  