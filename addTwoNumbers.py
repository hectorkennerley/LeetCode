# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # listNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
        # above is what a listNode looks like
        return self.intToListNode((self.listNodeToInt(l1) + self.listNodeToInt(l2)))

    def listNodeToInt(self, l):
        if l.next is None:
            return l.val
        return l.val + 10 * self.listNodeToInt(l.next)

    def intToListNode(self, n):
        n = str(n)
        if len(n) == 1:
            return ListNode(int(n), None)
        return ListNode(int(n[-1]), self.intToListNode(int(n[:-1])))
