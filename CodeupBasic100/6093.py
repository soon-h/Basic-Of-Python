num = int(input())
a = input().split()

for i in range(num):
    a[i] = int(a[i])

for j in range(num):
    print(a[num-1-j])
