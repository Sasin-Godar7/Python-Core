# input 2 num and display their sum mul div mod

# a = int(input("enter the first number :"))
# b= int(input("enter the scond number :"))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)


#wap to input side of square and print area

# l = int(input("enter the length :"))
# ln = float(input("enter the length :"))
# print("area of square is :",l*l)
# print("area of square is :",ln*ln)



#wap to take input 2 in num ie a and b 
#print true if a greate than b or equal to b  else print false

# a = int(input("enter the first number :"))
# b = int(input("enter the second number :"))

# if(a>=b):
#     print(True)
# else:
#     print(False)    



# wap to input user name and print its lenght

# name = input("Enter your name :")
# nlen = len(name)
# print("the lenght of the name is :" , nlen)

#wap to find the occurance of " $ " in string
# name = " hi my $name is $ sasin i am $ good $ boy"
# print(name.count("$"))


#wap to check enter number is evem or odd

# num = int(input("enter any number"))
# if(num%2==0):
#     print("number is even")
# else:
#     print("number is odd")    



#wap to find greatest among 3 entered num
# a = int(input("enter number a :"))
# b = int(input("enter number b:"))
# c = int(input("enter number  c:"))

# if(a>b and a>c):
#     print("a  is the greater")
# elif( b>c):
#     print("b is the greatest")   
# else:
#     print("c is the greatesr")


#wap to find greatest among 4 entered number

# a = int(input("enter number a :"))
# b = int(input("enter number b:"))
# c = int(input("enter number  c:"))
# d = int(input("enter number  d:"))

# if(a>=b and a>=c and a>=d):
#     print("a is greaest")
# elif(b>=c and b>=d):
#     print("b is the greates")
# elif(c>=d):
#     print(" c is the greatest")    
# else:
#     print(" d is the greatest")        





# wap to ask the user their 3 fav movie and store them in a list

# movi1 = input("enter your movie1 ")
# movi2 = input("enter your movie2 ")
# movi3 = input("enter your movie3 ")

# movies = [movi1,movi2,movi3]
# print("ypur fav movies are ")
# print(movies)
# print(type(movies))



# wap tp check if a list contain palindrome element ( hint use copy() method)

# list1 = [ 1 ,2, 3, 2, 1] # palindrome
# # list1 = ["racecar"] # palindrom

# # list1 = [ 1 ,2, 3, 2, 1,8] doesnot palindrome
# list2 = list1.copy()
# list2.reverse()
# if(list2 == list1):
#     print("list contain the palindrom element")
# else:
#     print("doesnot contain palindrome element")  
  



# wap to count the numebr of "A" grade in the following tuple

grade = ("c","d","a","a","d","b")
print(grade.count("a"))

# wap to store the avove value in list and sort them a ->d

ligrade = []
ligrade.append(grade)
ligrade.sort()
print(ligrade)
print(type(ligrade))
