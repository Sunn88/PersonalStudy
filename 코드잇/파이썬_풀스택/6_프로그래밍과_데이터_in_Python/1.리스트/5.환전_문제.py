# 먼저 한국 원화를 미국 달러로 변환해 주는 krw_to_usd 함수, 
# 그리고 미국 달러를 일본 엔화로 변환해 주는 usd_to_jpy 함수를 써야 하는데요. 
# krw_to_usd 함수는 파라미터로 원화 krw을 받아서 변환된 미국 달러 액수를 리턴해 줍니다. 
# 마찬가지로 usd_to_jpy 함수는 파라미터로 달러 usd를 받아서 변환된 일본 엔화 액수를 리턴해 주는 거죠.
# 참고로 환율은 1달러에 1,000원, 그리고 1,000엔에 8달러라고 가정합니다.

# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    # 여기에 코드를 작성하세요
    return krw * 0.001

# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    # 여기에 코드를 작성하세요
    return usd * (1000/8)

# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 
# prices를 원화(￦)에서 달러($)로 변환하기
# 여기에 코드를 작성하세요
i = 0
while i < len(prices):
    prices[i] = krw_to_usd(prices[i])
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)으로 변환하기
# 여기에 코드를 작성하세요
i = 0
while i < len(prices):
    prices[i] = usd_to_jpy(prices[i])
    i += 1

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))