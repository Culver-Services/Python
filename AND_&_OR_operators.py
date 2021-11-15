# Take ABC marks
abc_marks = float(input("Enter the MCQ marks: "))
# Take theory marks
theory_marks = float(input("Enter the Theory marks: "))

# Check the passing condition using AND and OR operator
if (abc_marks >= 40 and theory_marks >= 30) or (abc_marks + theory_marks) >=70:
    print("\nYou have passed")
else:
    print("\nYou have failed")