"""
04_lru_cache_design.py  —  REFERENCE FILE

Goal: Implement LRU Cache (LeetCode 146).
This is one of the MOST COMMON Amazon interview problems.

Requirements:
  - get(key)        -> value or -1 if not present.   O(1)
  - put(key, value) -> insert; evict least-recently-used if full.   O(1)

Solution: hash map + doubly linked list.
The hash map gives O(1) lookup. The list gives O(1) move-to-front.

SAY at the start of the interview:
"I will use a hash map for O(1) lookup, and a doubly linked list to track
 recency in O(1). Every time a key is accessed, I move its node to the
 front. When the cache is full, I evict the node at the back."
"""


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.cache: dict[int, _Node] = {}

        # SAY: "I use sentinel head and tail nodes to avoid edge cases
        #       when adding or removing at the boundaries."
        self.head = _Node(0, 0)
        self.tail = _Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---- Public API ----

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key, move to front
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
            return

        # Insert new key
        if len(self.cache) >= self.capacity:
            self._evict_lru()

        node = _Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

    # ---- Private helpers (separation of concerns) ----

    def _add_to_front(self, node: _Node) -> None:
        # SAY: "I insert right after the head sentinel."
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node: _Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    def _evict_lru(self) -> None:
        # SAY: "The node right before the tail is the least recently used."
        lru = self.tail.prev
        self._remove(lru)
        del self.cache[lru.key]


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 100)
    cache.put(2, 200)
    print(cache.get(1))   # 100
    cache.put(3, 300)     # evicts key 2
    print(cache.get(2))   # -1 (evicted)
    cache.put(4, 400)     # evicts key 1
    print(cache.get(1))   # -1
    print(cache.get(3))   # 300
    print(cache.get(4))   # 400
