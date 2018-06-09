#Cyclic Rotation: Shift the elements of Multi Value Container A to the right with R shifts.

"""def cyclicRotation(x,y):
    n = len(x)             
    z = list(range(0,n))                          #Method1
    for i in range(n):
        z[(i+y)%n] = x[i]
    return z"""

def cyclicRotation(x,y):
    n = len(x)
    if y==0:
        return x
    else:
        temp = x[n-1]                              #Method2
        for i in range(n-1,0,-1):
            x[i] = x[i-1]
        x[0] = temp
        return cyclicRotation(x,y-1)

x = []
y = int(input("Enter the shift amount: "))
n = int(input("How many elements you want to insert in the list? "))

for i in range(0,n):
    z = int(input("Enter a number: "))
    x.append(z)

print("List before shifting:",x)
print("List after shifting:",cyclicRotation(x,y))
