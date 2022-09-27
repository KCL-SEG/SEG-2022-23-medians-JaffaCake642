"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers = sorted(numbers)
if(len(numbers)%2 == 1):
    median = numbers[int(((len(numbers)-1)/2))]
    print(median)
else:
    lowerMedian = numbers[int(len(numbers)/2)-1]
    upperMedian = numbers[int(len(numbers)/2)]
    print((lowerMedian + upperMedian) / 2)
