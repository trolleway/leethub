# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        найти середину списка
        развернуть вторую половину списка
        проверить одинаковость половин

        цикл по списку с быстрым и медленным указателем
        когда быстрый указетель на последнем или за последним, медленный находится за серединой/в первом элементе второй половины
        если в списке нечётное число элементов, то медленный находится на среднем элементе
        начало второго списка - с маркера 1
        если в списке нечётное число элементов, то начало второго списка с следующего за маркером, тогда средний не участвует
        развернуть второй список
        сравнить первый и второй список
        '''
        slow=head
        fast=head
        while fast and fast.next: #хитрая конструкция поиска середины
            slow = slow.next
            fast = fast.next.next
        if fast: #хитрая проверка на нечётность длины списка
            slow = slow.next #теперь slow указывает на первый элемент второй половины
        
        mark=slow
        prev=None
        while mark is not None:
            nxt=mark.next
            mark.next=prev
            prev=mark
            mark=nxt
        mark2=prev
        mark1=head
        while mark2 is not None:
            if mark1.val != mark2.val:
                return False
            mark2=mark2.next
            mark1=mark1.next

        return True
        #prev
        '''

            !
        1 2 2 1
                !

            !
        1 2 3 2 1
                !

              !
        1 2 3 4 5 6
                    !

            !
        1 2 3 2 1
                !

        1 2
        21
        '''