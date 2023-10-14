from SinglyLinkedList import SinglyLinkedList

linkedList = SinglyLinkedList()
print('삽입 테스트')
for i in range(10):
    linkedList.addLast(i+1)
linkedList.printAll() # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10

print()
print('삭제 테스트')
linkedList.remove(3) 
linkedList.printAll() # 1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
linkedList.remove(linkedList.length-1)
linkedList.printAll() # 1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 9