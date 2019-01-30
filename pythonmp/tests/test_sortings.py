from __future__ import division, absolute_import, print_function

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

import time
import random
import numpy as np
import pandas as pd
from tqdm import tqdm

from pythonmp import sort as pymp_sort
sortings = [sorted, pymp_sort]


def listsEqual(l1, l2):
    if len(l1) != len(l2):
        return False

    for i in xrange(len(l1)):
        if l1[i] != l2[i]:
            return False

    return True


def print_results(test_name, times):
    print ()
    print ("PASSED: ", test_name)
    results = pd.DataFrame(
        [times],
        columns=[str(m.__name__) for m in sortings],
        dtype=np.float)
    print (results.to_string(index=False))


def generate_random_array(container, size, dtype):
    min_int = -100
    max_int = 100

    if dtype not in [int, float]:
        raise TypeError("Invalid data type: {}".format(dtype.__name__))

    if container == list:
        if dtype == int:
            return [random.randint(min_int, max_int) for _ in xrange(size)]
        else:
            return [random.uniform(min_int, max_int) for _ in xrange(size)]
    elif container == tuple:
        if dtype == int:
            return tuple(random.randint(min_int, max_int) for _ in xrange(size))
        else:
            return tuple(random.uniform(min_int, max_int) for _ in xrange(size))
    elif container == np.ndarray:
        if dtype == int:
            return np.random.randint(min_int, max_int, size=size)
        else:
            return np.random.rand(size) * 2 - 1
    else:
        raise TypeError("Cannot generate an array of type {}".format(
            container.__name__))


def generate_test(test, iterations, container, size, dtype):
    times = []

    for i in xrange(len(sortings)):

        time_run = 0
        for _ in xrange(iterations):
            arr = generate_random_array(container, size, dtype)
            arr_sorted_true = sorted(arr)


            current_sort = sortings[i]
            time_start = time.time()
            arr_sorted = current_sort(arr)
            time_run += time.time() - time_start

            # Check correctness
            assert listsEqual(arr_sorted, arr_sorted_true)

        times.append(time_run / iterations)

    print_results(test, times)


def test_list_int_10():
    name = "Container: list, size: 10, dtype: int"
    size = 10
    dtype = int
    iterations = 1000
    container = list
    generate_test(name, iterations, container, size, dtype)


def test_list_int_100():
    name = "Container: list, size: 100, dtype: int"
    size = 100
    dtype = int
    iterations = 300
    container = list
    generate_test(name, iterations, container, size, dtype)


def test_list_int_1000():
    name = "Container: list, size: 1000, dtype: int"
    size = 1000
    dtype = int
    iterations = 100
    container = list
    generate_test(name, iterations, container, size, dtype)


def test_list_int_1e4():
    name = "Container: list, size: 1e4, dtype: int"
    size = int(1e4)
    dtype = int
    iterations = 20
    container = list
    generate_test(name, iterations, container, size, dtype)


def test_list_int_1e5():
    name = "Container: list, size: 1e5, dtype: int"
    size = int(1e5)
    dtype = int
    iterations = 10
    container = list
    generate_test(name, iterations, container, size, dtype)


def test_list_int_1e6():
    name = "Container: list, size: 1e6, dtype: int"
    size = int(1e6)
    dtype = int
    iterations = 5
    container = list
    generate_test(name, iterations, container, size, dtype)


def test_list_int_1e7():
    name = "Container: list, size: 1e7, dtype: int"
    size = int(1e7)
    dtype = int
    iterations = 1
    container = list
    generate_test(name, iterations, container, size, dtype)


def test_list_float_1e5():
    name = "Container: list, size: 1e5, dtype: float"
    size = int(1e5)
    dtype = float
    iterations = 10
    container = list
    generate_test(name, iterations, container, size, dtype)


def test_tuple_int_1e5():
    name = "Container: tuple, size: 1e5, dtype: int"
    size = int(1e5)
    dtype = int
    iterations = 10
    container = tuple
    generate_test(name, iterations, container, size, dtype)


def test_tuple_float_1e5():
    name = "Container: tuple, size: 1e5, dtype: float"
    size = int(1e5)
    dtype = float
    iterations = 10
    container = tuple
    generate_test(name, iterations, container, size, dtype)


def test_ndarray_int_1e5():
    name = "Container: ndarray, size: 1e5, dtype: int"
    size = int(1e5)
    dtype = int
    iterations = 10
    container = np.ndarray
    generate_test(name, iterations, container, size, dtype)


def test_ndarray_float_1e5():
    name = "Container: ndarray, size: 1e5, dtype: float"
    size = int(1e5)
    dtype = float
    iterations = 10
    container = np.ndarray
    generate_test(name, iterations, container, size, dtype)


if __name__ == "__main__":
    test_list_int_10()
    test_list_int_100()
    test_list_int_1000()
    test_list_int_1e4()

    test_list_int_1e5()
    test_list_float_1e5()

    test_tuple_int_1e5()
    test_tuple_float_1e5()

    test_ndarray_int_1e5()
    test_ndarray_float_1e5()
