def lengthOfLongestSubstring(s: str) -> int:
    hash = {}; start = 0; max_len = 0
    for idx, val in enumerate(s):
        if val in hash and start <= hash[val]:
            start = hash[val] + 1
        else:
            max_len = max(max_len, idx - start + 1)
        hash[val] = idx
    return max_len


print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))