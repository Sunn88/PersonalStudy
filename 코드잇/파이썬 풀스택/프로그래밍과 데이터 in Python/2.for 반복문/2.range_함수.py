for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

# 범위가 너무 커지면 반복하기 힘듦

# range : 파라미터 2개 버전
# for i in range(start, stop)
for i in range(3, 11):
    print(i)

# range : 파라미터 1개 버전
# for i in range(stop)
for i in range(10):
    print(i)

# range : 파라미터 3개 버전
# for i in range(start, stop, step)
for i in range(3, 17, 3):
    print(i)

# range 함수의 장점 : 간편함, 깔끔함, 메모리 효율성


# for문과 range 함수를 사용하여, numbers의 인덱스와 원소를 출력해 보세요.
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
for i in range(len(numbers)):
    print(i, numbers[i])