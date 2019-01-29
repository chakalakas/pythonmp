from __future__ import division, absolute_import, print_function

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

import time
import random
from tqdm import tqdm

from pythonmp import sort as pymp_sort

NUM_ARRAYS_TO_GENERATE = 100
ARRAY_SIZE = 10000


def listsEqual(l1, l2):
    if len(l1) != len(l2):
        return False

    for i in xrange(len(l1)):
        if l1[i] != l2[i]:
            return False

    return True


def test_sortings_1d_uints():
    time_python = 0
    time_pymp = 0

    for i in tqdm(xrange(NUM_ARRAYS_TO_GENERATE)):
        l = [random.randint(0, 1000) for _ in xrange(ARRAY_SIZE)]

        time_python_start = time.time()
        l_sorted_python = sorted(l)
        time_python += time.time() - time_python_start

        time_pymp_start = time.time()
        l_sorted_our = pymp_sort(l)
        time_pymp = time.time() - time_pymp_start

        assert listsEqual(l_sorted_our, l_sorted_python)

    time_python = time_python / NUM_ARRAYS_TO_GENERATE
    time_pymp = time_pymp / NUM_ARRAYS_TO_GENERATE

    max_t = max(time_pymp, time_python)
    min_t = min(time_pymp, time_python)
    ratio = (max_t - min_t) / min_t * 100

    print ("PyMP sort is CORRECT")
    print ("PyMP sort is in average {}% {}".format(ratio,
        "faster" if time_pymp < time_python else "slower"))
    print ("Python sort time: {}".format(time_python))
    print ("PyMP   sort time: {}".format(time_pymp))


def test_sortings_1d_int():
    pass


def test_sortings_1d_float32():
    pass


def test_sortings_1d_float64():
    pass


def test_sortings_1d_string():
    pass


if __name__ == "__main__":
    test_sortings_1d_uints()
    test_sortings_1d_int()
    test_sortings_1d_float32()
    test_sortings_1d_float64()
    test_sortings_1d_string()
