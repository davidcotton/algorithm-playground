
class InsertionSort:
    """
        Insertion Sort
        --------------

        Time Complexity:
          - Best: O(n)
          - Avg: O(n^2)
          - Worst: O(n^2)

        Space Complexity:
          - O(n)
    """

    def sort(self, l):
        for i in range(1, len(l)):
            temp = l[i]
            j = i - 1
            while j >= 0 and l[j] > temp:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = temp
        return l
