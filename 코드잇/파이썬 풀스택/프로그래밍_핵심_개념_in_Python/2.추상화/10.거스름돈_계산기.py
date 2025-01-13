def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈 총액
    fifty_count = change // 50000  # 50,000원 지폐
    #ten_count = (change - 50000 * fifty_count) // 10000
    ten_count = (change % 50000) // 10000  # 10,000원 지폐 모범답안
    #five_count = (change - 50000 * fifty_count - 10000 * ten_count) // 5000
    five_count = (change % 10000) // 5000  # 5,000원 지폐 모범답안
    #one_count = (change - 50000 * fifty_count - 10000 * ten_count - 5000 * five_count) // 1000
    one_count = (change % 5000) // 1000  # 1,000원 지폐 모범답안
    
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))


# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)