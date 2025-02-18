# 거꾸로 읽어도 똑같은 단어를 '팰린드롬(palindrome)'이라고 부릅니다.
# 팰린드롬 여부를 확인하는 함수 is_palindrome을 작성하려고 하는데요. 
# is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴하고 팰린드롬이 아니면 False를 리턴합니다.

def is_palindrome(word):
    word_list = list(word)
    word_reversed_list = word_list[::-1]
    if word_list == word_reversed_list:
        return True
    else:
        return False
    
# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))


# 모범답안
def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True

# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
