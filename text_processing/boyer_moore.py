"""
    Boyer-Moore string searching algorithm.
    Preprocess the string being searched for (the pattern) but not string being searched (the text).
    Use information gathered during the preprocessing to skip sections of the text.
"""


class BoyerMoore:
    @staticmethod
    def search(p, t):
        """
            Time Complexity:
              - Best: O(n / m)
              - Avg: O(n + m)
              - Worst: O(nm)
        """
        pass


if __name__ == '__main__':
    pattern_success = 'pattern'
    pattern_failure = 'failure'
    text = 'looking in this text for pattern'
    print('Success {}'.format(BoyerMoore.search(pattern_success, text)))
    print('Failure {}'.format(BoyerMoore.search(pattern_failure, text)))
