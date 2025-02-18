#파라미터에 '기본값(default value)'을 설정할 수 있음
#기본값을 설정해 두면, 함수를 호출할 때 파라미터에 값을 꼭 넘겨주지 않아도 됨
#이런 파라미터를 '옵셔널 파라미터(optional parameter)'
#필수로 넘겨줄 필요가 없으니까 '옵셔널'

def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))

myself("코드잇", 1, "미국")  # 옵셔널 파라미터에 값을 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터에 값을 제공하지 않는 경우


#옵셔널 파라미터는 모두 마지막에 있어야 함
#중간에 넣으면 오류 발생

def myself(name, nationality="한국", age):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))

myself("코드잇", 1)  # 기본값이 설정된 파라미터를 바꾸지 않을 때
print()
myself("코드잇", "미국", 1)  # 기본값이 설정된 파라미터를 바꾸었을 때
