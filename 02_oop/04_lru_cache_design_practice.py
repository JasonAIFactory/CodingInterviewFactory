"""
04_lru_cache_design_practice.py  —  TYPE FROM SCRATCH

Implement LRUCache. O(1) get and put. Hash map + doubly linked list.
"""


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key, value):
        # TODO: store key, value, prev=None, next=None
        pass


class LRUCache:
    def __init__(self, capacity):
        # TODO: validate capacity > 0
        # TODO: store capacity, empty cache dict
        # TODO: create sentinel head and tail nodes, link them
        pass

    def get(self, key):
        # TODO: if key not in cache, return -1
        # TODO: move node to front, return value
        pass

    def put(self, key, value):
        # TODO: if key exists, update value, move to front
        # TODO: else if at capacity, evict LRU
        # TODO: create new node, add to front, store in cache
        pass

    # ---- Helpers ----

    def _add_to_front(self, node):
        # TODO: insert node right after self.head
        pass

    def _remove(self, node):
        # TODO: unlink node from its neighbors
        pass

    def _move_to_front(self, node):
        # TODO: remove + add_to_front
        pass

    def _evict_lru(self):
        # TODO: lru = self.tail.prev
        # TODO: remove it, delete from cache by key
        pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 100)
    cache.put(2, 200)
    assert cache.get(1) == 100      # 1 is now most-recent
    cache.put(3, 300)               # evicts 2
    assert cache.get(2) == -1
    cache.put(4, 400)               # evicts 1
    assert cache.get(1) == -1
    assert cache.get(3) == 300
    assert cache.get(4) == 400

    # Update existing key
    cache.put(3, 999)
    assert cache.get(3) == 999

    # Capacity validation
    try:
        LRUCache(0)
        assert False, "should have raised"
    except ValueError:
        pass

    print("✅ All tests passed.")
