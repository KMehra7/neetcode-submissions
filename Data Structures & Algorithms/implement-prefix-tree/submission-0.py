class PrefixTreeNode:
    def __init__(self):
        # self.children = [0] * 26
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = PrefixTreeNode()
            cur = cur.children[ch]
            #If we use an array
            # if cur.children[ord(ch)-ord('a')] == None:
                # cur.children[ord(ch)-ord('a')] = PrefixTreeNode()
            # cur = cur.children[ord(ch)-ord('a')]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
            #If we use an array
            # if cur.children[ord(ch)-ord('a')] == None:
            #    return False
            # cur = cur.children[ord(ch)-ord('a')]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
            #If we use an array
            # if cur.children[ord(ch)-ord('a')] == None:
            #    return False
            # cur = cur.children[ord(ch)-ord('a')]
        return True
        