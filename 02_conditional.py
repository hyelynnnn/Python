# if 조건:
#     코드
# elif 조건:
#     pass
# elif 조건:
#     pass
# else:
#     pass


# 비교연산자
# 값 == 값 양쪽의 값이 서로 같다
# 값 != 값 양쪽의 값이 서로 다르다
# 값>값, 값<값, 값<=값, 값<=값, 크기 비교

a = 3
b = 5
print(a == 3) # True


# 조건연산자
# 1조건 and 2조건 (1조건이 만족하면서 2조건 만족)
# 1조건 or 2조건 (두 조건 중 하나만 만족하면)

if a == 3:
    print('조건이 참이면 출력')

    print(a==3 and b==5) #True
    print(a==3 or b!=5) #True 


"""
Q1. 사과는 냉장실에
    아이스크림은 냉동실에 넣어 주시고,
    나머지는 폐기처분 해주세요.
"""

변수 = "사과"

if 변수 == "사과":
    print("냉장실")
elif 변수 == "아이스크림":
    print("냉동실")
else:
    print("폐기처분")


