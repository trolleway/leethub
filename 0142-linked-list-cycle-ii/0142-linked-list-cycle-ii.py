# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        has_cycle = False  # Флаг: нашли ли мы цикл
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True  # Цикл точно есть
                break
                
        # ИСПРАВЛЕНИЕ 1: Если первый цикл кончился, а встречи не было — цикла нет
        if not has_cycle:
            return None
            
        l = head
        r = slow
        
        # ИСПРАВЛЕНИЕ 2: Если цикл начинается в head, то l уже равен r
        if l == r: 
            return l
            
        while l != r:
            l = l.next
            r = r.next
            if l == r: 
                return l
                
        return None

        return None
            
        
        return False