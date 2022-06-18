from socket import has_dualstack_ipv6
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(n, prev, curr):
            if n == 1:
                prev.next = curr.next
            else:
                helper(n - 1, curr, curr.next)
        # need to find the node to be removed, relative to the start (NOT end)
        # just traverse the list and find the length
        # (alternative: reverse the linked list, remove Nth node, reverse again)
        l = 0
        curr = head
        while curr != None:
            l += 1
            curr = curr.next
        if l - n == 0:
            return head.next
        helper(l - n, head, head.next)
        return head
