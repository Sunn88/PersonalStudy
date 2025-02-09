# mask_security_number라는 함수를 정의하려고 하는데요. 
# 이 함수는 파라미터로 문자열 security_number를 받고, security_number의 마지막 네 글자를 '*'로 대체한 새 문자열을 리턴합니다.
# 참고로 파라미터 security_number에는 작대기 기호(-)가 포함될 수도 있고, 포함되지 않을 수도 있는데요.  작대기 포함 여부와 상관 없이, 마지막 네 글자가 '*'로 대체되어야 합니다!

def mask_security_number(security_number):
    security_number_list = []
    for i in range(len(security_number)):
        security_number_list.append(security_number[i])
    print(security_number_list)
    return(security_number_list)


# 테스트 코드
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))


# 모범답안1
def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

    # 리스트를 문자열로 복구
    total_str = ""
    for i in range(len(num_list)):
        total_str += num_list[i]

    return total_str


# 모범답안2
def mask_security_number(security_number):
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = '*'

    # 리스트를 문자열로 복구하여 반환
    return ''.join(num_list)


# 모범답안3
def mask_security_number(security_number):
    return security_number[:-4] + '****'


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
