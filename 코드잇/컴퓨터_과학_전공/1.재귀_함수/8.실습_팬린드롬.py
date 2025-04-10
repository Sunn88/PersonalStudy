# 문자열 my_str을 파라미터로 받아서 my_str이 팰린드롬인지 판별하는 함수 is_palindrome() 을 작성해 주세요.

def is_palindrome(my_str):
    # 베이스 케이스
    if len(my_str) <= 1:
        return True

    # 재귀 케이스
    if my_str[0] != my_str[-1]:
        return False 

    return is_palindrome(my_str[1: -1])


# 테스트 코드
print(is_palindrome('기러기'))
print(is_palindrome('토마토'))
print(is_palindrome('바나나'))
print(is_palindrome('racecar'))
print(is_palindrome('radar'))
print(is_palindrome('stars'))
print(is_palindrome('123321'))