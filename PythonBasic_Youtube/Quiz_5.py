# 예외코드를 이용한 치킨집 자동 주문 시스템

# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError 로 처리
# 출력 메시지 : "잘못된 값을 입력하였습니다."

# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨양은 10마리로 한정
# 치킨 소진시 사용자 정의 에러[SoldoutError]을 발생시키고 프로그램 종료
# 출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

class SoldOutError(Exception):
    def __init__(self):
        pass

try:
    chicken = 10
    waiting = 1
    while (True):
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? :"))
        if order <= 0:
            raise ValueError
        if order > chicken:
            print("재료가 부족합니다!")
        else:
            print("[대기 번호 : {}] {} 마리 주문이 완료되었습니다.".format(waiting,order))
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise SoldOutError
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except SoldOutError:
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")