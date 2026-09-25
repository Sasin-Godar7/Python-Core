 
# recursion is a function that call it self repeatedly

def fact(n):
    if(n==1 or n==0):
        return 1 
    return fact(n-1)* n

res = fact(3)
print(res)