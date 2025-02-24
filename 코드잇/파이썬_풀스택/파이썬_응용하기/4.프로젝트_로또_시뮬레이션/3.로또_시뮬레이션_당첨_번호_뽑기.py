# main.py 파일의 draw_winning_numbers() 함수를 작성하세요. 
# 이 함수는 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다. 
# 일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다. 
# 앞서 정의한 generate_numbers() 함수를 잘 활용하면, 함수를 간결하게 작성할 수 있습니다.

from random import randint


def generate_numbers(n):
    numbers = set()  # 중복을 방지하기 위해 집합 사용
    while len(numbers) < n:
        numbers.add(randint(1, 45))  # 1~45 사이의 난수 생성
    
    return list(numbers)


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


# 테스트 코드
print(draw_winning_numbers())