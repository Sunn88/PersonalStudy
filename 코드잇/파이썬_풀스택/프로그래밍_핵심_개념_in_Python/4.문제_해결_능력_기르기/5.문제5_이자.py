# 1988년 쌍문동에 사는 택이는 바둑 대회 우승 상금으로 5,000만 원을 받았습니다.
# 이 돈을 어떻게 할지 고민하던 택이는, 이웃인 동일 아저씨와 미란 아주머니의 의견 중 하나를 선택하려 합니다.
# 1. 이자가 붙은 원금에 다시 이자가 붙는 연복리 예금에 넣기
# 2. 아파트 가치 상승을 고려하여 당시 매매가 5000만 원인 은마 아파트 사기
# 2016년 기준 은마아파트의 매매가는 11억 원인데요. 1988년 은행에 5,000만 원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여,
# 은행에 저축해 둔 금액이 더 크면, *원 차이로 동일 아저씨 말씀이 맞습니다.를 출력하고
# 은마아파트의 가격이 더 크면, *원 차이로 미란 아주머니 말씀이 맞습니다.를 출력하는 코드를 작성해 보세요.
# 2016년에 은행에 저축해 둔 금액 계산은 while 문을 이용한 반복문으로 계산해주세요.
# 은마아파트 가격과 은행에 저축해 둔 금액을 비교 후 메시지 출력시에는 if 문을 사용해주세요.
# 최종 결과에서 1원 미만은 계산하지 않습니다.

price = 50000000
now = 1988
fut = 2016
apt = 1100000000

while now < fut:
    price = price * 1.12
    now += 1

if round(price) > apt:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(round(price) - apt))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(apt - round(price)))

# 모범답안
# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

# 변수 정의
year = 1988
bank_balance = 50000000

while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))
