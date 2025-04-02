# 하위 문제 찾기 : 파라미터로 받은 input의 사이즈를 하나 줄여서 생각하기
# 베이스 케이스 : 하위 문제 없이 바로 답을 알 수 있는 경우
# 재귀 케이스 : 하위 문제 필요

def reverse(my_list):
    if len(my_list) <= 1:
        return my_list
    return my_list[-1:] + reverse(my_list[:-1])

print(reverse([5, 2, 7, 1, 4]))