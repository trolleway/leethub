# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pntl=head
        pntr=head
        exit=False
        while exit == False:
            if pntr is None or pntr.next is None:
                return pntl
            pntl=pntl.next
            pntr=pntr.next.next
            