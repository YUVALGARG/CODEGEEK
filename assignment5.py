 
# Task 1: Create a Dictionary of Student Marks


# Step 1: Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show not found message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")

# Task 2: Demonstrate List Slicing 
# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Print the original list
print("Original list:", numbers)

# Step 2: Extract the first five elements
first_five = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_first_five = first_five[::-1]

# Step 4: Print both lists
print("First five elements:", first_five)
print("Reversed first five elements:", reversed_first_five)
