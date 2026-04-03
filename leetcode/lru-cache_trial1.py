class Node():
    def __init__(self, val, key=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}

        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        if key not in self.map:
            return -1

        node = self.map[key]
        self.remove(node)
        self.addTail(node)

        return node.val


    def put(self, key, value):
        if key in self.map:
            self.remove(self.map[key])

        node = Node(value, key)
        self.map[key] = node
        self.addTail(node)

        if len(self.map) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.map[lru.key]


    def addTail(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node


    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev