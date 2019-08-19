n=6
a=[]
s=0

for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i]%2==0:
        s=s+a[i]

print(s)
