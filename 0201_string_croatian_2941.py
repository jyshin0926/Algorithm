## 아이디어
# 단어 입력받고, 크로아티아 알파벳을 한 개의 문자로 치환하여 단어 새로 구성
# 새로 구성한 단어의 길이 출력
word = input()
cr_ref = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for x in cr_ref:
    word = word.replace(x,'a')  # 크로아티아 문자에 영향이 없는 문자로 치환
print(len(word))
