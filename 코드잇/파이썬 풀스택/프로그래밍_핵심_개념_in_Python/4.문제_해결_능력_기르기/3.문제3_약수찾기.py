# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 코드를 작성해 보세요.

num = 1
cnt = 0
while num <= 120:
    if 120 % num == 0:
        print(num)
        cnt += 1
    num += 1
print("120의 약수는 총 {}개입니다.".format(cnt))

# 모범답안
N = 120
i = 1
count = 0

while i <= N:
    if N % i == 0:
        print(i)
        count += 1
    i += 1

print("{}의 약수는 총 {}개입니다.".format(N, count))
