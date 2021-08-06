from collections import Counter
import re
def mostCommonWord(paragraph: str, banned):
    paragraph = [word for word in re.sub('[^0-9a-z]',' ',paragraph.lower()).split() if word not in banned]
    counter = Counter(paragraph)
    return counter.most_common(1)[0][0]

print(mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))


# 또 다른 정규표현식
# \w : word character 의미
# r 문자는 raw string으로 백슬래시 문자를 해석하지 않고 남겨두기 때문에 정규표현식과 같은 곳에 유용
# [] : 문자들의 범위를 나타내기 위해 사용
def sol2(paragraph, banned):
    paragraph = [word for word in re.sub(r'[^\w]',' ',paragraph.lower()).split() if word not in banned]
    counter = Counter(paragraph)
    return counter.most_common(1)[0][0]

print(sol2(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
