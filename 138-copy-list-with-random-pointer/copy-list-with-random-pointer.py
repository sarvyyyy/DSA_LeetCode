"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        temp = head
        mp = {}
        while temp:
            mp[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        while temp:
            mp[temp].next = mp.get(temp.next)
            mp[temp].random = mp.get(temp.random)
            temp = temp.next
        return mp[head]