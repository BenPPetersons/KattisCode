n = int(input())
a,b = 0,0

values = set(map(int, input().split()))

if len(values)!= n:
    a = 0 
    b = 6**(4-n)
elif n == 1:
    a = 60
    b = 156
elif n == 2:
    a = 12
    b = 24
else:
    a = 3
    b = 3
print(a,b)
