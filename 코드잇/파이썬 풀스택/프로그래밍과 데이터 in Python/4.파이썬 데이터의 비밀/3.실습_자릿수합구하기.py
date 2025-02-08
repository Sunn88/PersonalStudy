# 함수 sum_digit은 파라미터로 정수형 num을 받고, num의 각 자릿수를 더한 값을 리턴합니다.
# sum_digit 함수를 작성한다.
# sum_digit(1)부터 sum_digit(1000)까지의 합을 구해서 출력한다.

# 자리수 합 리턴
def sum_digit(num):
    num_str = str(num)
    sum = 0
    for i in range(len(num_str)):
        sum += int(num_str[i])
        i += 1
    return(sum)


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
total = 0
for i in range(1000):
    total += sum_digit(i+1)
print(total)


# 모범답안
# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)
    
    for digit in str_num:
        total += int(digit)

    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
digit_total = 0
for i in range(1, 1001):
    digit_total += sum_digit(i)

print(digit_total)
