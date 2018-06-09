#Integer N represents the no. of candies arranged in a circle, numbered from 0 to N-1.
#You will eat a candy and leave the wrapper.
#You shall begin eating and candy number 0. Then you omit the next M-1 candy or wrappers on the circle, and eat the following one.
#If you ate candy number X, then you will next eat the candy with number (X+M) modulo N (Remainder of division)
#You stop eating when you encounter an empty wrapper.
#For example, given N=10, M=4
#You will eat the following candy: 0,4,8,2,6.
#Your answer should be 5, i.e. count the number of candies you ate.

def candy(n,m):
    count = 0
    ls = list(range(0,n))
    i = 0
    while ls[i] != 'x':
        count += 1
        #print(ls[i], end=' ')
        ls[i] = 'x'
        i = (i+m)%n
        #print(ls) 
    return count

n = int(input("Enter the amount of candies: "))
m = int(input("Enter the shifting amount: "))

print("No. of candies eaten:", candy(n,m))