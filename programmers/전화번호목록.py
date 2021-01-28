# 하나만 어느 하나로 시작하는 게 있어도 False 리턴이므로 sort를 해주는 게 핵심
def solution(phone_book):
    for a,b in zip(sorted(phone_book), sorted(phone_book)[1:]):
        if b.startswith(a):
            return False
    return True

print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))