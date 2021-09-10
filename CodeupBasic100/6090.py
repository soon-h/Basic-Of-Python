start,m,d,num = input().split()

start = int(start)
d = int(d)
num = int(num)
m = int(m)

for i in range(0,num - 1):
    start = start * m + d
   
print(start)