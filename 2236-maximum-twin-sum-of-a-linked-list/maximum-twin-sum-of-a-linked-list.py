# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        left = head
        right = prev
        ans = 0

        while right:
            ans = max(ans, left.val + right.val)
            left = left.next
            right = right.next

        return ans     