# 같은 폴더 내에 있지 않으면 경로도 포함해야 함

import os
dir = os.getcwd()
with open(f'{dir}/../파일 읽고 쓰기/chicken.txt', 'r') as f:
    print(type(f))
    for line in f:
        print(line)