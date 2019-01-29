import numpy as np

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


def merge(array, left, mid, right):
    temp_size = right - left
    temp = np.zeros(((temp_size,) + array.shape[1:]))
    cur_left = left
    cur_right = mid

    for cur_temp in xrange(temp_size):
        if cur_left < mid:
            a_left = array[cur_left]
        if cur_right < right:
            a_right = array[cur_right]

        if cur_left < mid and cur_right < right:
            if a_left < a_right: # change to an optional condition
                temp[cur_temp] = a_left
                cur_left += 1
            else:
                temp[cur_temp] = a_right
                cur_right += 1
        elif cur_left < mid:
            temp[cur_temp] = a_left
            cur_left += 1
        elif cur_right < right:
            temp[cur_temp] = a_right
            cur_right += 1

    array[left : right] = temp


def run_mergesort(array, left, right):
    if right - left <= 1:
        return

    mid = (right + left) // 2

    run_mergesort(array, left, mid)
    run_mergesort(array, mid, right)
    merge(array, left, mid, right)


def mergesort(array):
    if not isinstance(array, np.ndarray):
        raise TypeError("An object to sort must be a numpy array")

    size = array.shape[0]
    run_mergesort(array, 0, size)
