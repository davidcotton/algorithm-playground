"""
    Selection sort is an in place comparison sort.
    Selection sort divides the list into into two lists: one sorted and one to sort.
    The algorithm proceeds by finding the smallest element in the unsorted list
    and swapping it into the sorted list.
"""


class SelectionSort:
    """
        Selection Sort
        --------------

        Time Complexity:
          - Best: O(n^2)
          - Avg: O(n^2)
          - Worst: O(n^2)

        Space Complexity:
          - O(1)
    """

    def sort(self, data):
        for j in range(len(data)):
            i_min = j
            for i in range(j + 1, len(data)):
                if data[i] < data[i_min]:
                    i_min = i
            data[i_min], data[j] = data[j], data[i_min]
        return data


if __name__ == '__main__':
    print(SelectionSort().sort([4, 2, 8, 6, 0, 5, 1, 7, 3, 9]))
