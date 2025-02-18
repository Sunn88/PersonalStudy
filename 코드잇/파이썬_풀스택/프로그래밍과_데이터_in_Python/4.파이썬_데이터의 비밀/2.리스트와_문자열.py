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



#인덱싱(Indexing)
# 두 자료형은 공통적으로 인덱싱이 가능함
# 알파벳 리스트의 인덱싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0])
print(alphabets_list[1])
print(alphabets_list[4])
print(alphabets_list[-1])

# 알파벳 문자열의 인덱싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0])
print(alphabets_string[1])
print(alphabets_string[4])
print(alphabets_string[-1])



#for 반복문
#공통적으로 인덱싱이 가능하므로 for 반복문에서도 활용 가능
# 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:
    print(alphabet)

# 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:
    print(alphabet)



#슬라이싱(Slicing)
#두 자료형은 공통적으로 슬라이싱이 가능함
# 알파벳 리스트의 슬라이싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

# 알파벳 문자열의 슬라이싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])



#덧셈 연산
#두 자료형에게 모두 덧셈은 "연결"하는 연산
# 리스트의 덧셈 연산
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# 문자열의 덧셈 연산
string1 = '1234'
string2 = '5678'
string3 = string1 + string2
print(string3)



#len함수
#두 자료형은 모두 길이를 재는 len함수를 쓸 수 있음
# 리스트의 길이 재기
print(len(['H', 'E', 'L', 'L', 'O']))

# 문자열의 길이 재기
print(len("Hello, world!"))



#Mutable(수정 가능) vs. Immutable(수정 불가능)
#리스트는 데이터를 바꿀 수 있지만, 문자열은 데이터를 바꿀 수 없음
#'mutable'한 자료형 : 리스트와 같이 수정 가능한 자료형
#'immutable'한 자료형 : 문자열과 같이 수정 불가능한 자료형 -> 숫자, 불린, 문자열