# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            n = cur.next          
            t = cur.next.next     
            nxt = t.next          

            cur.next = t
            t.next = n
            n.next = nxt

            cur = n

        return dummy.next