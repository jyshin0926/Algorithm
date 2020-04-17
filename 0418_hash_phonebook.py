## script 1
# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         if phone_book[i] in phone_book[i+1]:
#             return False
#         return True


## script 2
### zip() 으로 앞뒤값 비교하기
### str.startswith() : str[beg:end] 에서 원하는 문자열 찾기

def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
        return True


phone_book = list(input().split())
print(solution(phone_book))


