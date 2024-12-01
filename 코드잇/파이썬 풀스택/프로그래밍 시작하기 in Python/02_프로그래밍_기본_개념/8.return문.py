#파라미터 : 함수에 넘겨 주는 값

def get_square(x):
    return 3 * 3

print(get_square(3))

def get_square2(x):
    return x * x

y = get_square2(3)
print(y)
print(get_square2(3) + get_square2(4))