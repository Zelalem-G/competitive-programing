class Solution(object):
    def partition(self, head, x):
        less = None
        lhead = None
        greater = None
        ghead = None
        
        cur = head

        while cur:
            temp = cur.next      
            cur.next = None      

            if cur.val < x:
                if not less:
                    less = cur
                    lhead = less
                else:
                    less.next = cur
                    less = less.next
            else:
                if not greater:
                    greater = cur
                    ghead = greater
                else:
                    greater.next = cur
                    greater = greater.next

            cur = temp

        if not lhead:
            return ghead

        less.next = ghead
        return lhead