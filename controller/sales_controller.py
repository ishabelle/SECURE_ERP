from model import data_manager
from model import util
from model.sales import sales 
from view import terminal as view


INDEX_COL_ID = 0
INDEX_COL_CUSTOMER = 1
INDEX_COL_PRODUCT = 2 
INDEX_COL_PRICE = 3
INDEX_COL_DATE = 4

# READ from CRUD
def list_transactions(): #DZIAŁĄ
    """ Opening transactions list """

    print("\nLIST TRANSACTION\n")
    transactions = data_manager.read_table_from_file(sales.DATAFILE, separator=";")
    view.print_table(transactions, sales.HEADERS)
    

# CREATE from CRUD
def add_transaction(): #NIE DZIAŁA
    """ Adding new element to list transactions """
    
    transactions = data_manager.read_table_from_file(sales.DATAFILE, separator=";")
    transaction_id = util.generate_id()
    customer_id = util.generate_id()
    product = view.get_input("Please enter product name: ")
    price = view.get_input("Please enter price of product: ")
    date = view.get_input("Please provide date of transaction (in format 2021-01-11): ")
    tab = []
    new_transacion = tab.extend([transaction_id, customer_id, product, price, date])
    

    

    list_with_new_trans = data_manager.write_table_to_file(sales.DATAFILE, transactions, separator=";")
    view.print_table(list_with_new_trans, sales.HEADERS)
    
    
# UPDATE  from CRUD
def update_transaction(): #DZIAŁA
    """ Updating transaction list"""
    
    transactions = data_manager.read_table_from_file(sales.DATAFILE)
    user_choice = view.get_input("Please provide the ID's customer, which you want to update: ")
    for row in transactions:
        if user_choice == row[0]:
            customer_id = util.generate_id()
            product = view.get_input("Please enter product name: ")
            price = view.get_input("Please enter price of product: ")
            date = view.get_input("Please provide date of transaction (in format 2021-01-11): ")
            row[INDEX_COL_CUSTOMER] = customer_id
            row[INDEX_COL_PRODUCT] = product
            row[INDEX_COL_PRICE] = price
            row[INDEX_COL_DATE] = date
            data_manager.write_table_to_file(sales.DATAFILE, transactions)
    view.print_table(transactions, sales.HEADERS)


# DELETE from CRUD
def delete_transaction(): #DZIAŁA
    """ Removing transaction from the list of transaction """

    transactions = data_manager.read_table_from_file(sales.DATAFILE)
    user_choice = view.get_input("Please provide the ID's customer, which you want to delete: ")
    for row in transactions:
        if user_choice == row[0]:
            deleted_row = row
            print("\nChoosing transaction has been removed from list.\n")
            transactions.remove(deleted_row)
            data_manager.write_table_to_file(sales.DATAFILE, transactions)
    view.print_table(transactions, sales.HEADERS)
            

def get_biggest_revenue_transaction(): #DZIAŁA
    """ Determining which transaction is the largest and makes the biggest revenue """

    income = []
    transactions = data_manager.read_table_from_file(sales.DATAFILE)
    for row in transactions:
        income.append(row[INDEX_COL_PRICE])
    number_of_biggest_income = income.index(max(income))
    transaction = transactions[number_of_biggest_income]
    biggest_trans = " ".join(transaction)
    print(f"\nTransaction that makes the biggest revenue is: {biggest_trans}\n")
    return biggest_trans


def get_biggest_revenue_product():
    """ Determining which product makes the biggest revenue """

    biggest_trans = get_biggest_revenue_transaction()
    product = biggest_trans[INDEX_COL_PRODUCT]
    print(f"The product that makes the biggest revenue is: {product}")
    return product


def count_transactions_between():
    """ Counting number of transactions between two given dates """
    
    dates = []
    first_date = view.get_input("Please provide first date (in format 2021-01-11): ")
    second_date = view.get_input("Please provide second date (in format 2021-01-11): ")
    transactions = data_manager.read_table_from_file(sales.DATAFILE)
    for row in transactions:
        dates.append(row[-1])
    count = 0
    for date in dates:
        if date > first_date and date < second_date:
            count += 1
    print(f"The number of transaction beetween {first_date} and {second_date} is {count}.")


def sum_transactions_between():
    """ Summing the price of transactions between two given dates """

    dates = []
    trans_price = []
    trans_sum = []
    indexes = []
    transactions = data_manager.read_table_from_file(sales.DATAFILE)
    first_date = view.get_input("Please provide first date (in format 2021-01-11): ")
    second_date = view.get_input("Please provide second date (in format 2021-01-11): ")
    for row in transactions:
        dates.append(row[-1])
        trans_price.append(row[-2])
    for date in dates:
        if date > first_date and date < second_date:
            indexes.append(dates.index(date))
    for index in indexes:
        trans_sum.append(trans_price[index])
    trans_sum = [float(trans) for trans in trans_sum]
    result = sum(trans_sum)
    print(f"The sum beetween {first_date} and {second_date} is {result}.")


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
