# while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 코드를 작성해 보세요.

sum = 0
num = 1
while num < 1000:
    if num % 2 ==0 or num % 3 == 0:
        sum += num
    num += 1
print(sum)

# 모범답안
i = 1
total = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        total += i
    i += 1

print(total)
