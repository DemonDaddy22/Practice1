#Create a function which returns a list with the strings in sorted order
#Condition: Group all the strings that begin with 'x' first.

def fun1(ls):
    ls1 = []
    ls2 = []
    for i in ls:
        if i.startswith('x'):
            ls1.append(i)
        else:
            ls2.append(i)
    ls1.sort()
    ls2.sort()
    ls1.extend(ls2)
    return ls1

ls = []
n = int(input("Enter the number of elements you want to enter: "))

for i in range(0,n):
    st = input("Enter a string: ")
    ls.append(st)

print("List before sorting:",ls)
print("List after sorting:",fun1(ls))