"""
    Bubble sort is a simple sorting algorithm.
    Bubble sort compares each adjacent pair of items and swaps them if they are in the wrong order.
"""


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
    def sort(self, data):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(data) - 1):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swapped = True
        return data


if __name__ == '__main__':
    print(BubbleSort().sort([20, 6, 12, 16, 4, 10, 2, 6, 16, 13]))
