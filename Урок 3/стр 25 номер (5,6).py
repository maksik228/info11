a=int(input())
max1=-100
min1=100
s=0
k=0
while a > 0:
    dig=a%10
    s=s+dig
    k=k+1
    if dig > max1:
        max1 = dig
    if dig < min1:
        min1 = dig
    a = a//10
print(max1)
print(min1)
print(s/k)