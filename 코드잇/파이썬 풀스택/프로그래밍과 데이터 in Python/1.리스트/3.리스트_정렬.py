numbers = [19, 13, 2, 5, 3, 11, 7, 17]

new_list = sorted(numbers) # 정렬 -> 기존 리스트를 건드리지 않고, 정렬된 새로운 리스트를 만듦
new_list2 = sorted(numbers, reverse=True) # 역정렬
print(new_list)
print(new_list2)

numbers.sort() # 리턴 값이 없음, 리스트 자체를 정렬함

# sorted : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
# sort : 아무것도 리턴하지 않고, 기존 리스트를 정렬

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
num = 0
while num < len(greetings):
    print(greetings[num])
    num += 1