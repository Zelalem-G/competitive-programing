# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        ans = []
        cur = head
        size = 0

        while cur:
            size += 1
            cur = cur.next

        l = size // k
        extra = size % k

        cur = head

        for i in range(k):
            part_head = cur
            part_size = l

            if extra > 0:
                part_size += 1
                extra -= 1

            t = 1
            while t < part_size and cur:
                cur = cur.next
                t += 1

            if cur:
                nxt = cur.next
                cur.next = None
                cur = nxt

            ans.append(part_head)

        return ans