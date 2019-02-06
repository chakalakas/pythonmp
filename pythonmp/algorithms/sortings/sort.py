import numpy as np

from .mergesort import mergesort as default_sort


def sort(array):
    data = default_sort(array)
    return data
