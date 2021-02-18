from model.crm import crm
from view import terminal as view


def list_customers():
    '''Function prints list of customers in table, from loaded file'''
    view.print_message("\n List of Customers:\n")
    customers_list = crm.read_customers_data()
    view.print_table(customers_list, crm.HEADERS)



def add_customer():
    '''Function adds customer to chosen file, function can handle: empty input and wrong data type in case of user_subscribe_status input'''
    view.print_message("\n Add customer:\n")
    user_name = view.get_input("Type name: ")
    crm.check_content_for_empty_value(user_name)
    user_email = view.get_input("Type email ")
    crm.check_content_for_empty_value(user_email)
    user_subscribe_status = view.get_input("Is customer subscriber? 1: YES, 2: NO ")
    crm.is_input_not_empty_and_is_integer(user_subscribe_status)
    crm.create_customer(user_name, user_email, user_subscribe_status)
    
    view.print_table(crm.read_customers_data(), crm.HEADERS)



def update_customer():
    '''Function updates customers name, email and subscription status, function can handle: wrong customer id, empty input amd wrong type in case of user_subscribe_status input'''
    view.print_message("\n Update customer:\n")
    user_id = view.get_input("Type customer id ")
    crm.check_customer_id(user_id)
    updated_name = view.get_input("Type name for update or press enter to skip this field ")
    crm.check_content_for_empty_value(updated_name)
    updated_email = view.get_input("Type email for update or press enter to skip this field  ")
    crm.check_content_for_empty_value(updated_email)
    updated_subscription_status = view.get_input("Type user subscription status or press enter to skip this field (1: Is a subsriber, 2: is't a subscriber) ")
    crm.is_input_not_empty_and_is_integer(updated_subscription_status)
    
    crm.update_customer(user_id, updated_name, updated_email, updated_subscription_status)
    view.print_table(crm.read_customers_data(), crm.HEADERS)
    
    
    
def delete_customer():
    '''Function removes customer, function can handle: wrond customer id'''
    view.print_message("\n delete_customer:\n")
    user_id = view.get_input("User id: ")
    crm.check_customer_id(user_id)
    crm.delete_customer(user_id)
    view.print_table(crm.read_customers_data(), crm.HEADERS)



def get_subscribers_emails():
    '''Function collects subscribers emails and displays them numbered'''
    view.print_message("\n List of subscribers emails:\n")
    emails_list = crm.check_emails_of_subscribing_customers()
    crm.print_list_in_table(emails_list)
    
    
def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        try:                               
            add_customer()
        except ValueError as empty_input:
            view.print_error_message(empty_input)
    elif option == 3:
        try:                               
            update_customer()
        except ValueError as wrong_id:            
            view.print_error_message(wrong_id) 
        update_customer()
    elif option == 4:
        try:                                
            delete_customer()
        except ValueError as wrong_id:
            view.print_error_message(wrong_id)
    elif option == 5:
        get_subscribers_emails()
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
