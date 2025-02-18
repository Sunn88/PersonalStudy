# 1. 단어장 만들기
# 잘 모르는 단어 네 개입니다.
# sanitizer: 살균제
# ambition: 야망
# conscience: 양심
# civilization: 문명
# 이 단어들을 저장하는 사전을 만들고, 만든 사전을 vocab라는 변수에 저장하세요. 
# 단어와 뜻이 key-value로 들어가야 합니다.

# 2. 새로운 단어들 추가
# 이미 만들어진 vocab 사전에 새로운 단어들을 추가하고 싶습니다. 아래 단어들을 추가해 주세요.
# privilege: 특권
# principle: 원칙

vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명'
}
print(vocab)

vocab['privilege'] = '특권'
vocab['principle'] = '원칙'
print(vocab)