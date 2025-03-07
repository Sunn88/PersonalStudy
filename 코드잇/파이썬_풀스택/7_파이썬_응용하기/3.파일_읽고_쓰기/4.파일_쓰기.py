# 덮어쓰기 가능
with open('new_file.txt', 'w') as f:
    f.write("Hello world!\n")
    f.write("My name is ssh\n")

# 추가(덮어쓰기 불가)
with open('new_file.txt', 'a') as f:
    f.write("Bye")