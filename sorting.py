from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sorting algorithms
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort_numbers():
    data = request.json
    numbers = data.get('numbers', [])
    algorithm = data.get('algorithm', 'quick')

    # Validate input
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        return jsonify({'error': 'Invalid input. Please enter numeric values.'}), 400

    if algorithm == 'quick':
        sorted_numbers = quick_sort(numbers)
    elif algorithm == 'bubble':
        sorted_numbers = bubble_sort(numbers)
    elif algorithm == 'merge':
        sorted_numbers = merge_sort(numbers)
    else:
        return jsonify({'error': 'Invalid sorting algorithm'}), 400

    return jsonify({'sorted_numbers': sorted_numbers})

if __name__ == '__main__':
    app.run(debug=True)
