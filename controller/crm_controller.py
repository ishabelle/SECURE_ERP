from model.crm import crm
from view import terminal as view
# def list_employees():
#     employees_table = hr.read()
#     view.print_table(employees_table

def list_customers():
    view.print_message("\nCustomers list:\n")
    customers_table = crm.read_file()
    view.print_table(customers_table, crm.HEADERS)

def add_customer():
    view.print_message("\nAdd new customer:\n")
    customer_name = view.get_input("What's your email? ")
    customer_email = view.get_input("What's your email? ")
    customer_subscribed_status = view.get_input("Are you subscriber? (1: YES | 2: NO) ")
    crm.create_customer(customer_name, customer_email, customer_subscribed_status)
    view.print_table(crm.read_file(), crm.HEADERS)
    



def update_customer():
    customer_id = view.get_input("What's your Id? ")
    customer_new_name = view.get_input("What's your name? ")
    customer_new_email = view.get_input("What's your Id? ")
    customer_new_subscribe_status = view.get_input("Are you subscriber? (1: YES | 2: NO) ")

    crm.update_customer(customer_id, customer_new_name, customer_new_email, customer_new_subscribe_status)
    
    
def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
