from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Quick sorting algorithm
# Quick sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' 
# element from the array and partitioning the other elements into two sub-arrays, 
# according to whether they are less than or greater than the pivot.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Bubble sorting algorithm
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, 
# compares adjacent elements and swaps them if they are in the wrong order. 
# The pass through the list is repeated until the list is sorted.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Merge sorting algorithm
# Merge sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm.
# It divides the unsorted list into n sublists, each containing one element,
# and then repeatedly merges sublists to produce new sorted sublists until there is only 
# one sublist remaining.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Insertion sorting algorithm
# Insertion sort builds the final sorted array one item at a time.
# It works by taking elements from the unsorted portion and finding the correct
# position to insert them in the sorted portion of the array.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Flask application setup
# The Flask application serves as a web interface for the sorting algorithms.
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle sorting requests
# The '/sort' route accepts POST requests with JSON data containing the numbers to be sorted
@app.route('/sort', methods=['POST'])
def sort_numbers():
    data = request.json
    numbers = data.get('numbers', [])
    algorithm = data.get('algorithm', 'quick')

    # Validate input data
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        return jsonify({'error': 'Invalid input. Please enter numeric values.'}), 400

    # Check which sorting algorithm to use
    if algorithm == 'quick':
        sorted_numbers = quick_sort(numbers)
    elif algorithm == 'bubble':
        sorted_numbers = bubble_sort(numbers)
    elif algorithm == 'merge':
        sorted_numbers = merge_sort(numbers)
    elif algorithm == 'insertion':
        sorted_numbers = insertion_sort(numbers)
    else:
        return jsonify({'error': 'Invalid sorting algorithm'}), 400

    # Return the sorted numbers as JSON response
    # The sorted numbers are returned in a JSON format for easy consumption by the client-side application
    return jsonify({'sorted_numbers': sorted_numbers})

# Run the Flask application
# The application runs on the default Flask development server, which is suitable for 
# testing and development purposes.
if __name__ == '__main__':
    app.run(debug=True)
