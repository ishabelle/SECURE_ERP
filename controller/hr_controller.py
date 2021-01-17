from model.hr import hr
from view import terminal as view

# def list_employees():
#     employees_table = hr.read()
#     view.print_table(employees_table)
def list_employees():
    employees_table = hr.read()
    view.print_table(employees_table, hr.HEADERS)


def add_employee():
    view.print_message("You are adding a new employee. Please provide necessary information:")
    employee_headers = hr.HEADERS[1:]
    data = dict()
    for header in employee_headers:
        data[header] = view.get_input(f'{header}: ')
    hr.create(data)
    view.print_message("Employee added.")


def update_employee():
    employees_table = hr.read()
    
    view.print_message("Which employee's info you'd like to update?")
    for count, employee in enumerate(employees_table):
        view.print_general_results(employee, count)
    emp_number = int(view.get_input("Please provide employee number:"))
    
    view.print_message("What would you like to update?")
    employee = employees_table[emp_number]
    for count, label in enumerate(employee):
        view.print_general_results(label, hr.HEADERS[count])




def delete_employee():
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
