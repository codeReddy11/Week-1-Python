def analyze_marks(marks):
    total = len(marks)
    passed = failed = invalid = valid_count = total_sum = average =0
    high = low = None
    grade_a = grade_b = grade_c = grade_d = grade_f = 0

    for i in marks:

        if i < 0 or i > 100:
            invalid += 1
            continue
# this is test

#the comment is been added here directly in the GIT and practice the code pull from repo to local branch

        valid_count += 1
        total_sum += i

        if high is None or i > high:
            high = i
        if low is None or i < low:
            low = i

        if i >= 60:
            passed += 1
        else:
            failed += 1

        if i >= 90:
            grade_a += 1
        elif i >= 75:
            grade_b += 1
        elif i >= 60:
            grade_c += 1
        elif i >= 40:
            grade_d += 1
        else:
            grade_f += 1
        
        average = total_sum / valid_count

    return {
        "total": total,
        "valid": valid_count,
        "invalid": invalid,
        "passed": passed,
        "failed": failed,
        "average": average,
        "high": high,
        "low": low,
        "A": grade_a,
        "B": grade_b,
        "C": grade_c,
        "D": grade_d,
        "F": grade_f
    }

# marks = [52, 39, 67, 67, 34, 45, 89, 78, 90, 23, 21, 46, 57, 69]

# result = analyze_marks(marks)

# print("Total students:", result["total"])
# print("Valid marks:", result["valid"])
# print("Invalid marks:", result["invalid"])
# print("Passed:", result["passed"])
# print("Failed:", result["failed"])
# print("Average:", result["average"])
# print("High:", result["high"])
# print("Low:", result["low"])
# print("Grade A:", result["A"])
# print("Grade B:", result["B"])
# print("Grade C:", result["C"])
# print("Grade D:", result["D"])
# print("Grade F:", result["F"])

# Test cases:

#Test case 1:
marks1 = [70, 80, 90]

result1 = analyze_marks(marks1)

if result1["passed"] == 3:
    print("Test 1 Passed: All Passed")
else:
    print("Test 1 Failed")

#Test case 2
marks2 = [30, 60, 75]

result2 = analyze_marks(marks2)

if result2["passed"] == 2 and result2["failed"] == 1:
    print("Test 2 Passed: Pass/Fail count correct")
else:
    print("Test 2 Failed")

#Test case 3
marks3 = [50, -10, 120, 80]

result3 = analyze_marks(marks3)

if result3["invalid"] == 2:
    print("Test 3 Passed: Invalid marks detected")
else:
    print("Test 3 Failed")

#Test case 4
marks4 = [50, 100, -30]

result4 = analyze_marks(marks4)

expected_avg = 75

if result4["average"] == expected_avg:
    print("Test 4 Passed: Average correct")
else:
    print("Test 4 Failed")

#Test case 5

marks5 = [-5, 200]

result5 = analyze_marks(marks5)

if result5["valid"] == 0 and result5["invalid"] == 2:
    print("Test 5 Passed: All invalid handled")
else:
    print("Test 5 Failed")

#Test case 6

marks6 = [39, 99, 80]

result6 = analyze_marks(marks6)

if result6["A"] == 1 and result6["F"] == 1:
    print("Test 6 Passed: Grades are correct")
else:
    print("Test 6 Failed")



