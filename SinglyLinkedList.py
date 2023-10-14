# 단일 연결리스트 노드
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# 단일 연결리스트
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def remove(self, index):
        self.validateIndex(index)
        # 첫 번째 노드를 삭제 하는 경우
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        # 첫 번째 노드가 아닌 노드를 삭제 하는 경우
        beforeNode = self.findNodeFrom(index-1)
        beforeNode.next = beforeNode.next.next
        self.length -=1
    
    def removeLast(self):
        self.remove(self.length - 1)

    def add(self, index, data):
        '''
            index: 데이터가 삽입될 인덱스 0~length-1 까지 유효\n
            data: 노드의 데이터
        '''
        self.validateIndex(index)
        newNode = Node(data)

        # 연결리스트가 비어 있는 경우 
        if self.head == None:
            self.head = newNode
            self.length += 1
            return
        
        # 첫 번째에 삽입 하는 경우
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
            return

        # 첫번째 노드가 아닌 곳에 삽입하는 경우 삽입할 위치의 이전 노드를 찾는다.
        beforeNode = self.findNodeFrom(index-1)
        newNode.next = beforeNode.next
        beforeNode.next = newNode
        self.length += 1

    def addLast(self, data):
        self.add(self.length, data)

    def findNodeFrom(self, index):
        ret = self.head
        for _ in range(index):
            ret = ret.next
        return ret

    def validateIndex(self, index):
        if index > self.length or index < 0:
            raise IndexError('허용되지 않는 인덱스입니다. 현재 연결리스트의 허용 인덱스 0~%d' %(self.length))
    
    def printAll(self):
        cur = self.head

        while cur != None:
            if cur.next != None:
                print(cur.data, end=" -> ")
            else:
                print(cur.data)
            cur = cur.next
