import math
diagonal, h_ratio, w_ratio = map(int, input().split())
x = math.sqrt(diagonal**2 / (h_ratio**2 + w_ratio**2))
print(math.floor(h_ratio*x), math.floor(w_ratio*x))
