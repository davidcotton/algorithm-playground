
class BubbleSort:
    """
        Bubble Sort
        ----------

        Time Complexity:
          - Best: O(n)
          - Avg: O(n^2)
          - Worst: O(n^2)

        Space Complexity:
          - O(n)
    """

    def sort(self, l):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(l) - 1):
                if l[i] > l[i + 1]:
                    l[i], l[i + 1] = l[i + 1], l[i]
                    swapped = True
        return l
