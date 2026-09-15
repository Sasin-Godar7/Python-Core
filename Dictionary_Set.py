# dictionary in python 

# dictionaries are used to store element in key:value pair
# they are unorderedd, mutable & dont allow the duplicate key

# info ={
#     "key":"value",
#        "name":"sasin",
#        "age":21,
#        "salary":56.88,
#        "topic": ("disc","set"),
#        "subjects":["java","c","python"]
# }

# print(info)
# print(type(info))
# print(info["key"])
# print(type(info["topic"]))
# print(type(info["subjects"]))

# null_disc={}
# print(null_disc)

#nested disctionary

# student = {
#     "name":"sasin godar",
#     "subjects":{
#         "physics":98,
#         "english":77,
#         "math":99.99,
#         "is_pass":True
#     },
#     "class":12
# }

# print(student)
# # print(student["name2"]) # error
# print(student["subjects"])
# print(student["subjects"]["is_pass"])
# print(student.keys())
# print(len(list(student.keys())))

# print(student.values())
# print(list(student.values())) # typecasing from disc to list


# print(student.items()) # returns all (key,value) pair in tuple

# print(student.get("class")) # used to get value by key

# student.update({"city" : "chitwan"})   #used to update in disc
# print(student)

# new_dis ={ "roll":1,"postion":"first"}
# student.update(new_dis)
# ---
# print(student)
