def calculate_grade(marks):
    if marks >= 90:
        return "A","Excellent Work! Keep Shining!"
    elif marks >= 80:
        return "B","Good Job! You're Doing Great!"
    elif marks >= 70:
        return "C","Not Bad! Keep Improving!"
    elif marks >= 60:
        return "D","You Passed! Work a little harder for better results!"
    else:
        return "F","Don't give up! Practice and try again!"
    
print("==== Student Grade Calculator ====")
student_name = input("Enter your name: ")
while True:
    try:
        marks = float(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100. Please try again.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.") 

    except ValueError:
       print("Invalid input! Please enter a numeric value.")

grade, message = calculate_grade(marks)

print("\n===== RESULT =====")
print("Student Name:", student_name)
print("Marks:", marks)
print("Grade:", grade)
print(message)