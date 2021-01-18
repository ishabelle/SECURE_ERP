from model.crm import crm
from view import terminal as view


def list_customers():
    view.print_message("\n List of Customers:\n")
    customers_list = crm.read()
    view.print_table(customers_list, crm.HEADERS)

def add_customer():
    view.print_message("\n Add customer:\n")
    user_name = view.get_input("Type name: ")
    user_email = view.get_input("Type email ")
    user_subscribe_status = view.get_input("Is customer subscriber? 1: YES, 2: NO ")
    crm.create_customer(user_name, user_email, user_subscribe_status)
    
    view.print_table(crm.read(), crm.HEADERS)


def update_customer():
    view.print_message("\n Update customer:\n")
    user_id = view.get_input("Type customer id ")
    updated_name = view.get_input("Type name for update ")
    updated_email = view.get_input("Type email for update ")
    updated_subscribe_status = view.get_input("Is customer subscriber? 1: YES, 2: NO ")
    
    crm.update(user_id, updated_name, updated_email, updated_subscribe_status)
    view.print_table(crm.read(), crm.HEADERS)
    
def delete_customer():
    view.print_message("\n delete_customer:\n")
    user_id = view.get_input("User id: ")
    crm.delete(user_id)
    view.print_table(crm.read(), crm.HEADERS)

def get_subscribed_emails():
    view.print_message("\n List of subscribers emails:\n")
    subscribers_email_list = crm.check_subscribers()
    view.print_message((''.join(subscribers_email_list)))
    
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
