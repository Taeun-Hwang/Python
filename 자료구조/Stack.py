class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # 스택이 비어있는지 확인
        return len(self.items) == 0

    def push(self, item):
        # 스택에 항목 추가
        self.items.append(item)

    def pop(self):
        # 스택의 가장 위에 있는 항목 제거 및 반환
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        # 스택의 가장 위에 있는 항목 확인
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        # 스택의 크기 확인
        return len(self.items)


# 스택 사용 예시
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print("스택의 크기: ", my_stack.size())
    print("가장 위의 항목: ", my_stack.peek())

    my_stack.pop()
    print("pop 후 가장 위의 항목: ", my_stack.peek())
    print("스택이 비어있는지 확인: ", my_stack.is_empty())
