# TREE_DESIGN.md
## Tree Selection
Which tree did you choose and why? We chose the Trie (Prefix Tree) as it's very good at word and prefix-based tasks like autocomplete and spell checking. These features are common in real apps (search bars, code editors, messaging apps) and the operations are easier to implement than a self-balancing tree while still being powerful.

## Use Cases
What problems does this tree solve well? 
- Autocomplete for:
  - Dictionary words
  - City names/course titles
  - Commands in a CLI
  - Any operation that involves a search
- Spell checking and “did you mean?” style suggestions, typically seen in browsers
- Quickly finding all words that start with a given prefix
- Efficiently storing large word sets that share prefixes

## Properties
What makes this tree unique? 
- Each node represents a character
- Paths from root node represent prefixes of words
- Words are marked by a boolean is_end flag
- Many strings can share large portions of memory due to overlapping prefixes
- Performance depends on input length, not the number of stored words
What are its performance characteristics?
- Insert is O(m)
- Search is O(m)
- Starts With is O(p)
- Prefix Query is O(p + k)
- Delete is O(m)
- Space is O(n·m) worst case but often less due to prefix sharing

## Interface Design 
Method signatures with descriptions
What operations does your tree support? insert words, search for words, delete words, get suggestions
What are the parameters and return types?
- insert(word): adds a word to the trie
- search(word): checks if a word exists
- starts_with(prefix): checks if any words start with a prefix
- get_words_with_prefix(prefix): returns autocomplete suggestions
- delete(word): removes a word
- count_words(): tells you how many words are stored
What is the Big-O time complexity of each operation? (Required for every method)
- insert is O(m), where m = word length
- search is O(m)
- starts_with is O(p) where p = prefix length
- get_words_with_prefix is O(p + k) p = prefix k = size of results
- delete is O(m)
What is the space complexity? (if relevant)
- n = number of words
- m = average word length
Some use no extra memory (O(1))
Some store results in a list (O(k))

## Implementation Notes 
Key algorithms or techniques you'll use
- children: dict[str, TrieNode] which maps of characters to children
- is_end: bool which marks if a node ends a word
- Insert: Walk the characters of the word create nodes as needed set is_end = True
- Search: Walk character by character and return True only if the final node is is_end
- Starts With: Same as search but stops early and checks only node existence
- Prefix Retrieval (get_words_with_prefix): Walk down to the node for the prefix (O(p))
- Delete: A recursive helper removes a word and prunes nodes only if unused by other words
- Count Words: A simple integer counter tracks insertions/deletions is O(1)
