import pytest
from sorting import quick_sort, bubble_sort, merge_sort, insertion_sort

# filepath: c:\Users\jpayne\Documents\Training\Notebooks for ML classes\AIAssistant2\test_sorting.py

# This is a test file for sorting algorithms.
# It contains unit tests for quick_sort, bubble_sort, and merge_sort functions.
class TestSortingAlgorithms:
    
    # test_quick_sort tests the quick_sort function
    # it checks for various cases including empty list, single element, already sorted, 
    # reverse sorted, and unsorted lists.
    def test_quick_sort(self):
        assert quick_sort([]) == []
        assert quick_sort([1]) == [1]
        assert quick_sort([1, 2, 3]) == [1, 2, 3]
        assert quick_sort([3, 2, 1]) == [1, 2, 3]
        assert quick_sort([5, 3, 8, 3, 1]) == [1, 3, 3, 5, 8]

    # test_bubble_sort tests the bubble_sort function
    # it checks for various cases including empty list, single element, already sorted,
    # reverse sorted, and unsorted lists.
    def test_bubble_sort(self):
        assert bubble_sort([]) == []
        assert bubble_sort([1]) == [1]
        assert bubble_sort([1, 2, 3]) == [1, 2, 3]
        assert bubble_sort([3, 2, 1]) == [1, 2, 3]
        assert bubble_sort([5, 3, 8, 3, 1]) == [1, 3, 3, 5, 8]

    # test_merge_sort tests the merge_sort function
    # it checks for various cases including empty list, single element, already sorted,
    # reverse sorted, and unsorted lists.
    def test_merge_sort(self):
        assert merge_sort([]) == []
        assert merge_sort([1]) == [1]
        assert merge_sort([1, 2, 3]) == [1, 2, 3]
        assert merge_sort([3, 2, 1]) == [1, 2, 3]
        assert merge_sort([5, 3, 8, 3, 1]) == [1, 3, 3, 5, 8]

    # test_insertion_sort tests the insertion_sort function
    # it checks for various cases including empty list, single element, already sorted,
    # reverse sorted, and unsorted lists.
    def test_insertion_sort(self):
        assert insertion_sort([]) == []
        assert insertion_sort([1]) == [1]
        assert insertion_sort([1, 2, 3]) == [1, 2, 3]
        assert insertion_sort([3, 2, 1]) == [1, 2, 3]
        assert insertion_sort([5, 3, 8, 3, 1]) == [1, 3, 3, 5, 8]