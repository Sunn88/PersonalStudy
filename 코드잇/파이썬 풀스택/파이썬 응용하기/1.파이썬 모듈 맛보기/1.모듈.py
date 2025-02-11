import calculator

#모듈 이름 변경 가능
import calculator as calc

#특정 함수만 추출 가능 -> 전체 불러오기는 함수 출처가 불분명해지므로 추천하지 않음
from calculator import add, multiply, subtract

#같은 폴더에 있는 모듈만 불러올 수 있음



print(calculator.add(2, 5))
print(calc.multiply(3, 4))
print(subtract(9, 2))