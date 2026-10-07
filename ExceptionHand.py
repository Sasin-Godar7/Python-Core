# exception is a error that terminates the further program

# the handeling technique use to handle the error/exception is called exception handeling

# if asking input int but user gives another dtype then it'll be valueError 


# try:
#     user_input = int(input("enter the number: "))
# except ValueError:   
#     print("invalid daatatype")
# else:
#     print(user_input)    

# print("end ho hai")





# iterator

# nums = [1,2,3,4]
# for val in nums:
#     print(val)


# nums = [1,2,3,4]
# print(nums.__iter__)

# a = 1
# print(a.__iter__)   # cant perform

# nums_iter = iter(nums)

# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# # print(next(nums_iter))    #stopIteration ( error )



# while True:
#     try:
#         num = print(next(nums_iter))
#     except StopIteration:
#         break
#     else:
#         print(num)






# Generator

def crange(stop):
    start = 0
    while start < stop:
        print(start)
        #return start    # this is return the start (0) and terminate

        yield start  #pause until mext func call
        start +=1

crange_gen = crange(10)

print(next(crange_gen))
print(next(crange_gen))
print(next(crange_gen))
print(next(crange_gen))
print(next(crange_gen))