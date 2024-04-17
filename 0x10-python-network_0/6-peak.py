#!/usr/bin/python3
""" Finds the peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
    Finds the peak in an unsorted list of integers

    Args:
        list_of_integers: The input list of integers

    Returns:
        int: A peak value from the list if it exists or None
             if the list is empty
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    a = list_of_integers

    left, right = 1, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid - 1] < a[mid] > a[mid + 1]:
            return a[mid]
        elif a[mid - 1] == a[mid] and a[mid] == a[mid + 1]:
            return a[mid - 1]
        elif a[mid - 1] > a[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return None
