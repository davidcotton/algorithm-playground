"""
    Knuth-Morris-Pratt (KMP) text search algorithm.
    The KMP text searching algorithm optimises the time required to scan a document by bypassing
    re-examination of previously matched characters.
"""


class KMP:
    @staticmethod
    def search(pattern, text):
        n = len(text)
        m = len(pattern)

        # trivial search for empty string
        if m == n:
            return 0

        # compute failure function
        fail = KMP.failure(pattern)
        i = j = 0
        while i < n:
            if text[i] == pattern[j]:
                if j == m - 1:
                    # match complete
                    return i - m + 1
                # otherwise try to extended match
                i += 1
                j += 1
            elif j > 0:
                j = fail[j - 1]
            else:
                i += 1
        # no match
        return -1

    @staticmethod
    def failure(p):
        """
        Time complexity:
          - O(m)
        Space complexity:
          - O(m)
        """
        m = len(p)
        fail = [0] * m
        i = 1
        j = 0
        while i < m:
            if p[i] == p[j]:
                # we have matched j+1 chars
                fail[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                # use failure func to shift p
                j = fail[j - 1]
            else:
                # no match
                i += 1
        return fail


if __name__ == '__main__':
    # pattern_success = 'pattern'
    # pattern_failure = 'failure'
    # text = 'looking in this text for pattern'
    # print('Success: {}'.format(KMP.search(pattern_success, text)))
    # print('Failure: {}'.format(KMP.search(pattern_failure, text)))

    # pattern = 'abcdabca'
    pattern = 'abcaby'
    text = 'abxabcabcaby'
    print('Success: {}'.format(KMP.search(pattern, text)))
