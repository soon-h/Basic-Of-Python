many = int(input())

a = input().split()
b = input().split()
c = input().split()
d = input().split()
e = input().split()

for k in range(2):
    a[k] = int(a[k])
    b[k] = int(b[k])
    c[k] = int(c[k])
    d[k] = int(d[k])
    e[k] = int(e[k])

for i in range(1,20):
    for j in range(1,20):
        if i == int(a[0]) and j == int(a[1]):
            print(1,"",end="")
        elif i == int(b[0]) and j == int(b[1]):
            print(1,"",end="")
        elif i == int(c[0]) and j == int(c[1]):
            print(1,"",end="")
        elif i == int(d[0]) and j == int(d[1]):
            print(1,"",end="")
        elif i == int(e[0]) and j == int(e[1]):
            print(1,"",end="")
        else:
            print(0,"",end="")
    print("\n")

