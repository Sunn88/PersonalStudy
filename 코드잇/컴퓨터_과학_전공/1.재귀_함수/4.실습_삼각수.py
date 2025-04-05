# 0보다 큰 정수 n을 파라미터로 받아서 n번째 삼각수를 리턴하는 함수 triangle_number()를 작성해 주세요. 
# 함수 안에서 for문과 while문은 사용하시면 안 됩니다!

def triangle_number(n):
    # 베이스 케이스
    if n == 1:
        return 1

    # 재귀 케이스
    return triangle_number(n - 1) + n


# 테스트 코드
for i in range(1, 11):
    print(triangle_number(i))
