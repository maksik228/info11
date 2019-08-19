a=int(input())
s=0
k=0
min1=100
max1=-100
min1_num=0
max1_num=0
i=1

while a!=0:
    if a%10==7:
        s=s+a
        k=k+1
        i=i+1
        if a<min1:
            min1=a
            min1_num=i
        if a>max1:
            max1=a
            max1_num=i

    a=int(input())

print(s)
print(k)
print(min1)
print(max1)
print(min1_num)
print(max1_num)
