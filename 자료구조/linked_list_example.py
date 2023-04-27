class Node:
    def __init__(self, data):
        self.data = data  # 노드의 데이터 저장
        self.next = None  # 다음 노드에 대한 참조 초기화

class LinkedList:
    def __init__(self):
        self.head = None  # 연결 리스트의 첫 번째 노드를 가리키는 head 초기화

    def insert(self, data):
        new_node = Node(data)  # 새 노드 생성
        new_node.next = self.head  # 새 노드의 다음 노드를 기존 head로 지정
        self.head = new_node  # head를 새 노드로 업데이트

    def delete(self, data):
        current = self.head  # 현재 노드를 head로 시작
        prev = None  # 이전 노드를 None으로 초기화

        while current:
            if current.data == data:  # 삭제할 데이터를 찾으면
                if prev:
                    prev.next = current.next  # 이전 노드의 다음 노드를 현재 노드의 다음 노드로 업데이트
                else:
                    self.head = current.next  # 삭제할 노드가 head 노드인 경우, head를 다음 노드로 업데이트
                return True
            prev = current
            current = current.next  # 다음 노드로 이동
        return False

    def display(self):
        current = self.head  # 현재 노드를 head로 시작
        while current:
            print(current.data, end=' -> ')  # 노드의 데이터를 출력
            current = current.next  # 다음 노드로 이동
        print("None")

linked_list = LinkedList()

while True:
    print("\n1: Insert, 2: Delete, 3: Display, 4: Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the integer to insert: "))
        linked_list.insert(data)  # 정수 삽입
    elif choice == 2:
        data = int(input("Enter the integer to delete: "))
        if linked_list.delete(data):  # 정수 삭제
            print("Data deleted.")
        else:
            print("Data not found.")
    elif choice == 3:
        linked_list.display()  # 연결 리스트 출력
    elif choice == 4:
        break  # 종료
    else:
        print("Invalid choice.")
