# 0보다 큰 정수 n을 파라미터로 받아서 n의 각 자릿수의 합을 구해서 리턴하는 함수 sum_digits()를 작성해 주세요.

def sum_digits(n):
    # 베이스 케이스
    if n < 10:
        return n
    
    # 재귀 케이스
    return sum_digits(n // 10) + (n % 10)


# 테스트 코드
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))