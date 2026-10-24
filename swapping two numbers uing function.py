a=10
b=20
temp=0
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
add=swap(a,b)
print(add)
