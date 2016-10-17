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
        m = len(p)
        # check for empty string
        if m == 0:
            return 0
        # set -1 as default for all text chars
        last = {c: -1 for _, c in enumerate(t)}
        #
        for k, c in enumerate(p):
            last[c] = k
        # start with the end of the pattern aligned at index m-1 of the text
        i = k = m - 1
        while i < len(t):
            if t[i] == p[k]:
                if k == 0:
                    return i
                i -= 1
                k -= 1
            else:
                derp = 1 + last[t[i]]
                i += m - (k if k < derp else derp)
                k = m - 1
        return -1


if __name__ == '__main__':
    pattern_success = 'pattern'
    pattern_failure = 'failure'
    text = 'looking in this text for pattern'
    print('Success: {}'.format(BoyerMoore.search(pattern_success, text)))
    print('Failure: {}'.format(BoyerMoore.search(pattern_failure, text)))
