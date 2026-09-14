# to check the condition and execute accordingly 

#( if elif else)

# if condition

a = 10
b=9
if(a>b):
    print("a is greater")


s = 3
t=77
if(s>t):
    print("s is greater") 
else:
    print("t is greater")       


x = 12
y=90
if(x>y):
    print(" x is greater")   # indetation ( require space )
elif(a==b):
    print(" both are equal ")
else:
    print(" y is greater")


# nesting

age = 87
if(age<18):
    print("cannot drive too small")
elif(age>=18 and age<=80):
    print("can drive")
else:
    print("cannot drive to old")      
