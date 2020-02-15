coin_list = [500,100,50,10, 5, 1]
def greedy(value, coin_list):
    total = 0
    for coin in coin_list:
        # print('coin',coin)
        num = value // coin     # 갯수는 금액/동전값 몫 (// : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함)
        total += num            # 최종갯수 업데이트
        value -= num * coin     # 금액은 갯수*동전값 만큼 빠지면서 나머지 금액 for문 돌아야함
    return total
print(greedy(1000-int(input()), coin_list))