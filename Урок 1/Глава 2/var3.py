import math

a=int(input())  #ввели а
b=int(input())
x=int(input())
y=int(input())
f=3*(a+b*b)/(x-7*math.sqrt(y))
print(f)
f=(2*a*a+5*b)/(math.fabs(x+y))
print(f)
f=2*(a+b*b)*(math.fabs(x-7*y))+a*b
print(f)


