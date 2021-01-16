from model.sales import sales 
from view import terminal as view
from model import util


INDEX_COL_ID = 0
INDEX_COL_CUSTOMER = 1
INDEX_COL_PRODUCT = 2 
INDEX_COL_PRICE = 3
INDEX_COL_DATE = 4

def list_transactions(): #DZIAŁA
    """ Opening transactions list """

    view.print_message("\nLIST TRANSACTION\n")
    transactions_list = sales.read()
    view.print_table(transactions_list, sales.HEADERS)
    

def add_transaction(): #DZIAŁA
    """ Adding new element to list transactions """

    view.print_message("\nADDING NEW TRANSACTIONS\n")
    product = view.get_input("Please enter product name: ")
    price = view.get_input("Please enter price of product: ")
    date = view.get_input("Please provide date of transaction (in format 2021-01-11): ")
    sales.create(product, price, date)
    view.print_table(sales.read(), sales.HEADERS)
    
    
def update_transaction(): #NIE DZIAŁA
    """ Updating transaction list"""

    view.print_message("\nUPDATING TRANSACTION\n")
   
    
   
    
    
    
def delete_transaction(): #DZIAŁA
    """ Removing transaction from the list of transaction """

    view.print_message("\nREMOVING TRANSACTION\n")
    id = view.get_input("Please provide the ID, which you want to update: ")
    sales.delete(id)
    view.print_table(sales.read(), sales.HEADERS)
              

def get_biggest_revenue_transaction(): #DZIAŁA
    """ Determining which transaction is the largest and makes the biggest revenue """

    income = []
    transaction_list = sales.read()

    for element in transaction_list:
        income.append(float(element[3]))

    max_income_index = income.index(max(income))
    id_max_income_transaction = transaction_list[max_income_index][INDEX_COL_ID]
    view.print_message(f"\nTransaction that makes the biggest revenue is: {id_max_income_transaction}\n")
        

def get_biggest_revenue_product(): #DZIAŁA
    """ Determining which product makes the biggest revenue """

    income = []
    transaction_list = sales.read()

    for element in transaction_list:
        income.append(float(element[3]))

    max_income_index = income.index(max(income))
    id_max_income_transaction = transaction_list[max_income_index][INDEX_COL_PRODUCT]
    view.print_message(f"\nThe product that makes the biggest revenue is: {id_max_income_transaction}\n")
    

def count_transactions_between(): #DZIAŁA
    """ Counting number of transactions between two given dates """
    
    dates = []
    first_date = view.get_input("\nPlease provide first date (in format 2021-01-11): ")
    second_date = view.get_input("\nPlease provide second date (in format 2021-01-11): ")
    transactions = sales.read()
    
    for row in transactions:
        dates.append(row[-1])
    count = 0
    for date in dates:
        if date > first_date and date < second_date:
            count += 1
    view.print_message(f"\nThe number of transaction beetween {first_date} and {second_date} is {count}.\n")


def sum_transactions_between(): #DZIAŁA
    """ Summing the price of transactions between two given dates """

    dates = []
    transaction_price = []
    transactions_sum = []
    indexes = []
    transactions = sales.read()
    first_date = view.get_input("\nPlease provide first date (in format 2021-01-11): ")
    second_date = view.get_input("\nPlease provide second date (in format 2021-01-11): ")

    for row in transactions:
        dates.append(row[-1])
        transaction_price.append(row[-2])
    for date in dates:
        if date > first_date and date < second_date:
            indexes.append(dates.index(date))
    for index in indexes:
        transactions_sum.append(transaction_price[index])
    
    transactions_sum = [float(trans) for trans in transactions_sum]
    result = sum(transactions_sum)
    view.print_message(f"\nThe sum beetween {first_date} and {second_date} is {result}.\n")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
