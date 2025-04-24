import pytest
from sorting import quick_sort, bubble_sort, merge_sort

# filepath: c:\Users\jpayne\Documents\Training\Notebooks for ML classes\AIAssistant2\test_sorting.py

class TestSortingAlgorithms:
    def test_quick_sort(self):
        assert quick_sort([]) == []
        assert quick_sort([1]) == [1]
        assert quick_sort([1, 2, 3]) == [1, 2, 3]
        assert quick_sort([3, 2, 1]) == [1, 2, 3]
        assert quick_sort([5, 3, 8, 3, 1]) == [1, 3, 3, 5, 8]

    def test_bubble_sort(self):
        assert bubble_sort([]) == []
        assert bubble_sort([1]) == [1]
        assert bubble_sort([1, 2, 3]) == [1, 2, 3]
        assert bubble_sort([3, 2, 1]) == [1, 2, 3]
        assert bubble_sort([5, 3, 8, 3, 1]) == [1, 3, 3, 5, 8]

    def test_merge_sort(self):
        assert merge_sort([]) == []
        assert merge_sort([1]) == [1]
        assert merge_sort([1, 2, 3]) == [1, 2, 3]
        assert merge_sort([3, 2, 1]) == [1, 2, 3]
        assert merge_sort([5, 3, 8, 3, 1]) == [1, 3, 3, 5, 8]