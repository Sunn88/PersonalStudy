# 사전에 있는 값을 목록으로 출력
my_family={
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}

print(my_family.values())
print('이지영' in my_family.values())
print('성태호' in my_family.values())

for value in my_family.values():
    print(value)

print(my_family.keys())
for key in my_family.values():
    print(key)

for key in my_family.values():
    value = my_family[key]
    print(key, value)

# 동시에 가져오기
for key, value in my_family.items():
    print(key, value)