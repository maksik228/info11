# до­пус­ка­ет­ся также
# ис­поль­зо­вать две
# це­ло­чис­лен­ные пе­ре­мен­ные j, min

a = []
n = 5
for i in range(0, n):
    a.append(int(input()))

min1=1000
for i in range(n):
    if a[i]>=20 and a[i]<min1:
        min1=a[i]
print(min1)







