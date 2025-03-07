from random import randint

def generate_numbers(n):
    numbers = set()  # 중복을 방지하기 위해 집합 사용
    while len(numbers) < n:
        numbers.add(randint(1, 45))  # 1~45 사이의 난수 생성
    
    return list(numbers)

# 테스트 코드
print(generate_numbers(6))



# 모범답안
def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers