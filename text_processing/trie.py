"""Trie."""


class DefaultTrie:
    @staticmethod
    def search(p, t):
        pass


if __name__ == '__main__':
    pattern_success = 'pattern'
    pattern_failure = 'failure'
    text = 'looking in this text for pattern'
    print('Success: {}'.format(DefaultTrie.search(pattern_success, text)))
    print('Failure: {}'.format(DefaultTrie.search(pattern_failure, text)))

