# 리스트에서 값의 존재 확인하기 : 키워드 in
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)
# 값이 없는지 확인
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 not in primes)
print(12 not in primes)


# 리스트 안의 리스트(Nested List)
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]
# 첫 번째 학생의 성적
print(grades[0])
# 세 번째 학생의 성적
print(grades[2])
# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])
# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])
# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)


# sort 메소드
# some_list.sort()는 새로운 리스트를 생성하지 않고 some_list를 정렬된 상태로 바꿔줌
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)


# reverse 메소드
# some_list.reverse()는 some_list의 원소들을 뒤집어진 순서로 배치함
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)


# index 메소드
# some_list.index(x)는some_list에서 x의 값을 갖고 있는 원소의 인덱스를 리턴
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))


# remove 메소드
# some_list.remove(x)는some_list에서 첫 번째로 x의 값을 갖고 있는 원소를 삭제
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)
