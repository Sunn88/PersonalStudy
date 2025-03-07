#return문의 역할 : (함수가) 무언가를 돌려줌 + 함수를 즉시 종료시킴

def square(x):
    return x * x
print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후") #dead code

#함수 즉시 종료하기
#값 돌려주기