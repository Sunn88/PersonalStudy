# 이번에는 유저에게 숫자 3개를 입력 받는 take_guess() 함수를 작성하겠습니다. 
# 이 함수는 유저에게 숫자 3개를 반복적으로 입력 받은 후, 
# 유저가 입력한 숫자들을 리스트에 정리해서 리턴합니다. 
# 유저가 범위에서 벗어나는 숫자를 입력하면, 
# 범위를 벗어나는 숫자입니다. 다시 입력하세요.라는 메시지가 출력되고 다시 입력을 받습니다. 
# 마찬가지로 유저가 이미 입력한 숫자를 다시 입력하면, 
# 중복되는 숫자입니다. 다시 입력하세요.라는 메시지가 출력되고 다시 입력을 받습니다.
# take_guess() 함수는 결과적으로 리스트를 리턴해야 합니다.

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        new_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))

        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_num)

    return new_guess
  
    
# 테스트 코드
print(take_guess())
