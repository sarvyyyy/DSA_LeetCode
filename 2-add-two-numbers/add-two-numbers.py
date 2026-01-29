# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        prev1 = None
        while cur1:
            nxt1=cur1.next
            cur1.next = prev1
            prev1 = cur1
            cur1 = nxt1
        prev2 = None
        while cur2:
            nxt2=cur2.next
            cur2.next = prev2
            prev2 = cur2
            cur2 = nxt2

        str1 = ""
        str2 = ""
        tra1 = prev1
        while tra1:
            str1+=str(tra1.val)
            tra1 = tra1.next
        tra2 = prev2
        while tra2:
            str2+=str(tra2.val)
            tra2 = tra2.next
        ans = int(str1)+int(str2)
        if ans == 0:
            return ListNode(0)
        l = []
        n = 0
        while ans:
            digit = ans%10
            ans //=10
            l.append(digit)
        
        dummy = ListNode(0)
        cur = dummy
        for d in l:
            cur.next = ListNode(d)
            cur = cur.next

        return dummy.next
            