# a<b<c라고 가정할 때, a+b+c=400a+b+c=400을 만족하는 피타고라스 삼조(a,b,c)(a,b,c)는 단 하나인데요. 이 경우, a∗b∗ca∗b∗c는 얼마인가요?

# 단순하지만 비효율적인 버전
#for a in range(1, 400):
#    for b in range(1, 400):
#        for c in range(1, 400):
#            if a * a + b * b == c * c and a < b < c and a + b + c == 400:
#                print(a * b * c)

# 모범답안
for a in range(1, 400):
    for b in range(1, 400):
        c = 400 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)