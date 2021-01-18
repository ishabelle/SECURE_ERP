""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

INDEX_COL_ID = 0
INDEX_COL_CUSTOMER = 1
INDEX_COL_PRODUCT = 2 
INDEX_COL_PRICE = 3
INDEX_COL_DATE = 4

def create(product, price, date):
    """ Developing new data's """

    table = read()
    id = util.generate_id()
    customer = util.generate_id()
    data_to_add = [id, customer, product, price, date]
    table.append(data_to_add)
    data_manager.write_table_to_file(DATAFILE, table)


def read(with_headers = False):
    """ Opening file with data's """

    file_content = data_manager.read_table_from_file(DATAFILE)
    if with_headers:
        file_content = HEADERS + file_content
    return file_content


def update(id, product, price, date): 
    """ Changing existing data's """

    transactions = read()

    for transaction in transactions:
        if id == transaction[INDEX_COL_ID]:
            trans_to_update = transaction

    if product:
        trans_to_update[INDEX_COL_PRODUCT] = product
    if price:
        trans_to_update[INDEX_COL_PRICE] = price
    if date:
        trans_to_update[INDEX_COL_DATE] = date

    data_manager.write_table_to_file(DATAFILE, transactions)

    
def delete(id):
    """ Removing existing data's """
    
    table = read()
    new_table = []
    id_index = HEADERS.index("Id")

    for element in table:
        if element[id_index] != id:
            new_table.append(element)

    data_manager.write_table_to_file(DATAFILE, new_table)


