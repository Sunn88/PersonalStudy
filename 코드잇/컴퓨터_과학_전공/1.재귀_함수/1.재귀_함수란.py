# 재귀 함수 : 스스로를 호출하는 함수

# 핵심 : 하위 문제 파악 -> 큰 문제를 작은 문제로 나누기
# 베이스 케이스와 재귀 케이스 구하기

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n
    
print(factorial(4))