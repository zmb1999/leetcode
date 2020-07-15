class Trie:
    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        t = self.d
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]  # 字典迭代
        t['end'] = True  # 标记单词终点

    def search(self, word: str) -> bool:
        t = self.d
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return 'end' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.d
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True

"""
apple:{'a': {'p': {'p': {'l': {'e': {'end': True}}}}}}             #第一次insert，最后一个'e'存在结束'end'
app:  {'a': {'p': {'p': {'l': {'e': {'end': True}}, 'end': True}}}}#第二次insert，第二个'p'存在结束'end'
"""
