"""
09_trie.py  —  REFERENCE FILE

Trie (Prefix Tree) template.

Use when:
  - Prefix lookup (autocomplete, dictionary)
  - "Word search II" type problems
  - Spell-check / longest common prefix

Operations (all O(L) where L = key length):
  - insert(word)
  - search(word)         exact match
  - startsWith(prefix)   prefix exists in any inserted word
"""


class TrieNode:
    __slots__ = ("children", "is_word")

    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_word: bool = False


class Trie:
    def __init__(self):
        # SAY: "Root is an empty node — it represents the empty prefix."
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        """True only if the EXACT word was inserted."""
        node = self._walk(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        """True if any inserted word begins with this prefix."""
        return self._walk(prefix) is not None

    def _walk(self, key: str) -> TrieNode | None:
        node = self.root
        for ch in key:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    print(t.search("apple"))         # True
    print(t.search("app"))           # False
    print(t.starts_with("app"))      # True
    t.insert("app")
    print(t.search("app"))           # True

    t.insert("application")
    print(t.starts_with("appli"))    # True
    print(t.starts_with("banana"))   # False
