"""Trie."""


class Trie:
    @staticmethod
    def search(p, t):
        pass


class TrieMap:
    def __init__(self, data):
        self.root = {}
        for (k, v) in data:
            self.add(k, v)

    def add(self, k, v):
        cur = self.root
        for c in k:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['value'] = v

    def query(self, k):
        pass

    @staticmethod
    def search(p, t):
        """Helper method to match the interface used by the other string processing algorithms."""
        trie = TrieMap(t)
        return trie.query(p)


if __name__ == '__main__':
    pattern_success = 'pattern'
    pattern_failure = 'failure'
    text = 'looking in this text for pattern'
    print('Success: {}'.format(TrieMap.search(pattern_success, text)))
    print('Failure: {}'.format(TrieMap.search(pattern_failure, text)))

