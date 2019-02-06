from __future__ import division, absolute_import, print_function

import numpy as np

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


def insertionsort(array, left=0, right=-1):
    if not isinstance(array, np.ndarray):
        data = np.asarray(array)
    else:
        data = array

    if right == -1:
        right = data.shape[0]

    if right - left <= 1:
        return data

    for i in xrange(left + 1, right):
        for j in xrange(i - 1, left - 1, -1):
            cur_pos = j + 1
            if data[j] > data[cur_pos]:
                temp = data[cur_pos]
                data[cur_pos] = data[j]
                data[j] = temp
            else:
                break

    return data
