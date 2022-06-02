# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return ListNode((l1.val + l2.val) % 10, self.addTwoNumbersHelper(l1.next, l2.next, (l1.val + l2.val) // 10))
    def addTwoNumbersHelper(self, l1 : Optional[ListNode], l2: Optional[ListNode], carry: int):
        curr = carry
        if l1 != None:
            curr += l1.val
        if l2 != None:
            curr += l2.val
        if (l1 != None and l2 != None):
            return ListNode(curr % 10, self.addTwoNumbersHelper(l1.next, l2.next, curr // 10))
        if (l1 != None):
            return ListNode(curr % 10, self.addTwoNumbersHelper(l1.next, None, curr // 10))
        if (l2 != None):
            return ListNode(curr % 10, self.addTwoNumbersHelper(None, l2.next, curr // 10))
        if curr == 0: # (and l1 == None and l2 == None)
            return None
        return ListNode(curr, None)
