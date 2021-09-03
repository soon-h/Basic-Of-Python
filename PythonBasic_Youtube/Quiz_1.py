from math import perm
from random import *
count = 1
sum = 0
while count <= 50:
    person = randint(5,50)
    if 5 <= person and person <= 15:
        print("[o] {}번째 손님 (소요시간 : {}분)".format(count,person))
        sum += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(count,person))
    count += 1
print("총 탑승 승객 :"+str(sum)+"명")
