# 이제 스트라이크 수와 볼 수를 알려 주는 get_score() 함수를 작성할 것입니다. 
# 이 함수는 두 개의 파라미터를 받는데요.
# guesses: 유저가 뽑은 번호 3개가 담긴 리스트
# solution: 컴퓨터가 뽑은 정답 번호 3개가 담긴 리스트
# 두 리스트를 비교해서 스트라이크와 볼의 개수를 계산하고 리턴합니다. 
# 여기서 새로운 개념을 알려 드릴게요. 
# 파이썬의 함수에서 여러 값을 리턴하고 싶으면 이렇게 할 수 있습니다.

# def square_and_cube(x):
#    square = x ** 2
#    cube = x ** 3
#    return square, cube

# 또한 여러 리턴 값을 한 번에 여러 변수에 저장할 수도 있습니다. 
# 아래와 같이 코드를 작성하면 square_and_cube(2)의 첫 번째 리턴 값이 변수 s에 저장되고, 
# 두 번째 리턴 값이 변수 c에 저장됩니다.

# s, c = square_and_cube(2)
# print(s)
# print(c)

# 이런 식으로 get_score() 함수는 스트라이크와 볼의 개수를 모두 리턴하도록 해야 합니다.

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        # 스트라이크 판단 방법
        if guesses[i] == solution[i]:
            strike_count += 1
        # 볼 판단 방법
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 테스트 코드
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)



# 테스트 코드
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)
