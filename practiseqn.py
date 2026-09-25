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

# grade = ("c","d","a","a","d","b")
# print(grade.count("a"))

# wap to store the avove value in list and sort them a ->d

# ligrade = []
# ligrade.append(grade)
# ligrade.sort()
# print(ligrade)
# print(type(ligrade))





# (1) store following word meaning in a python dictionary
# table="a peice of furniture" , "list of facts and figure "
# cat = " a small animal"

# dic ={
#     "table":["a peice of furniture , list of facts and fugure"],
    
#     "cat":"a small animal"
# }

# print(dic)
# print(type(dic["table"]))


# (2) you  are given a list of subjects, assume 1 classroom for 1 subjects then how manu
#classerroom are needed by all students

# "python","java","c++","python","javascript"
# "java","python","java","c++","c"

# subjects = { "python","java","c++","python","javascript" ,
#             "java","python","java","c++","c"
#               }

# print(len(subjects))
# print("so total calssroom rrquired is :",len(subjects))


#(3) wap to enter marks of 3 subject from user and add them in a dictionary.starts with and empty dic later fill one by one , use sub name = key and marks = value


# mark1 = int(input("enter the physics : "))
# mark2 = int(input("enter the chemistry: "))
# mark3 = int(input("enter the math : "))

# student = { }

# student.update({"physics":mark1})
# student.update({"chemistry":mark2})
# student.update({"math":mark3})

# print(student)
# print(type(student))
# print(student["chemistry"])



#(4) find a way to store 9 and 9.0 as a sepearate value( you can use built in datatypes)

# set ={9,9.0}  # print {9}
# set2 ={9.0 , "9.0"} 

# value = {
#     ("float",9.0),
#     ("int",9)
# }

# print(set2)
# print(value)




#   loopsss in pythonnn------------------
#usinf while loop

# 1) print numbers from 1 to 100

# i=1
# while i<=100:
#     print(i)
#     i+=1


#2) print numbers from 100 to 1
 
# i=100
# while i>=1:
#     print(i)
#     i-=1

#3)print the multiplication number of n 

# num = int(input("enter any number :"))
# i=1
# while i<=10:
#     print(num ,"*" , i , "=" , num*i)
#     i+=1


#4)print the elements of the list using the loops
# [1,4,9,16,15,67,78,89,677,100]

# nums = [1,4,9,16,15,67,78,89,677,100]
# heores = ["thor","ironman","superman","batman"]

# ix = 0
# while ix<len(heores):
#     print(heores[ix])
#     ix+=1

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx+=1


#5) search for the number x in the given tuple

# nums = [1,4,9,16,15,67,78,89,677,100]
# x = 1995

# i = 0
# while i<len(nums):
#     if(nums[i] == x):
#         print("found at index",i)

#     i+=1


#6) print the elements of the loop using for loop

# list = [1,2,4,6,44,22,333,332,112,2,2,3,3,7]
# for el in list:
#     print(el)


#7) search the elements x  from the tuple using for loop

# tup = [1,2,4,6,44,22,333,332,112,2,2,3,3,7]
# x = 2
# idx = 0
# for el in tup:
#     if(el==x):
#         print(" found on the index",idx)      
#     idx+=1



#using for and range

#8) print multiplication table of n 

# num = int(input("enter any number :"))
# for i in range(1,11):
#     print(num ,"*", i,"=",num*i)


#9) print from 100 to 1 
# for el in range(100,1,-1):
#     print(el)    




# wap to print sum first n numbers using while and for loop

# n = int(input("enter the number"))
# i=0
# sum = 0
# while i<=n:
#     sum+=i
#     i+=1
    
# print("sum is",sum)

# num = int(input("enter any number :"))
# add=0
# for i in range(n+1):
#     add+=i
#     i+=1
# print("sum is ",add)




# wap to print factorial of given   numbers using while and for loop

# n = int(input("enter number for factorial :"))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
#     i+=1
# print("factorial of",n , "is", fact)


# num = int(input("enter number for fact :"))
# facto = 1
# i=1
# while i<=n:
#     facto = facto * i
#     i+=1
# print("factorial of number is ",facto)    

    
    
# ---- from function -----

#1) wap to print the lenght of list (list is parameter)

# def calc_len(list):
#     print(len(list))

# list = [1,2,3,4,5,6,7,8,9,9,9,9]
# calc_len(list)


#2)wap to print the elementsof a list in a single line(list is a parameter)

# def calc_len(list):
#     for items in list:
#         print(items, end=" ")

# list = ["thor","sasin","lalala"]
# calc_len(list)


#3) wap to print the factorail of n ( n is the parameter)

# def calc_fact(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i
#     print("factorial of",num , "is", fact)
# calc_fact(4)


#4) wap to convert the usd to npr

# def  usd_to_npr(usd):
#     npr = usd * 132.5
#     return npr
# usd = float(input("enter the usd :"))
# print("the npr is :",usd_to_npr(usd))


#4) wap to convert to check prime or composote in function ( n is paramter)

def PrimeChecker(num):
 count = 0
 for i in range(1,num+1):
  if(num % i ==0):
   count +=1
 if (count==2):
  print("number is prime")
 else:
  print("number is compposite")

n = int(input("enter num to check"))
PrimeChecker(n)
