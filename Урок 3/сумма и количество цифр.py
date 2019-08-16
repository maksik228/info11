a=int(input())
s=0
k=0
while a>0:
    dig=a%10
    s=s+dig
    k=k+1
    a=a//10
print(s)
print(k)
