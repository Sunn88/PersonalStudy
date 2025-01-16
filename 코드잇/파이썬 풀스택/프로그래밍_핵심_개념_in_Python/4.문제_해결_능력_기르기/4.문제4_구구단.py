# while문을 사용해서 구구단을 출력하는 코드를 작성해 봅시다.

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print("{} * {} = {}".format(i, j, i * j))
        j += 1
    i += 1