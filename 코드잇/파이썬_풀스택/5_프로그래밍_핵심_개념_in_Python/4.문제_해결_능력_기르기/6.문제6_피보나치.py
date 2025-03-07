# 피보나치 수열의 첫 50개 항을 차례대로 출력하는 코드를 작성해 보세요.

a = 0
b = 1
c = 0
cnt = 1
while cnt <= 50:
    print(b)
    c = a
    a = b
    b = b + c
    cnt += 1

# 모범답안
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1
