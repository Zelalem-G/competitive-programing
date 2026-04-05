class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        l = 0
        cur = head
        while cur:
            cur = cur.next
            l += 1

        k = k % l
        if k == 0:
            return head

        cur = head
        i = 0
        while i < l - k - 1:
            cur = cur.next
            i += 1

        new_head = cur.next
        cur.next = None

        tail = new_head
        while tail.next:
            tail = tail.next

        tail.next = head

        return new_head