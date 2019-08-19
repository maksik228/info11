n=6
a=[None]*n
s=0

for i in range(n):
    a[i]=int(input())
for i in range(n):
    if a[i]%2==0:
        s=s+a[i]

print(s)
