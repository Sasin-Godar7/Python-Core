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






#sets in python-----------------------------------------------
#set in pythin is the collection if the unordered itams
#sets in python store only value and        (set=mutuable  &&& element of set = immutable)

# set = { 1 ,2,3,3,3,2,"hello","world","hello","Hello"}  

# print(set)   # unorderly print the set and print only once a value
# print(type(set))
# print(len(set))   #also ignore the duplicate value and count once

# null_set = { }   # this is empty disctionary
# emp_set = set( )    # this is empty set
# print(type(emp_set))


#     ------ methods of set

collection = set()

collection.add(1)    # add an elements 
collection.add(2)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add("sasin")
collection.add((99,88,77))
# collection.add([99,88,77])   #  cant add list

print(collection)

collection.remove(4)  # remove any element 
print(collection)

collection.pop()  # removes any random value
print(collection)

collection.clear()  # empities the set
print(collection)
print(len(collection))


set1 = { 6 ,7 ,8 }
set2 = {8,9,10}

print(set1)
print(type(set1))
print(set1.union(set2))


print(set2)
print(set1.intersection(set2))
