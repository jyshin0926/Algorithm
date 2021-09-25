class MyCircularQueue:
    def __init__(self,k):
        self.q = [None]*k  # k(큐의 크기) 초기화
        self.maxlen = k    # 최대길이를 k값으로 설정
        self.p1 = 0     # front 포인터
        self.p2 = 0     # rear 포인터

    # 요소 삽입 연산
    def enQueue(self,value):    # rear 포인터 이동
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # 요소 삭제 연산
    # 원래 원형 큐의 dequeue는 요소삭제랑 추출 같이 수행되지만 리트코드 문제요구사항에 따름
    def deQueue(self):   # front 포인터 이동
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    # 원래 큐에는 rear 연산이 없고 맨 앞에 있는 요소를 가져오는 front 또는 Peek 연산만 있으나, 리트코드 요구사항에 따름
    # 원형 큐를 구현하기 위해서는 2개의 포인터를 사용하는 만큼, rear 연산을 구현하는 건 어렵지 않음
    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2-1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None


obj = MyCircularQueue(5)
param_1 = obj.enQueue(0)
param_2 = obj.enQueue(1)
param_3 = obj.enQueue(2)
param_4 = obj.deQueue()
param_5 = obj.Front()
param_6 = obj.Rear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()

print(obj, param_1,param_2,param_3,param_4,param_5,param_6,param_7,param_8)


