# x의 n제곱을 계산하고 반환하는 함수 power(x, n)를 작성해 주세요. 
# for문, while문, 거듭제곱 연산자 **는 사용할 수 없습니다!

# 이 문제는 이미 재귀적으로 정의되어 있습니다. 
# x^n(power(x, n))을 계산하려면 x^(n//2)(하위 문제 power(x, n // 2))가 필요하며, 
# n이 홀수인지 짝수인지에 따라 하위 문제의 결괏값을 약간 다르게 사용해서 재귀 함수를 작성해야 합니다.

# 이번 토픽에서 봤던 다른 재귀 문제들과 다르게 이 문제에서는 n이 하나씩 작아지지 않고 절반으로 줄어듭니다. 
# 재귀에서 하위 문제를 찾을 때 항상 인풋을 하나씩 줄이는 것은 아닙니다. 
# 메인 문제를 하위 문제로 나누는 방법은 문제 특성에 따라 다르기 때문에 다양한 알고리즘과 재귀 문제들을 접하면서 실력을 길러야 합니다.

def power(x, n):
    # 베이스 케이스
    if n == 0:
        return 1

    if n == 1:
        return x
   
    # 재귀 케이스
    temp = power(x, n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp


# 테스트 코드
print(power(2, 3))
print(power(5, 0))
print(power(17, 5))
print(power(3, 17))
print(power(4, 18))
