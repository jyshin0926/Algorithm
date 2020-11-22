def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            return False
    return True
# 테스트 1 〉	통과 (3.25ms, 10.9MB)
# 테스트 2 〉	통과 (3.90ms, 10.9MB)

def solu(phone_book):
    phone_book.sort()
    for a,b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True
# 테스트 1 〉	통과 (3.32ms, 10.8MB)
# 테스트 2 〉	통과 (3.25ms, 10.9MB)





print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))

print(solu(['119', '97674223', '1195524421']))
print(solu(['123','456','789']))
print(solu(['12','123','1235','567','88']))


# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인