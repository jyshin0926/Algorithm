from collections import Counter
def topKFrequent(nums, k):
    ans = [x[0] for x in Counter(nums).most_common(k)]
    return ans


print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))
