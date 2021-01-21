from model.hr import hr
from view import terminal as view


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

# REFACTORING BLOCK

    for count, employee in enumerate(employees_table):
        employee_data = {}
        for value in range(len(employee)):
            employee_data.update({hr.HEADERS[value]: employee[value]})

        view.print_general_results(employee_data, count)

    emp_number = int(view.get_input("Please provide employee number:")) #validate input or TRY EXCEPT
    
# /REFACTORING BLOCK

    view.print_message("What would you like to update?")
    employee = employees_table[emp_number]

    for count, label in enumerate(employee):
        view.print_general_results({hr.HEADERS[count]: label}, count)

    record = int(view.get_input("Please type a number: "))



    current_label = employee[hr.HEADERS.index("Name")]
    view.print_message(f"You're updating {current_label}'s {hr.HEADERS[record]}")
    new_value = view.get_input("Please provide new value: ")
    hr.update(employee[hr.HEADERS.index("Id")], hr.HEADERS[record], new_value)
    view.print_message("Record updated. Please check your new table: ")
    list_employees()



def delete_employee():
    employees_table = hr.read()
    
    view.print_message("Which employee you'd like to delete?")

# REFACTORING BLOCK

    for count, employee in enumerate(employees_table):
        employee_data = {}
        for value in range(len(employee)):
            employee_data.update({hr.HEADERS[value]: employee[value]})

        view.print_general_results(employee_data, count)

    emp_number = int(view.get_input("Please provide employee number:"))

# /REFACTORING BLOCK

    chosen_emp_id = employees_table[emp_number][hr.HEADERS.index("Id")]

    hr.delete(chosen_emp_id)


def get_oldest_and_youngest():
    employees_table = hr.read()

    DoB_position = hr.HEADERS.index("Date of birth")
    Name_position = hr.HEADERS.index("Name")

    youngest_date = "-5000-01-01"
    oldest_date = "5000-01-01"

    for employee in employees_table:
        if employee[DoB_position] >= youngest_date:
            youngest_date = employee[Name_position]

    for employee in employees_table:
        if employee[DoB_position] <= oldest_date:
            oldest_date = employee[Name_position]

    view.print_general_results((youngest_date, oldest_date), "The youngest and oldest employees are")

def get_average_age():

    employees_table = hr.read()

    DoB_position = hr.HEADERS.index("Date of birth")

    currentdate = view.get_input("Please enter current date in yyyy-mm-dd format: ")

    current_year = currentdate[:4]

    bth_years = []

    for employee in employees_table:
        emp_age  = int(current_year) - int(employee[DoB_position][:4])
        bth_years.append(emp_age)

    avg_age = sum(bth_years) / len(bth_years) #should count months (at least)

    view.print_general_results({"The average age of employees is": avg_age}, "")


def is_leap_year(year):
    return (year %4 == 0 and not year %100 == 0) or year %400 == 0

def date_in_two_weeks(current_date):
    
    MONTHS_W_31_DAYS = ('01', '03', '05', '07', '08', '10', '12')

    current_year = current_date[0:4]
    current_month = current_date[5:7]
    current_day = current_date[8:10]

    if current_month == '02':
        days_in_month = 29 if is_leap_year(current_year) else 28
    else:
        days_in_month = 31 if current_month in MONTHS_W_31_DAYS else 30

    day_in_14 = int(current_day) + 14
    month_in_14 = int(current_month)
    year_in_14 = int(current_year)

    if day_in_14 > days_in_month:
        month_in_14 += 1
        day_in_14 = day_in_14 % days_in_month

    if month_in_14 > 12:
        year_in_14 += 1
        month_in_14 = month_in_14 % 12

    # this makes one digit month a two digit string
    month_in_14 = format(month_in_14, '02d')
    day_in_14 = format(day_in_14, '02d')

    return f'{year_in_14}-{month_in_14}-{day_in_14}'


def next_birthdays():

    current_date = view.get_input("Please enter current date in yyyy-mm-dd format: ")
    date_in_14 = date_in_two_weeks(current_date)

    employees_table = hr.read()
    DoB_position = hr.HEADERS.index("Date of birth")
    Name_position = hr.HEADERS.index("Name")

    current_month_and_day = current_date[5:10]
    month_and_day_in_14 = date_in_14[5:10]

    employees_with_bday_in_14 = dict()

    for employee in employees_table:
        emp_month_and_day = employee[DoB_position][5:10]

    #breaks on DEC/JAN

        if current_month_and_day <= emp_month_and_day <= month_and_day_in_14:
            employees_with_bday_in_14[employee[Name_position]] = emp_month_and_day
    
    view.print_general_results([date_in_14], "The date in two weeks will be")
    view.print_general_results(employees_with_bday_in_14, "Following employees will have their birthday in two weeks")


def count_employees_with_clearance():
    '''HR module/(8) Return the number of employees with at least the given clearance level.'''

    clearance_index = hr.HEADERS.index("Clearance")

    employees_table = hr.read()
    clearence_table = []

    for employee in employees_table:
        clearence_table.append(employee[clearance_index])

    desired_cleareance = view.get_input("Please type Clearence treshold: ")

    counter = int()

    for clearance in clearence_table:
        if desired_cleareance <= clearance:
            counter += 1

    view.print_general_results((counter), "You have this many employees with desired clearance")


def count_employees_per_department():
    '''HR module/(9) Return the number of employees per department in a dictionary (like {'dep1': 5, 'dep2': 11}).'''

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
