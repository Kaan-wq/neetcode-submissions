class Node:
    def __init__(
        self,
        val: int | None = None,
        key: int | None = None,
        prev_ptr: "Node | None" = None,
        next_ptr: "Node | None" = None,
    ):
        self.val = val
        self.key = key
        self.prev = prev_ptr
        self.next = next_ptr

class LRUCache:
    def __init__(self, capacity: int):
        self.c_max = capacity
        self.c_cur = 0 # running capacity
        self.kn: dict[int, Node] = {} # nodes set
        self.head = Node() # DLL head
        self.tail = Node() # DLL tail

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node: Node):
        node.prev, node.next = self.tail, None
        self.tail.next, self.tail = node, node

    def get(self, key: int) -> int:
        node = self.kn.get(key, None)
        if node:
            if node is self.head and node.next:
                self.head = node.next
            
            if node is not self.tail:
                self._remove(node)
                self._append(node)

            return self.tail.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.kn.get(key, None)
        cache_hit = False
        if node:
            cache_hit = True # record cache hit

            if node is self.head and node.next:
                self.head = node.next

            if node is not self.tail:
                self._remove(node)
                self._append(node)

            self.tail.val = value
        else: # cache miss
            node = Node(value, key)
            self.kn[key] = node # add node to dict
            self._append(node)

        if self.c_cur < self.c_max:
            # has capacity
            if self.c_cur == 0:
                self.head = node
            self.c_cur += 0 if cache_hit else 1
        elif not cache_hit:
            # no capacity
            del_node = self.head
            self.head = self.head.next
            del self.kn[del_node.key]
            del del_node