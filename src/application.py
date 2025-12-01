from __future__ import annotations
from trie import Trie

def load_words(path: str, limit: int | None = None) -> list[str]:
    """Load words from a text file one word per line"""
    words: list[str] = []

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue
                words.append(word)
                if limit is not None and len(words) >= limit:
                    break
    except FileNotFoundError:
        print(f"Could not find {path}. Starting with an empty trie.")
    return words

def build_trie_from_file(path: str, limit: int | None = None) -> Trie:
    """Create a Trie and insert words"""
    trie = Trie()
    words = load_words(path, limit=limit)
    for w in words:
        trie.insert(w)
    return trie

def print_menu() -> None:
    print("\nMenu")
    print("1) Autocomplete by prefix")
    print("2) Check if a word exists")
    print("3) Insert a new word")
    print("4) Delete a word")
    print("5) Count words")
    print("6) Quit")

def main() -> None:
    print("Trie Autocomplete and Spell Checking")
    trie = build_trie_from_file("../data/words.txt", limit=50000)
    print(f"Loaded {trie.count_words()} words into the trie")

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            prefix = input("Enter a prefix: ").strip().lower()
            if prefix == "":
                print("Please enter a non-empty prefix")
                continue
            suggestions = trie.get_words_with_prefix(prefix, limit=20)
            if suggestions:
                print(f"\nSuggestions for '{prefix}':")
                for w in suggestions:
                    print("  -", w)
            else:
                print("No words found with that prefix")

        elif choice == "2":
            word = input("Enter a word: ").strip().lower()
            if trie.search(word):
                print(f"'{word}' is in the dictionary")
            else:
                print(f"'{word}' is not in the dictionary")

        elif choice == "3":
            word = input("Word to insert: ").strip().lower()
            if not word:
                print("Please enter a non-empty word")
                continue
            trie.insert(word)
            print(f"Inserted '{word}'. Total words: {trie.count_words()}")

        elif choice == "4":
            word = input("Word to delete: ").strip().lower()
            if not word:
                print("Please enter a non-empty word")
                continue
            if trie.delete(word):
                print(f"Deleted '{word}'. Total words: {trie.count_words()}")
            else:
                print(f"'{word}' was not found, nothing deleted")

        elif choice == "5":
            print(f"The trie currently stores {trie.count_words()} words")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 6")

if __name__ == "__main__":
    main()