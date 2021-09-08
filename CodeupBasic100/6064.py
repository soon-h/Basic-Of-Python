a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if (a > b):
    if b > c:
        print(c)
    else:
        print(b)
elif a < b:
    if a > c:
        print(c)
    else:
        print(a)
elif a == b:
    if a > c:
        print(c)
    elif a < c:
        print(a)
    else:
        print(a)