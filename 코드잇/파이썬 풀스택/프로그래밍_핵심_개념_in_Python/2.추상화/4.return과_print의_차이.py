def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

print_square(3)
get_square(3)
print(get_square(3))
print(print_square(3)) #return이 없으면 none 반환


def first():
    message = "코드잇"
    return message

def second():
    message = "codeit"
    print(message)

def third():
    message = None
    print(message)

# 테스트 코드
print(first())
second()
print(third())