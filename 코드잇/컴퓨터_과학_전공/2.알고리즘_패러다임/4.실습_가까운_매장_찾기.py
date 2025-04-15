# 태호는 영업팀에서 매장들 좌표 위치를 튜플 리스트로 받아 왔습니다.
# 예시 tuple 리스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

# 튜플은 각 매장의 위치를 x, y 좌표로 나타낸 것입니다.
# 0번 매장은 (2, 3)에, 그리고 1번 매장은 (12, 30) 위치에 있는 거죠.
# 태호가 사용하려는 함수 closest_pair는 이 좌표 리스트를 파라미터로 받고,
# 리스트 안에서 가장 가까운 두 매장을 [(x1, y1), (x2, y2)] 형식으로 리턴합니다.
#참고로 태호는 이미 두 좌표 사이의 거리를 계산해 주는 함수 distance를 써 놨는데요,
# 함수 distance는 인풋으로 두 튜플을 받아서 그 사이의 직선 거리를 리턴합니다.
print(distance((2, 5), (5, 9))) # => 두 지점 사이의 거리 5.0이 출력됨

# 제곱근 사용을 위한 sqrt 함수 불러오기
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 현재까지 본 가장 가까운 두 매장
    pair = [coordinates[0], coordinates[1]]
  
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]

            # 더 가까운 두 매장을 찾으면 pair 업데이트
            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]

    return pair

# 테스트 코드
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
