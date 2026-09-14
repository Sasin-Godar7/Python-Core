
#escape sequence

# str1 = " this is a string . we are writing in python"
# print(str1)
# str2 = " this is a string .\nwe are writing in python"
# print(str2)
# str3 = " this is a string .\t we are writing in python"
# print(str3)

# print("hello" +" "+ "world")
# print(str1 + str3)

# print(len("sasin" + " "+"Godar"))  # determine the lenght  ( space also count )


#indexing
#--> index also starts from the 0 and all the  special char also gets the indexing ( we can acces but not modify)

# str = "Sasin Godar"
# print(str[0] + " " + str[5]+" " + str[8])


#slicing

#----->> accesing parts of string( tukda banaunu)

# str = "Sasin Godar"
# print(str[0:4] + " " + str[5:len(str)])
# print(str[0:]) # [0:last]
# print(str[:11])  #[start:11]

#negative slicing

# str = "Sasin Godar"
# print(str[-11:-1]  )
# print(str[-8:-5])




str = "my name is sasin godar"
print(str.endswith("dar")) # true
print(str.endswith("asin"))#false

#print(str = str.capitalize()) # captalixe the first letter

print(str.replace("s","i"))  # replace the old with new one

print(str.find("y")) # 1 index

print(str.count("sasin")) # counts how many time repeate
print(str.count("s"))