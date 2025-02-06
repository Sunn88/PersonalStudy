#공통점
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabet_list[0])
print(alphabet_list[1])
print(alphabet_list[4])
print(alphabet_list[-1])
print(alphabet_list[0:5])
print(alphabet_list[4:])
print(alphabet_list[:4])

alphabet_string = 'ABCDEFGHIJ'
print(alphabet_string[0])
print(alphabet_string[1])
print(alphabet_string[4])
print(alphabet_string[-1])
print(alphabet_string[0:5])
print(alphabet_string[4:])
print(alphabet_string[:4])


str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2
print(str_3)

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)


my_list = [2, 3, 5, 7, 11]
print(len(my_list))

my_string = 'Hello world!'
print(len(my_string))



#차이점
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

name = 'codeit'
name[0] = 'C'
#print(name)
#문자열은 리스트와 달리 수정 불가