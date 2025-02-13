# standard library(표준 라이브러리) : 자주 쓰는 모듈들

# 수학 관련 기능들
import math

print(math.log10(100))
print(math.cos(0))
print(math.pi)


# 랜덤한 값 생성
import random

print(random.random())

# randint() 함수 : 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수
# randint(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))

# uniform() 함수 : 두 수 사이의 랜덤한 소수를 리턴하는 함수
# randint() 함수와 다른 것은 리턴하는 값이 정수가 아니라 소수라는 점
# uniform(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 소수 N을 리턴
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))


# 파이썬으로 운영체제 조작
import os

print(os.getlogin())
print(os.getcwd())


# 날짜와 시간
import datetime

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))

today = datetime.datetime.now()
print(today)
print(type(today))

# timedelta 타입 : 날짜 간의 차이를 나타내는 타입
print(today - pi_day)
print(type(today - pi_day))
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)
print(today + my_timedelta)

today = datetime.datetime.now()
print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

today = datetime.datetime.now()
print(today)
print(today.strftime("%A, %B %dth %Y"))

# 포맷코드
# 포맷코드	설명	                            예시
# %a	    요일 (짧은 버전)	                Mon
# %A	    요일 (풀 버전)	                    Monday
# %w	    요일 (숫자 버전, 0~6, 0이 일요일)   5
# %d	    일 (01~31)	                        23
# %b	    월 (짧은 버전)	                    Nov
# %B	    월 (풀 버전)	                    November
# %m	    월 (숫자 버전, 01~12)	            10
# %y    	연도 (짧은 버전)	                16
# %Y	    연도 (풀 버전)	                    2016
# %H	    시간 (00~23)	                    14
# %I	    시간 (00~12)	                    10
# %p	    AM/PM	                            AM
# %M	    분 (00~59)	                        34
# %S	    초 (00~59)	                        12
# %f	    마이크로초 (000000~999999)	        413215
# %Z	    표준시간대	                        PST
# %j	    1년 중 며칠째인지 (001~366)	        162
# %U	    1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	35
# %W	    1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35