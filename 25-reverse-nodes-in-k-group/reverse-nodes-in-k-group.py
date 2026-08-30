# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            prev = groupNext
            cur = groupPrev.next

            while cur!=groupNext:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            temp = groupPrev.next
            groupPrev.next = prev
            groupPrev = temp

    
