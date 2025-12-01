# Project 3 Tree Applications
## Project Title and Description
What tree did you implement? We implemented the Trie (prefix tree) from scratch in Python and uses it in a small command line application that provides:
- Autocomplete suggestions based on a typed prefix
- Exact word lookup spell checking
- Inserting and deleting words
- Viewing how many words are stored
The goal is to show how a Trie can efficiently handle prefix based search
compared to a simple list or array.

Who would use this and why?
- Students learning data structures who want to see a Trie working in a real application
- Developers experimenting with basic autocomplete/spell helper functionality
- Anyone curious how search bars and code editors can show live suggestions

## Team Members
Names: Mallory Tolliver and Connor Murphy

## Installation & Setup
Prerequisites: Python 3.10 or above
How to run:
- cd src
- python3 application.py

## Usage Guide
When you run the program, you will see a menu:
1) Autocomplete by prefix
2) Check if a word exists
3) Insert a new word
4) Delete a word
5) Count words
6) Quit
These mean:
Autocomplete: Enter a prefix like "app" to see up to 20 matching words
Search: Type a full word to check if it exists
Insert: Add a new word into the trie
Delete: Remove a word
Count: Displays the number of words currently in the trie
Quit: Exit the program

## Screenshots/Demos
Main Menu which shows the app startup
Autocomplete Example which shows suggestions for a prefix
Insert/Delete/Count Example which shows modifying the trie and verifying changes

## Tree Implementation Details
- Tree Type: Trie (Prefix Tree)
- Main Operations Used in the App:
  - `insert(word)`
  - `search(word)`
  - `starts_with(prefix)`
  - `get_words_with_prefix(prefix, limit)`
  - `delete(word)`
  - `count_words()`

## Evolution of the Interface
What changed from your initial design?
Initial design:
- insert
- search
- starts_with
- delete
- get_words_with_prefix
Changed:
- count_words() to show the total number of items in the CLI
- limit parameter for get_words_with_prefix to avoid printing hundreds of words
- Internal helper _find_node() to simplify repeated traversal logic
Why did you need those changes?
Building the CLI revealed what information the user needs to see and what helper functions simplified the code
What did you learn from this iterative process?
- Designing an interface upfront is hard and building the application exposes missing functionality
- Small helper methods reduce duplication
- Real applications often drive the tree’s final interface

## Challenges & Solutions
Implementing delete correctly
- Challenge: Removing nodes without breaking prefixes for other words
- Solution: We used a recursive helper that returns whether a node can safely be deleted
Handling large word lists
- Challenge: Printing too many autocomplete results at once
- Solution: Added a limit parameter
Keeping the application simple but functional
- Challenge: Avoiding feature bloat while still meeting assignment goals
- Solution: Focused on autocomplete + basic word operations, which clearly demonstrate Trie advantages

## Future Enhancements
- Implement spell checking/edit distance suggestions
- Add time comparison against a list based search
- Allow exporting and saving the trie to file