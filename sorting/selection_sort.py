# Selection Sort
#
# Best : O(n^2)
# Avg  : O(n^2)
# Worst: O(n^2)
# Space: O(1)


def selection_sort(data):
    """Selection sort. """
    for j in range(len(data)):
        i_min = j
        for i in range(j + 1, len(data)):
            if data[i] < data[i_min]:
                i_min = i
        data[i_min], data[j] = data[j], data[i_min]
    return data


l = [64, 25, 12, 22, 11]
print(selection_sort(l))
