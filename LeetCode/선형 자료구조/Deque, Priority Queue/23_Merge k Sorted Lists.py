def mergeKLists(lists):
    return sorted(sum(lists,[]))

print(mergeKLists([[1,4,5],[1,3,4],[2,6]]))
print(mergeKLists([]))
print(mergeKLists([[]]))