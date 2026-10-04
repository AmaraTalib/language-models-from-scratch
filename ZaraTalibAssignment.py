# BanoQabil Assignment 2

# Store the numbers in a list
numbers_list = [45, 78, 23, 91, 56, 34, 89, 12]

# Find the count and sum
count = len(numbers_list)
total = sum(numbers_list)

# Calculate the average
average = total / count

# Find the highest and lowest numbers
highest = max(numbers_list)
lowest = min(numbers_list)

# Display the results
print("Numbers:", numbers_list)
print("Count:", count)
print("Sum:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)

# Display numbers from highest to lowest
print("Highest to lowest:")

for num in sorted(numbers_list, reverse=True):
    print(num)