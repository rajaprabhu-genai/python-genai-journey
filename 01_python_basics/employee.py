def calculate_annual_salary(monthly_salary : float) -> float:
    return monthly_salary * 12

def display_employee_details(name : str, emp_id : str, department : str, monthly_salary : float):
    annual_salary = calculate_annual_salary(monthly_salary)
    employee_category = "Senior Employee" if annual_salary > 50000 else "Junior Employee"
    print("-" * 50)
    print("{:^50}".format("Employee Details"))
    print("-" * 50)
    print(f"ID             : {emp_id}")
    print(f"Name           : {name}")
    print(f"Department     : {department}")
    print(f"Monthly Salary : ${monthly_salary:.2f}")
    print(f"Annual Salary  : ${annual_salary:.2f}")
    print(f"Category       : {employee_category}")
    print("-" * 50)

def get_employee_details():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    department = input("Enter employee department: ")
    monthly_salary = float(input("Enter employee monthly salary: "))
    return name, emp_id, department, monthly_salary

print("Employee Management System")

employee_name, employee_id, employee_department, employee_monthly_salary = get_employee_details()
display_employee_details(employee_name, employee_id, employee_department, employee_monthly_salary)