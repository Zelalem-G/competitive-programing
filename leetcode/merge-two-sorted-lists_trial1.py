class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        def rec(l1, l2, cur):
            if not l1:
                cur.next = l2
                return l2
            elif not l2:
                cur.next = l1
                return l1

            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                return rec(l1.next,l2,cur)
            else:
                cur.next = l2
                cur = cur.next
                return rec(l1,l2.next,cur)

        rec(l1,l2,cur)

        return dummy.next