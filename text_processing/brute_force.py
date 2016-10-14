"""Brute force pattern matching."""


class BruteForce:
    @staticmethod
    def search(p, t):
        """
            Time Complexity:
              - O(n - m + 1)
        """
        n = len(t)
        m = len(p)
        for i in range(n - m + 1):
            k = 0
            while k < m and t[i + k] == p[k]:
                k += 1
            if k == m:
                return i
        return -1


if __name__ == '__main__':
    pattern_success = 'pattern'
    pattern_failure = 'failure'
    text = 'looking in this text for pattern'
    print('Success {}'.format(BruteForce.search(pattern_success, text)))
    print('Failure {}'.format(BruteForce.search(pattern_failure, text)))
