from collections import Counter
def numJewelsInStones(jewels, stones):
    jewel_dict = Counter(stones)
    cnt = 0
    for j in jewels:
        cnt += jewel_dict[j]
    return cnt

print(numJewelsInStones('aA','aAAbbbb'))
print(numJewelsInStones('z','ZZ'))