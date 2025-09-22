"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after
each character of searchWord is typed. Suggested products should have common 
prefix with searchWord. If there are more than three products with a common 
prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of 
searchWord is typed.

 

Example 1:

Input: products = [
    "mobile",
    "mouse",
    "moneypot",
    "monitor",
    "mousepad"
    ],

    searchWord = "mouse"

Output: [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
]

Explanation: products sorted lexicographically = ["mobile","moneypot","monitor",
    "mouse","mousepad"].

After typing m and mo all products match and we show user ["mobile","moneypot",
    "monitor"].

After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the 
search word.

 

Constraints:

    1 <= products.length <= 1000
    1 <= products[i].length <= 3000
    1 <= sum(products[i].length) <= 2 * 104
    All the strings of products are unique.
    products[i] consists of lowercase English letters.
    1 <= searchWord.length <= 1000
    searchWord consists of lowercase English letters.
"""

from typing import List

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

    def searchPrefix(self, prefix: str) -> Node:
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')

            if not node.children[index]:
                return None
            node = node.children[index]
        return node
        

    def startsWith(self, prefix: str) -> bool:
        return searchPrefix(prefix) is not None

        
    def findWithPrefix(self, prefix) -> List[str]:

        def impl(n, txt):
            res = []
            if n.end:
                res.append(txt)

            for i in range(0, len(n.children)):
                c = chr(i + ord('a'))

                if n.children[i] is not None:
                    children = impl(n.children[i], txt + c)
                    res.extend(children)
            return res
    
        n = self.searchPrefix(prefix)
        if not n:
            return []
        return impl(n, prefix)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)

        res = []
        
        currentSearchWord = ""
        for key in searchWord:
            currentSearchWord += key

            currentResult = trie.findWithPrefix(currentSearchWord)
            if len(currentResult) > 3:
                currentResult = currentResult[:3]
            res.append(currentResult)
            # print(f'Key: {currentSearchWord}, result: {currentResult}')
        return res





if __name__ == "__main__":
    # trie = Trie()
    # trie.insert("mobile")
    # trie.insert("moneypot")
    # trie.insert("monitor")

    # print(trie.findWithPrefix("mon"))

    obj = Solution()

    expect = [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"]
    ]

    res = obj.suggestedProducts(
        ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        "mouse"
    )

    if res != expect:
        raise Exception(f'Expect {expect}, got {res}')

    obj = Solution()

    expect = [
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"]
    ]

    res = obj.suggestedProducts(["havana"], "havana")

    if res != expect:
        raise Exception(f'Expect {expect}, got {res}')

