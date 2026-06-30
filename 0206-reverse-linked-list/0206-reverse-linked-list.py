# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        mark = head
        while mark is not None:
            nxt=mark.next
            mark.next=prev
            prev=mark
            mark=nxt
        return prev

        """
        проход по циклу
        считывание следующего
        текущий изменяется: ссылается на предыдущий
        """