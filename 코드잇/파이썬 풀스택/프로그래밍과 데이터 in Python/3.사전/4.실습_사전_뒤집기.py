# 사전의 key와 value를 뒤집어 주는 함수 reverse_dict를 작성해 주세요. 
# reverse_dict는 파라미터로 사전 old_dict를 받고, key와 value가 뒤집힌 새로운 사전을 리턴합니다.

def reverse_dict(old_dict):
    new_dict = {}

    for key, value in old_dict.items():
        new_dict[value] = key
        new_dict[key] = value
    
    return new_dict

# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))