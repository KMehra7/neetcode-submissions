class TrieNode:
        def __init__(self):
            self.children = {}
            self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root
            # print(word)
            for c in range(i, len(word)):
                # print('cur c', word[c])
                #Will check other chs recursivlely
                if word[c] == '.': #The . matches any one of 26 alphabets
                    # return self.dotSearch(c+1, word, cur)
                    for child in cur.children.values():
                        if dfs(c + 1, child):
                            return True
                    return False

                else:
                    #Check next ch iteratively
                    if word[c] not in cur.children:
                        return False
                    cur = cur.children[word[c]]
            return cur.endOfWord
        return dfs(0, self.root)