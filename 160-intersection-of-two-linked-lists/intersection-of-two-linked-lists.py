class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1 = headA
        cur2 = headB
        while cur1!=cur2:
            if cur1 is None:
                cur1 = headB
            else:
                cur1 = cur1.next
            if cur2 is None:
                cur2 = headA
            else:
                cur2 = cur2.next
        return cur1