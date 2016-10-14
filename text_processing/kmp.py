"""
    KMP.
"""


class KMP:
    @staticmethod
    def search(p, t):
        f = KMP.failure(p)
        i = j = 0
        while i < len(t):
            if t[i] == p[i]:
                if j < len(p) - 1:
                    pass
                else:
                    pass
            else:
                if j > 0:
                    pass
                else:
                    pass
        # no match
        return -1

    @staticmethod
    def failure(p):
        """
        Time complexity:
          - O(m)
        """
        f = [0]
        i = 0
        j = 0
        while i < len(p):
            if p[i] == p[j]:
                # we have matched j+1 chars
                f[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                # use failure func to shift p
                j = f[j - 1]
            else:
                # no match
                f[i] = 0
                i += 1
        return f


if __name__ == '__main__':
    pattern_success = 'pattern'
    pattern_failure = 'failure'
    text = 'looking in this text for pattern'
    print('Success {}'.format(KMP.search(pattern_success, text)))
    print('Failure {}'.format(KMP.search(pattern_failure, text)))
