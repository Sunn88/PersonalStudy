# Divide and Conquer를 이용해서 1부터 n까지 더하는 예시를 보았는데요. 코드로 한 번 구현해 봅시다.

# 우리가 작성할 함수 consecutive_sum은 두 개의 정수 인풋 start와 end를 받고, 
# start부터 end까지의 합을 리턴합니다. end는 start보다 크다고 가정합니다.

def consecutive_sum(start, end):
    # base case        
    if end == start:
        return start

    # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다 (Divide)
    mid = (start + end) // 2

    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine).
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트 코드
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
