# 리스트 : 변수에 값을 여러 개 저장하고 싶을 때 사용

numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

print(numbers)
print(names)


# 인덱싱(indexing)
print(names[1])
print(numbers[1] + numbers[3])

num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)

# 마이너스 인덱스
print(numbers[-1])
print(numbers[-2])

# 리스트 슬라이싱(list slicind) : 리스트 일부를 잘라오기
print(numbers[0:4])
print(numbers[2:])
print(numbers[:3])

new_list = numbers[:3]
print(new_list[2])

numbers[0] = 7
