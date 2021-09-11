num = int(input())
a = input().split()

for i in range(num):
    a[i] = int(a[i])

a.sort()

print(a[0])