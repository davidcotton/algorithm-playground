"""
    Insertion sort is a simple sorting algorithm.
    Insertion sort builds the final sorted array on item at a time.
"""


class InsertionSort:
    """
        Insertion Sort
        --------------

        Time Complexity:
          - Best: O(n)
          - Avg: O(n^2)
          - Worst: O(n^2)

        Space Complexity:
          - O(1)
    """
    def sort(self, data):
        for i in range(1, len(data)):
            temp = data[i]
            j = i - 1
            while j >= 0 and data[j] > temp:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = temp
        return data


if __name__ == '__main__':
    print(InsertionSort().sort([4, 2, 8, 6, 0, 5, 1, 7, 3, 9]))
