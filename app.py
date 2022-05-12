print(124+123)

이름 = "ㅁㄴㅇ 모노레일 스파크"
print(이름[0:2])

중고차 = ["K5", "white", [5000, 6000]]
중고차2 = {"brand" : "BMW", "model" : "520d"} # dictionary 자료형
print(중고차[2][0])
print(중고차2["brand"])

재고량 = -1
중고차재고 = ["K5", "BMW", "Tico"]

if 재고량 > 0 : 
    print("지금 주문가능합니다")

if "K6" in 중고차재고 : # 배열안에 글자가 있으면 참
    print("중고차 존재")
else : 
    print("주문불가능함 ㅅㄱ")
    # else if 는 elif로 사용

for i in range(0,10) : 
    print("BMW 있어요")

중고차들 = ["k5", "bmw", "tico"]
for i in 중고차들 : 
    print(i * 3)

def 인사하기() : 
    print("안녕하세요")
    print("반갑습니다")

def 모자(구멍, 구멍2) :
    print(구멍 + 구멍2)

모자(123, 123)

def 함수() :
    return 10

print(함수())

# 중고차.sort : 정렬
# 중고차.reverse : 거꾸로 출력
# 중고차.pop : 맨뒷자리 출력
# 파이썬 실행은 터미널 열고 그 폴더 안에서 python3 파일명(app.py) 치면 나옴