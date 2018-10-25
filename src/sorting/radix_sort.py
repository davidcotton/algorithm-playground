"""
    Radix sort is a non-comparative, integer sorting algorithm.
"""


class RadixSort1:
    """
        Radix Sort
        ----------

        Time Complexity:
          - Best: O(wn)
          - Avg: O(wn)
          - Worst: O(wn)

        Space Complexity:
          - O(w + N)
    """
    def sort(self, data):
        n = len(data)
        maxx = max(data)
        exp = 1
        while maxx / exp > 0:
            count = [0] * 10
            temp = [0] * n

            # count frequencies
            for i in range(n):
                index = data[i] // exp
                count[index % 10] += 1

            # calculate prefixes
            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= n:
                index = data[i] // exp
                temp[count[index % 10] - 1] = data[i]
                count[index % 10] -= 1
                i -= 1

            # copy back
            for i in range(n):
                data[i] = temp[i]

            # progress to the next digit
            exp *= 10


class RadixSort2:
    def sort(self, data):
        n = len(data)
        w = max(data)
        exp = 1
        while w / exp > 0:
            count = [0] * n
            temp = []
            # count frequencies
            for i in range(n):
                index = data[i] // exp
                count[index % 10] += 1

            # move records
            for j in range(n):
                derp = count[data[j]]
                temp[derp] = data[j]

            # copy back
            for i in range(n):
                data[i] = temp[i]

            # progress to the next digit
            exp *= 10


class RadixSort3:
    def sort(self, data):
        n = len(data)
        w = len(str(max(data)))
        for x in range(w):
            bins = [[] for _ in range(n)]

            for y in data:
                bins[(y // 10 ** x) % n].append(y)

                data = []
                for section in bins:
                    data.extend(section)

        return data


if __name__ == '__main__':
    l = [6, 12, 8, 6, 0, 5, 1, 17, 3, 9]
    print(RadixSort1().sort(l))
    print(RadixSort2().sort(l))
    print(RadixSort3().sort(l))
