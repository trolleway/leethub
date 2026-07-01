# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        zero = ListNode(0,head)
        pnt = zero
        while pnt and pnt.next: #трюк
            if pnt.next.val == val:
                pnt.next=pnt.next.next
            else:
                pnt = pnt.next
        return zero.next
        

'''
вставить условный элемент в начало
указатель на первый
цикл
если следующий=пусто, то конец
если следующий=вал, то указатель.след=след.след
переход на следующий
'''