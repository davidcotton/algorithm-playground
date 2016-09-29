
class MergeSort:
    """
        Merge Sort
        ----------

        Time Complexity:
          - Best: O(n log n)
          - Avg: O(n log n)
          - Worst: O(n log n)

        Space Complexity:
          - O(n)
    """

    def sort(self, l):
        if len(l) < 2:
            return

        mid = len(l) // 2
        l1 = l[0:mid]
        l2 = l[mid:len(l)]

        self.sort(l1)
        self.sort(l2)

        self.merge(l1, l2, l)

    def merge(self, l1, l2, l):
        """Merge two sorted sequences."""
        i = j = 0
        while i + j < len(l):
            if j == len(l2) or (i < len(l1) and l1[i] < l2[j]):
                l[i + j] = l1[i]
                i += 1
            else:
                l[i + j] = l2[j]
                j += 1


class MergeSortStrict:
    """
        Merge Sort
        ----------

        Time Complexity:
          - Best: O(n log n)
          - Avg: O(n log n)
          - Worst: O(n log n)

        Space Complexity:
          - O(n)
    """

    def sort(self, l):
        if len(l) < 2:
            return l

        mid = len(l) // 2
        l1 = l[0:mid]
        l2 = l[mid:len(l)]

        l1 = self.sort(l1)
        l2 = self.sort(l2)

        return self.merge(l1, l2, l)

    def merge(self, l1, l2, l):
        """Merge two sorted sequences."""
        i = j = 0
        while i + j < len(l):
            if j == len(l2) or (i < len(l1) and l1[i] < l2[j]):
                l[i + j] = l1[i]
                i += 1
            else:
                l[i + j] = l2[j]
                j += 1
        return l

# data = [4, 2, 8, 6, 0, 5, 1, 7, 3, 9]
