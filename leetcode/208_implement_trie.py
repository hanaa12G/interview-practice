"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to 
efficiently store and retrieve keys in a dataset of strings. There are 
various applications of this data structure, such as autocomplete and 
spellchecker.

Implement the Trie class:
```
    Trie() Initializes the trie object.

    void insert(String word) Inserts the string word into the trie.

    boolean search(String word) Returns true if the string word is in the trie 
    (i.e., was inserted before), and false otherwise.

    boolean startsWith(String prefix) Returns true if there is a previously
    inserted string word that has the prefix prefix, and false otherwise.
```
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

 

Constraints:

    1 <= word.length, prefix.length <= 2000

    word and prefix consist only of lowercase English letters.

    At most 3 * 104 calls in total will be made to insert, search, and 
    startsWith.

"""


class Trie:

    class Node:
        def __init__(self):
            self.end = False
            self.children = [None] * (ord('z') - ord('a') + 1)

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str):

        node = self.root
        for c in word:
            index = ord(c) - ord('a')

            if not node.children[index]:
                node.children[index] = Trie.Node()
            node = node.children[index]
        node.end = True
        

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            index = ord(c) - ord('a')

            if not node.children[index]:
                return False
            node = node.children[index]
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')

            if not node.children[index]:
                return False
            node = node.children[index]
        return True
        



if __name__ == "__main__":

    def test(methods, inputs, outputs):
        obj = Trie()
        for method, ip, op in zip(methods, inputs, outputs):
            match method:
                case "Trie":
                    trie = Trie()
                case "insert":
                    res = trie.insert(ip)
                    if res != op:
                        raise Exception(f'(Insert) {ip} Expecting {op}, got {res}')
                case "search":
                    res = trie.search(ip)
                    if res != op:
                        raise Exception(f'(Search) {ip} Expecting {op}, got {res}')
                case "startsWith":
                    res = trie.startsWith(ip)
                    if res != op:
                        raise Exception(f'(StartsWith) {ip} Expecting {op}, got {res}')
                case _:
                    raise Exception(f'Invalid state')


    test(["Trie", "insert", "search", "search", "startsWith", "insert",
          "search"],
         [None, "apple", "apple", "app", "app", "app", "app"],
         [None, None, True, False, True, None, True])
