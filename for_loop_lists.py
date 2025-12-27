# names = ["Alice", "Bob", "Charlie", "David"]
# for name in names:
#     print("Hello", name)

# Numbers = [23, 34, 45, 56]
# for num in Numbers:
#     print("Square of", num, "is", num*num)

# test_results = ["Pass", "Fail", "Not_Ran"]
# for i in test_results:
#     if i!= "Pass":
#         print(i, "Issue")


marks = [52,39,67,67, 34, 45, 89, -67, 123, 78, 90, 23, 21, 46, 57, 69]

total = len(marks)
passed = 0
total_sum = 0
high = marks[0]
low = marks[0]
failed = 0
invalid = 0
valid_count = 0

for i in marks:

    if i < 0 or i > 100:
        invalid += 1
        continue   # skip rest of loop for invalid marks

    # only valid marks reach here
    valid_count += 1
    total_sum += i

    if i > high:
        high = i
    if i < low:
        low = i

    if i >= 60:
        passed += 1
    else:
        failed += 1


print("Total students in class:", total)
print("Number of invalid marks entered:", invalid)
print("Total students passed the exam:", passed)
print("Total students failed the exam:", failed)
print("Average of the class is:", total_sum/valid_count )
print("Pass percentage is:", (passed*100)/valid_count)
print("High score in the class is:", high)
print("Low score in the class is:", low)
if invalid > 0:
    print("You entered", invalid, "invalid marks in the list. Please enter valid marks for correct calculations")
    

