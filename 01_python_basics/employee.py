LINE = "-" * 50
def calculate_annual_salary(monthly_salary : float) -> float:
    return monthly_salary * 12

def display_employee_details(name : str, emp_id : str, department : str, monthly_salary : float):
    annual_salary = calculate_annual_salary(monthly_salary)
    employee_category = "Senior Employee" if monthly_salary > 50000 else "Junior Employee"
    print(LINE)
    print("{:^50}".format("Employee Details"))
    print(LINE)
    print(f"ID             : {emp_id}")
    print(f"Name           : {name}")
    print(f"Department     : {department}")
    print(f"Monthly Salary : ${monthly_salary:.2f}")
    print(f"Annual Salary  : ${annual_salary:.2f}")
    print(f"Category       : {employee_category}")
    print(LINE)

def get_employee_details() -> tuple[str, str, str, float]:
    try:
        employee_name = input("Enter employee name: ")
        employee_id = input("Enter employee ID: ")
        employee_department = input("Enter employee department: ")
        employee_monthly_salary = float(input("Enter employee monthly salary: "))
        return employee_name, employee_id, employee_department, employee_monthly_salary
    except ValueError:
        print("Invalid input for monthly salary. Please enter a numeric value.")
        return get_employee_details()      

def main(): 
    print("Employee Management System")
    add_employee : str = "Y"
    while add_employee == "Y":
        employee_name, employee_id, employee_department, employee_monthly_salary = get_employee_details()
        display_employee_details(employee_name, employee_id, employee_department, employee_monthly_salary)
        add_employee = input("\nDo you want to add another employee? (Y/N): ").strip().upper()

if __name__ == "__main__":
    main()