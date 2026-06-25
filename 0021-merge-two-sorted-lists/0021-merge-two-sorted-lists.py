# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        p1 = list1
        p2 = list2
        
        if not list1:
            return list2

        if not list2:
            return list1

        stop = False
        lesser=0
        while stop==False:
            if p1.val<=p2.val:
                current.next = p1
                lesser=1
            else:
                current.next = p2
                lesser=2
            if lesser==1 and p1.next is not None:
                p1 = p1.next
                current = current.next
            elif lesser==2 and p2.next is not None:
                p2 = p2.next
                current = current.next
            elif lesser==2 and p2.next is None:
                stop=True
                current = current.next
                current.next = p1
            elif lesser==1 and p1.next is None:
                stop=True
                current = current.next
                current.next = p2
        
        return dummy.next

        """
        # 3. Запускаем цикл (в этом примере жестко берем по 1 элементу 3 раза)
        for _ in range(3):
            if p1: # Если в первом списке еще есть элементы
                current.next = p1  # Присоединяем текущий узел из list1 к нашему результату
                p1 = p1.next       # Сдвигаем указатель первого списка на следующий элемент
                current = current.next # Сдвигаем наш строительный указатель вперед
                
            if p2: # Если во втором списке еще есть элементы
                current.next = p2  # Присоединяем текущий узел из list2 к результату
                p2 = p2.next       # Сдвигаем указатель второго списка на следующий элемент
                current = current.next # Сдвигаем наш строительный указатель вперед

        # 4. Возвращаем dummy.next. 
        # Сама dummy-нода (со значением 0) нам не нужна, но ее .next указывает на 
        # самый первый реальный элемент, который мы присоединили (первый элемент из list1).
        return dummy.next
        """
"""
      !
1  2  3
11 12 13
!

маркеры на первые элементы
цикл пока
добавить меньшее значение под 2 маркерами
лет лессер=номер маркера
если меньший маркер не на конце, то сдвинуть его
если меньший маркер на конце то прицепить оставшийся противоположный список


#сдвинуть тот что сдвигается, если оба на конце, то конец цикла
#
"""