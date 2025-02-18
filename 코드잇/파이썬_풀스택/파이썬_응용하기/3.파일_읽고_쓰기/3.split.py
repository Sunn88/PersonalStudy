my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))

full_name = "Kim, Yuna"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]
print(first_name, last_name)

numbers = "     \n\n    2     \t    3     \n    5  7  11  \n\n".split()
print(numbers[0] + numbers[1])
# split을 사용했을 때는 문자열로 나옴
print(int(numbers[0]) + int(numbers[1]))


with open('data/chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0
    
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)
