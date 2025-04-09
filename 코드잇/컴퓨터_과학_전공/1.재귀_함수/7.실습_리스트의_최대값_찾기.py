# 리스트 my_list를 파라미터로 받아서 my_list의 최대 요소를 리턴하는 함수 max_list()를 작성해 주세요. 
# my_list의 모든 요소는 숫자이고, 1개 이상의 요소가 있다고 가정합니다.
# for문, while문 그리고 max() 함수는 사용하지 말아 주세요!

def max_list(my_list):
    # 베이스 케이스
    if len(my_list) == 1:
        return my_list[0]

    # 재귀 케이스
    max_sublist = max_list(my_list[:-1])
    if max_sublist >= my_list[-1]:
        return max_sublist
    else:
        return my_list[-1]


# 테스트 코드
print(max_list([1, 4, 3, 2, 5, 0, 2]))
print(max_list([-1, -3, -10, -5, -9]))
print(max_list([3, 7, 3, 7, 7]))
print(max_list([1, 2.7, -3, 2.8, 1.6]))
print(max_list([32, 2, 3, 0 , 1]))