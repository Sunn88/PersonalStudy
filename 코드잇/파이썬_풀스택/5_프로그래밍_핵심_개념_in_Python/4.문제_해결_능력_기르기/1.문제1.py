# while문과 if문을 활용하여, 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.

num = 1
while num <= 100:
    if num%8 == 0:
        if num%12 != 0:
            print(num)
            num += 1
        else:
            num += 1
    else:
        num += 1

# 모범답안
i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
    i += 1