# 0보다 큰 정수 n을 파라미터로 받아서 n번째 피보나치 수를 리턴하는 함수 fib()를 작성해 주세요.

def fib(n):
    # 베이스 케이스
    if n <= 2:
        return 1

    # 재귀 케이스
    return fib(n - 2) + fib(n - 1)


# 테스트 코드
for i in range(1, 16):
    print(fib(i))