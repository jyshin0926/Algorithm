from collections import deque
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self,x):
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

print(obj, param_2, param_3, param_4)