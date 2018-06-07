num = int(input("Enter a number: "))
res1 = ""
res2 = ""
rem = 0
count = 0
num1 = num

while(num>0):
    rem = num%2
    res1 += str(rem)
    num = num//2

m = len(res1)
for i in range(-1,-m-1,-1):
    res2 += res1[i]
    #print (res2)
n = len(res2)
print("Input number:", num1)
print("Required Binary Output:", res2)

leng = []
leng1 = []
l = 0

for i in range(n):
    #print (res2[i])
    if res2[i] == '1':
        count += 1
        if count==1:
            index = i
        elif count==2:
            l = i-index-1
            leng.append(l)
            count = 1
            index = i
    else:
        continue

leng1 = leng
leng.sort();
k = len(leng)

if k!=0:
    print("Minimum gap between 2 consecutive 1s:", leng[0])
    print("Maximum gap between 2 consecutive 1s:", leng[k-1])
else:
    print("No is either zero or contains only one 1!")
