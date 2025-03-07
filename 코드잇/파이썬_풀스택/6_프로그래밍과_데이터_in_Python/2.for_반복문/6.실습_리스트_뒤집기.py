# numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 보세요!

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

a = len(numbers)
for i in range(a // 2):
    
    temp = numbers[i]
    numbers[i] = numbers[a - (i + 1)]
    numbers[a - (i + 1)] = temp

print("뒤집어진 리스트: {}".format(numbers))


numbers = [2, 3, 5, 7, 11, 13, 17, 19]


# 모범답안1 : swap
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("뒤집어진 리스트: " + str(numbers))


# 모범답안2 : 튜블 이용
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산    
    right = len(numbers) - left - 1

    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))
