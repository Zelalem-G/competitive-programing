class Solution(object):
    def flatten(self, head):
        def dfs(node):
            cur = node
            last = None

            while cur:
                nxt = cur.next

                if cur.child:
                    child_tail = dfs(cur.child)

                    cur.next = cur.child
                    cur.child.prev = cur

                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail

                    cur.child = None
                    last = child_tail
                else:
                    last = cur

                cur = nxt

            return last

        dfs(head)
        return head