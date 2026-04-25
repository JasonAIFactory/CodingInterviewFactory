"""
09_trie_practice.py  —  TYPE FROM SCRATCH
"""


class TrieNode:
    __slots__ = ("children", "is_word")

    def __init__(self):
        # TODO: self.children = {}; self.is_word = False
        pass


class Trie:
    def __init__(self):
        # TODO: root = TrieNode()
        pass

    def insert(self, word):
        # TODO: walk through chars, creating nodes as needed
        # TODO: mark final node is_word = True
        pass

    def search(self, word):
        # TODO: _walk to last node; return node is not None and node.is_word
        pass

    def starts_with(self, prefix):
        # TODO: _walk; return node is not None
        pass

    def _walk(self, key):
        # TODO: starting from root, descend by character; return node or None
        pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.starts_with("app") is True
    t.insert("app")
    assert t.search("app") is True

    t.insert("application")
    assert t.starts_with("appli") is True
    assert t.starts_with("banana") is False

    # Empty trie
    empty = Trie()
    assert empty.search("anything") is False
    assert empty.starts_with("a") is False

    print("✅ All tests passed.")
