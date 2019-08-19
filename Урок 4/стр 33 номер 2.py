a=[]
n=6

for i in range(n):
    a.append(int(input()))
max1=-100
max1_num=-1
for i in range(6):
    if a[i]>max1:
        max1=a[i]
        max1_num=i

print(max1)
print(max1_num)

