class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for character in word:
            if character not in currentNode.children:
                currentNode.children[character] = TrieNode()
            currentNode = currentNode.children[character]
        currentNode.endOfWord = True

    def search(self, word: str) -> bool:
        currentNode = self.root
        for character in word:
            if character not in currentNode.children:
                return False
            currentNode = currentNode.children[character]
        return currentNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for character in prefix:
            if character not in currentNode.children:
                return False
            currentNode = currentNode.children[character]
        return True


obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
print(param_2)
param_3 = obj.startsWith("app")
print(param_3)
