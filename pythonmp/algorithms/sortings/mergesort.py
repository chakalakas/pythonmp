from __future__ import division, absolute_import, print_function
from .insertionsort import insertionsort

import numpy as np
from multiprocessing import Process

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


def merge(array, left, mid, right):
    temp_size = right - left
    temp = np.zeros(temp_size) # 1d array only for now
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


def run_parallel(target, args=()):
    p = Process(target, args)
    p.start()
    return p


def run_mergesort(array, left, right, insertions=False):
    INSERTIONS_SIZE = 10

    if right - left <= 1:
        return

    if insertions and right-left <= INSERTIONS_SIZE:
        insertionsort(array, left, right)
        return

    mid = (right + left) // 2

    run_mergesort(array, left, mid)

    # parallel another part of the recursion
    pms = run_parallel(run_mergesort, (array, mid, right))
    pms.join()

    run_mergesort(array, mid, right)
    merge(array, left, mid, right)


def mergesort(array):
    if not isinstance(array, np.ndarray):
        data = np.asarray(array)
    else:
        data = array

    size = data.shape[0]
    run_mergesort(data, 0, size)
    return data


def mergesort_insertions(array):
    if not isinstance(array, np.ndarray):
        data = np.asarray(array)
    else:
        data = array

    size = data.shape[0]
    run_mergesort(data, 0, size, insertions=True)
    return data
