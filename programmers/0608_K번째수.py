def solution(array, commands):
    ans = []
    tmp = []
    for i in range(len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        new_array = sorted(array[start-1:end])
        num = commands[i][2]
        tmp.append(new_array)
        for idx in range(len(tmp[i])):
            if idx == num - 1:
                ans.append(tmp[i][idx])
    return ans


def solution2(arr, cmd):
   ans=[]
   for i,j,k in cmd:
       ans.append(sorted(arr[i-1:j])[k-1])
       print(k)
   return ans

a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a,c))
print(solution2(a,c))