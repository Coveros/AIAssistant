# This file contains BDD tests for sorting algorithms using pytest-bdd and SeleniumBase.
# It includes scenarios for quick sort, bubble sort, and merge sort for the following user story:

# Feature: Sorting numbers using different algorithms
#     As a user of the sorting application
#     I want to sort a list of numbers using various sorting algorithms
#     So that I can see the sorted output

from pytest_bdd import scenario, given, when, then
import seleniumbase as sb

# Constants
PAGE = 'http://localhost:5000'

# BDD test for quick sort scenario
# Scenario: Sorting numbers using Quick Sort
#    Given I open the sorting application
#    When I enter 5, 3, 8, 1 as numbers
#    And I select Quick Sort from the dropdown
#    And I click the Sort button
#    Then I should see 1, 3, 5, 8 in the sorted numbers area

@scenario('features/sorting_app.feature', 'Sorting numbers using Quick Sort')
def test_quick_sort():
    pass

@given('I open the sorting application')
def step_open_sorting_application(sb):
    sb.get(PAGE)

@when('I enter 5, 3, 8, 1 as numbers')
def step_enter_numbers(sb):
    sb.type("#numbers", "5, 3, 8, 1")

@when('I select Quick Sort from the dropdown')
def step_select_quick_sort(sb):
    sb.select_option_by_value("#algorithm", "quick")
    sb.click("#algorithm")

@when('I click the Sort button')
def step_click_sort_button(sb):
    sb.click("button:contains('Sort')")

@then('I should see 1, 3, 5, 8 in the sorted numbers area')
def step_see_sorted_numbers(sb):
    sb.assert_text("1, 3, 5, 8", "#sortedNumbers")
    sb.sleep(2)

# BDD test for bubble sort 
# Scenario: Sorting numbers using Bubble Sort
#     Given I open the sorting application
#     When I enter 9, 7, 2, 6 as numbers
#     And I select Bubble Sort from the dropdown
#     And I click the Sort button
#     Then I should see 2, 6, 7, 9 in the sorted numbers area

@scenario('features/sorting_app.feature', 'Sorting numbers using Bubble Sort')
def test_bubble_sort():
    pass

@given('I open the sorting application')
def step_open_sorting_application(sb):
    sb.get(PAGE)

@when('I enter 9, 7, 2, 6 as numbers')
def step_enter_numbers(sb):
    sb.type("#numbers", "9, 7, 2, 6")

@when('I select Bubble Sort from the dropdown')
def step_select_quick_sort(sb):
    sb.select_option_by_value("#algorithm", "bubble")
    sb.click("#algorithm")

@when('I click the Sort button')
def step_click_sort_button(sb):
    sb.click("button:contains('Sort')")

@then('I should see 2, 6, 7, 9 in the sorted numbers area')
def step_see_sorted_numbers(sb):
    sb.assert_text("2, 6, 7, 9", "#sortedNumbers")
    sb.sleep(2)

# BDD test for merge sort
# Scenario: Sorting numbers using Merge Sort
#     Given I open the sorting application
#     When I enter 4, 10, 3, 8 as numbers
#     And I select Merge Sort from the dropdown
#     And I click the Sort button
#     Then I should see 3, 4, 8, 10 in the sorted numbers area

@scenario('features/sorting_app.feature', 'Sorting numbers using Merge Sort') 
def test_merge_sort():
    pass

@given('I open the sorting application')
def step_open_sorting_application(sb):
    sb.get(PAGE)

@when('I enter 4, 10, 3, 8 as numbers')
def step_enter_numbers(sb):
    sb.type("#numbers", "3, 4, 8, 10")

@when('I select Merge Sort from the dropdown')
def step_select_quick_sort(sb):
    sb.select_option_by_value("#algorithm", "merge")
    sb.click("#algorithm")

@when('I click the Sort button')
def step_click_sort_button(sb):
    sb.click("button:contains('Sort')")

@then('I should see 3, 4, 8, 10 in the sorted numbers area')
def step_see_sorted_numbers(sb):
    sb.assert_text("3, 4, 8, 10", "#sortedNumbers")
    sb.sleep(2)

# BDD test for insertion sort
# Scenario: Sorting numbers using Insertion Sort
#     Given I open the sorting application
#     When I enter 7, 2, 9, 1 as numbers
#     And I select Insertion Sort from the dropdown
#     And I click the Sort button
#     Then I should see 1, 2, 7, 9 in the sorted numbers area

@scenario('features/sorting_app.feature', 'Sorting numbers using Insertion Sort') 
def test_insertion_sort():
    pass

@given('I open the sorting application')
def step_open_sorting_application(sb):
    sb.get(PAGE)

@when('I enter 7, 2, 9, 1 as numbers')
def step_enter_numbers(sb):
    sb.type("#numbers", "7, 2, 9, 1")

@when('I select Insertion Sort from the dropdown')
def step_select_insertion_sort(sb):
    sb.select_option_by_value("#algorithm", "insertion")
    sb.click("#algorithm")

@when('I click the Sort button')
def step_click_sort_button(sb):
    sb.click("button:contains('Sort')")

@then('I should see 1, 2, 7, 9 in the sorted numbers area')
def step_see_sorted_numbers(sb):
    sb.assert_text("1, 2, 7, 9", "#sortedNumbers")
    sb.sleep(2)