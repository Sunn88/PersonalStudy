# main.py 파일의 count_matching_numbers() 함수를 작성하세요. 
# 이 함수는 참가자가 뽑은 6개의 번호 리스트와 
# 당첨 번호 6개의 리스트 중 몇 개의 숫자가 일치하는지 알려 주는 함수입니다. 
# 파라미터로 리스트 numbers와 리스트 winning_numbers를 받고, 
# 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.

def count_matching_numbers(list_1, list_2):
    s1 = set(list_1)
    s2 = set(list_2)
    same_number = s1&s2
    return len(same_number)

# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))



# 모범답안
def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count


# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))
