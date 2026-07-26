LINE_EQUAL = "=" * 50
LINE_DASH  = "-" * 50
NUMBER_OF_SUBJECTS = 5

user_choice : str = "1"
result : str = ""
student_id : str = ""
student_name : str = ""    
tamil_mark : float = 0.0
english_mark : float = 0.0
math_mark : float = 0.0
science_mark : float = 0.0
social_mark : float = 0.0
total_mark : float = 0.0
average_mark : float = 0.0

def add_student():
    global student_id, student_name, tamil_mark, english_mark, math_mark, science_mark, social_mark    
    try:
        student_id      = input("Enter student ID      :")
        student_name    = input("Enter student Name    :")
        tamil_mark      = float(input("Tamil Mark      :"))
        if not validate_marks(tamil_mark):
            print("Invalid Tamil mark. Please enter a value between 0 and 100.")
            return add_student()
        english_mark    = float(input("English Mark    :"))
        if not validate_marks(english_mark):
            print("Invalid English mark. Please enter a value between 0 and 100.")
            return add_student()
        math_mark       = float(input("Math Mark       :"))
        if not validate_marks(math_mark):
            print("Invalid Math mark. Please enter a value between 0 and 100.")
            return add_student()
        science_mark    = float(input("Science Mark    :"))
        if not validate_marks(science_mark):
            print("Invalid Science mark. Please enter a value between 0 and 100.")
            return add_student()
        social_mark     = float(input("Social Mark     :"))
        if not validate_marks(social_mark):
            print("Invalid Social mark. Please enter a value between 0 and 100.")
            return add_student()
    except ValueError:
        print("Invalid input for marks. Please enter numeric values.")
        return add_student()
    
def validate_marks(mark : float) -> bool:
    return 0 <= mark <= 100

def calculate_total_marks(tamil_mark, english_mark, math_mark, science_mark, social_mark) -> float:
    return tamil_mark + english_mark + math_mark + science_mark + social_mark

def calculate_average_marks(total_mark : float) -> float:
    return total_mark / NUMBER_OF_SUBJECTS

def calculate_grade(average_mark : float) -> str:
    if average_mark >= 90:
        return "A"
    elif average_mark >= 80:
        return "B"
    else:
        return "C"

def calculate_result(tamil_mark : float, english_mark : float, math_mark : float, science_mark : float, social_mark : float) -> str:
    if tamil_mark >= 35 and english_mark >= 35 and math_mark >= 35 and science_mark >= 35 and social_mark >= 35:
        return "Pass"
    else:
        return "Fail"

def display_student_details(student_id : str, student_name : str, tamil_mark : float, english_mark : float, math_mark : float, science_mark : float, social_mark : float):
    print(LINE_EQUAL)
    print("{:^50}".format("Student Details"))
    print(LINE_EQUAL)
    print(f"Student ID      : {student_id}")
    print(f"Student Name    : {student_name}")
    print(f"Tamil Mark      : {tamil_mark:.2f}")
    print(f"English Mark    : {english_mark:.2f}")
    print(f"Math Mark       : {math_mark:.2f}")
    print(f"Science Mark    : {science_mark:.2f}")
    print(f"Social Mark     : {social_mark:.2f}")
    print(LINE_DASH)
    total_marks = calculate_total_marks(tamil_mark, english_mark, math_mark, science_mark, social_mark)
    average_marks = calculate_average_marks(total_marks)
    grade = calculate_grade(average_marks)
    result = calculate_result(tamil_mark, english_mark, math_mark, science_mark, social_mark)

    print(f"Total Marks     : {total_marks}")
    print(f"Average Marks   : {average_marks:.2f}")
    print(f"Grade           : {grade}")
    print(f"Result          : {result}")
    print(LINE_DASH) 

def main():
    user_choice = "1"
    while user_choice != "3":
        print(LINE_EQUAL)
        print("{:^50}".format("Student Management System"))
        print(LINE_EQUAL)
        print("1. Add Student")
        print("2. View Student Details")
        print("3. Exit")
        user_choice = input("\n Enter your choice (1-3): ")
        if user_choice == "1":
            add_student()
        elif user_choice == "2":
            display_student_details(student_id, student_name, tamil_mark, english_mark, math_mark, science_mark, social_mark)
        elif user_choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            main()

if __name__ == "__main__":
    main() 
