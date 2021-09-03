#표준 체중을 구하는 문제
def std_weight(height,gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 177
gender = "남자"
weight = round(std_weight(height / 100,gender),2)

print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height,gender,weight))

def astd_weight(height,gender):
    weight = round(std_weight(height / 100,gender),2)
    if gender == "남자":
        print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height,gender,weight))
        return height * height * 22
    else:
        print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height,gender,weight))
        return height * height * 21

astd_weight(168,"여자")
astd_weight(180,"남자")