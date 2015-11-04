#!/usr/bin/env python
__author__ = 'RamiC'

from operator import itemgetter as getter


def sortinplace(items):
    """
    Sort items inplace per type (str and int supported) given the condition that
    the same types will occupy the same positions after the sort

    :param items: A list of string objects possibly containing digit chars
    :type items: list
    :return: A list of 'inplace per type' sorted items
    :rtype : list

    :Example:
    >sortinplace(['car', 'truck', '8', '4', 'bus', '6', '-1'])
    ['bus', 'car', '-1', '4', 'truck', '6', '8'])

    """
    # filter out indexes for both types, use comprehensions for readability
    # and compactness since input is small
    iidx = [i for i, item in enumerate(items) if item.strip('-').isdigit()]
    oidx = [i for i, item in enumerate(items) if not item.strip('-').isdigit()]

    # Sort indexes based on the value it points to
    siidx = sorted(iidx, key=lambda idx: int(items[idx]))
    soidx = sorted(oidx, key=lambda idx: items[idx])

    # Map the positions pre and post sort, merge the result and sort again
    # based on the pre sort keys.
    msidx = sorted(zip(iidx, siidx) + zip(oidx, soidx), key=getter(0))

    return [items[i[1]] for i in msidx]


def test_sort():
    fixtures = [
        (['1'], ['1']),
        (['car', 'truck', 'bus'], ['bus', 'car', 'truck']),
        (['8', '4', '6', '1', '-2', '9', '5'], ['-2', '1', '4', '5', '6', '8', '9']),
        (['car', 'truck', '8', '4', 'bus', '6', '1'], ['bus', 'car', '1', '4', 'truck', '6', '8']),
        (['car', 'truck', '8', '4', 'bus', '6', '-1'], ['bus', 'car', '-1', '4', 'truck', '6', '8']),
    ]
    for fx in fixtures:
        assert sortinplace(fx[0]) == fx[1], "Test failed with input %s, output %s" % fx
    print("All tests passed")

if __name__ == "__main__":
    import sys
    f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    print(' '.join(sortinplace(f.read(1000).split())))