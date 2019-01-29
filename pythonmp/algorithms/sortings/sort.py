import numpy as np

from .mergesort import mergesort as default_sort


def sort(array):
    if not isinstance(array, np.ndarray):
        data = np.asarray(array)
    else:
        data = array

    default_sort(data)
    return data
