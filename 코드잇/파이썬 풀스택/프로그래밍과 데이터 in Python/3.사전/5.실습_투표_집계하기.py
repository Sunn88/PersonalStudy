# 파이썬 리스트 votes에는 성북구민들의 투표 결과가 저장되어 있습니다. 
# 리스트 votes의 정보를 토대로, 사전 vote_counter에 후보별 득표수를 정리하는 것이 목표입니다.
# 예를 들어서 votes가 ['허유나', '서혜선', '허유나']라고 가정하면, vote_counter는 {'허유나': 2, '서혜선': 1}이 되어야 하는 거죠.

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

# 후보별 득표수 출력
print(vote_counter)