word = input().upper()      # 입력 받은 단어를 모두 대문자(출력시 필요)화여 통일
word_cnt = list()           # 각 알파벳 갯수 리스트 필요
for i in set(word):         # set() 을 통해 알파벳 중복 제거
    word_cnt.append((word.count(i)))    # 알파벳 카운트하여 리스트
idx = [i for i,x in enumerate(word_cnt) if x==max(word_cnt)]        # max 알파벳 인덱스를 넣을 리스트(출력문자 판별용)
if len(idx) > 1:
    print('?')
else:
    print(list(set(word))[word_cnt.index(max(word_cnt))])      # 인덱스(word_cnt에서의 max)에 대한 값 출력