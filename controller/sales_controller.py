from model.sales import sales 
from view import terminal as view


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
    
    
# UPDATE  from CRUD
def update_transaction(): #NIE DZIAŁA
    """ Updating transaction list"""

    view.print_message("\nUPDATING TRANSACTION LIST\n")
    view.print_table(sales.read(), sales.HEADERS)
    header = view.get_input("Enter number of transaction to update: ")
    value = view.get_inputs(sales.HEADERS[2:5])
    sales.update(id, header, value)
    view.get_input("Transaction updated. Press enter")
    
    

    
    # sales.update(id, header, value)
    # transactions = data_manager.read_table_from_file(sales.DATAFILE)
    # user_choice = view.get_input("Please provide the ID's customer, which you want to update: ")
    # for row in transactions:
    #     if user_choice == row[0]:
    #         customer_id = util.generate_id()
    #         product = view.get_input("Please enter product name: ")
    #         price = view.get_input("Please enter price of product: ")
    #         date = view.get_input("Please provide date of transaction (in format 2021-01-11): ")
    #         row[INDEX_COL_CUSTOMER] = customer_id
    #         row[INDEX_COL_PRODUCT] = product
    #         row[INDEX_COL_PRICE] = price
    #         row[INDEX_COL_DATE] = date
    #         data_manager.write_table_to_file(sales.DATAFILE, transactions)
    # view.print_table(transactions, sales.HEADERS)



def delete_transaction(): #DZIAŁA
    """ Removing transaction from the list of transaction """

    view.print_message("\nREMOVING TRANSACTION\n")
    id = view.get_input("Please provide the ID, which you want to update: ")
    sales.delete(id)
    view.print_table(sales.read(), sales.HEADERS)
  
            

def get_biggest_revenue_transaction(): #DZIAŁA
    """ Determining which transaction is the largest and makes the biggest revenue """

    income = []
    transactions = sales.read()
    for row in transactions:
        income.append(row[INDEX_COL_PRICE])
    number_of_biggest_income = income.index(max(income))
    transaction = transactions[number_of_biggest_income]
    biggest_trans = " ".join(transaction)
    view.print_message(f"\nTransaction that makes the biggest revenue is: {biggest_trans}\n")
    return biggest_trans


def get_biggest_revenue_product():
    """ Determining which product makes the biggest revenue """

    # biggest_trans = get_biggest_revenue_transaction()
    income = []
    transactions = sales.read()
    for row in transactions:
        income.append(row[INDEX_COL_PRICE])
    number_of_biggest_income = income.index(max(income))
    transaction = transactions[number_of_biggest_income]
    biggest_trans = " ".join(transaction)
    product = biggest_trans[INDEX_COL_PRODUCT]
    view.print_message(f"\nThe product that makes the biggest revenue is: {product}\n")
    return product


def count_transactions_between(): #DZIAŁA
    """ Counting number of transactions between two given dates """
    
    dates = []
    first_date = view.get_input("Please provide first date (in format 2021-01-11): ")
    second_date = view.get_input("Please provide second date (in format 2021-01-11): ")
    transactions = sales.read()
    for row in transactions:
        dates.append(row[-1])
    count = 0
    for date in dates:
        if date > first_date and date < second_date:
            count += 1
    view.print_message(f"\nThe number of transaction beetween {first_date} and {second_date} is {count}.\n")


def sum_transactions_between():
    """ Summing the price of transactions between two given dates """

    dates = []
    trans_price = []
    trans_sum = []
    indexes = []
    transactions = sales.read()
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
    view.print_message(f"The sum beetween {first_date} and {second_date} is {result}.")


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
