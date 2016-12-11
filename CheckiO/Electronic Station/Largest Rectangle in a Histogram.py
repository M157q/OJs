#!/usr/bin/env python3

# https://py.checkio.org/mission/largest-histogram/


def largest_histogram(histogram):
    # append 0 at the end so we don't have to check if stack is empty again.
    histogram.append(0)

    largest_area = 0
    stack = []
    i = 0

    while i < len(histogram):
        if len(stack) == 0 or histogram[i] > histogram[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            height = histogram[stack.pop()]
            width = i if len(stack) == 0 else i - stack[-1] - 1
            largest_area = max(largest_area, height * width)

    return largest_area


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
