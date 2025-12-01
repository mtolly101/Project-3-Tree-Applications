from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class TrieNode:
    """A single node in the Trie"""
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    is_end: bool = False

class Trie:
    """Trie (prefix tree) implementation"""

    def __init__(self) -> None:
        self.root = TrieNode()
        self._word_count = 0

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie

        Time: O(m) where m is the length of the word
        Space: O(m) extra in the worst case if new nodes are added
        """
        if not word:
            return  # ignore empty strings

        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        if not node.is_end:
            node.is_end = True
            self._word_count += 1

    def search(self, word: str) -> bool:
        """
        Check if a word exists in the trie

        Time: O(m)
        Space: O(1)
        """
        if not word:
            return False

        node = self._find_node(word)
        return bool(node and node.is_end)

    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word starts with this prefix

        Time: O(p)
        Space: O(1)
        """
        if prefix == "":
            # Every word starts with empty prefix if the trie is not empty
            return not self.is_empty()
        return self._find_node(prefix) is not None

    def get_words_with_prefix(self, prefix: str, limit: Optional[int] = None) -> List[str]:
        """
        Return all words that start with the given prefix

        Time: O(p + k) where:
          p = prefix length
          k = total characters in the returned words
        Space: O(k) for the results list
        """
        start_node = self._find_node(prefix)
        if start_node is None:
            return []

        results: List[str] = []

        def dfs(node: TrieNode, path: List[str]) -> None:
            # Stop early if hit the limit
            if limit is not None and len(results) >= limit:
                return

            if node.is_end:
                results.append(prefix + "".join(path))

            for ch, child in node.children.items():
                path.append(ch)
                dfs(child, path)
                path.pop()

        dfs(start_node, [])
        return results

    def delete(self, word: str) -> bool:
        """
        Delete a word from the trie if it exists
        Returns True if the word was deleted

        Time: O(m)
        Space: O(1) extra
        """
        if not word:
            return False

        def _delete(node: TrieNode, index: int) -> bool:
            # Returns True if this node can be pruned by the parent
            if index == len(word):
                if not node.is_end:
                    return False  # word not found
                node.is_end = False
                self._word_count -= 1
                # If no children this node can be removed
                return len(node.children) == 0

            ch = word[index]
            child = node.children.get(ch)
            if child is None:
                return False  # word not found

            should_delete_child = _delete(child, index + 1)
            if should_delete_child:
                del node.children[ch]

            # Return True if this node is useless
            return (not node.is_end) and (len(node.children) == 0)

        return _delete(self.root, 0)

    def count_words(self) -> int:
        """
        Return total number of words stored

        Time: O(1)
        Space: O(1)
        """
        return self._word_count

    def is_empty(self) -> bool:
        """
        Return True if no words are stored

        Time: O(1)
        Space: O(1)
        """
        return self._word_count == 0

    def _find_node(self, string: str) -> Optional[TrieNode]:
        """
        Follow the characters in 'string' down the trie and return
        the final node or None if the path does not exist

        Time: O(len(string))
        Space: O(1)
        """
        node = self.root
        for ch in string:
            node = node.children.get(ch)
            if node is None:
                return None
        return node