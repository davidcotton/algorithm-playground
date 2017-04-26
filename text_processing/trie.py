"""Trie."""


class DefaultTrie:
    def __init__(self):
        self.root = Node


    @staticmethod
    def search(p, t):
        pass

    @staticmethod
    def find(node, key):
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node


class Node:
    def __init__(self):
        self.children = {}

if __name__ == '__main__':
    pattern_success = 'pattern'
    pattern_failure = 'failure'
    text = 'looking in this text for pattern'
    print('Success: {}'.format(DefaultTrie.search(pattern_success, text)))
    print('Failure: {}'.format(DefaultTrie.search(pattern_failure, text)))

