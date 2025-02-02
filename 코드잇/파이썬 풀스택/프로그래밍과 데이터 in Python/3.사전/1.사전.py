# 사전(dictionary)
# key-value pair(키-값 쌍)

my_dictionady={
    5: 25,
    2: 4,
    3: 9
}

print(type(my_dictionady))
print(my_dictionady[3])

# 키 추가
my_dictionady[9] = 81
print(my_dictionady)

# 사전에는 순서라는 개념이 없음
# list의 index는 정수형이지만, 사전은 정수형일 필요가 없음
my_family={
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}