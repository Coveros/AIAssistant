Feature: Sorting numbers using different algorithms
    As a user of the sorting application
    I want to sort a list of numbers using various sorting algorithms
    So that I can see the sorted output

  Scenario: Sorting numbers using Quick Sort
    Given I open the sorting application
    When I enter 5, 3, 8, 1 as numbers
    And I select Quick Sort from the dropdown
    And I click the Sort button
    Then I should see 1, 3, 5, 8 in the sorted numbers area

  Scenario: Sorting numbers using Bubble Sort
    Given I open the sorting application
    When I enter 9, 7, 2, 6 as numbers
    And I select Bubble Sort from the dropdown
    And I click the Sort button
    Then I should see 2, 6, 7, 9 in the sorted numbers area

  Scenario: Sorting numbers using Merge Sort
    Given I open the sorting application
    When I enter 4, 10, 3, 8 as numbers
    And I select Merge Sort from the dropdown
    And I click the Sort button
    Then I should see 3, 4, 8, 10 in the sorted numbers area