print("저는 {1}, {0}, {2}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1/num_2))


#%기호 : 포맷 스트링 -> 옛날 방식
name1 = "최지웅"
age1 = 32
print("제 이름은 %s이고 %d살입니다." % (name1, age1))

#format() 메소드
name2 = "최지웅"
age2 = 32
print("제 이름은 {}이고 {}살입니다.".format(name2, age2))

#f-string -> 최신 방식
name3 = "최지웅"
age3 = 32
print(f"제 이름은 {name3}이고 {age3}살입니다.")


#실습
wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)
# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))
# "5시간에 25달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5, wage * 5, "달러"))  # 여기에 코드를 작성하세요
# "1시간에 5710.8원 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1 * exchange_rate, "원"))  # 여기에 코드를 작성하세요
# "5시간에 28554.0원 벌었습니다." 출력
print("{}시간에 {:.1f}{} 벌었습니다.".format(5, wage * 5 * exchange_rate, "원"))  # 여기에 코드를 작성하세요