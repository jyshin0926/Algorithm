# 문제를 잘 보고 파악해야함.
# 처음에는 [1]로만 순서두어서 틀렸음. 그 다음에 오는 것들도 비교하고 후순위로 식별자 둠
def reorderLogFiles(logs):
    let = []; dig = []
    for x in logs:
        tmp = x.split()
        if tmp[1].isalpha():
            let.append(x)
        else:
            dig.append(x)
    let.sort(key=lambda x:(x.split()[1:],x.split()[0]))
    return let+dig




print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))