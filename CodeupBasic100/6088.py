start,d,num = input().split()

start = int(start)
d = int(d)
num = int(num)

for i in range(0,num - 1):
    start += d
   
print(start)