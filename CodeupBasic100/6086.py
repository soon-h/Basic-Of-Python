flag = int(input())
n = 1
sum = 0
while True:
    if sum >= flag:
        print(sum)
        break
    else:
        sum += n
        n += 1