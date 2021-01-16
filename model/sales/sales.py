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

# Create Read Update Delete

def create(product, price, date):
    table = read()
    id = util.generate_id()
    customer = util.generate_id()
    data_to_add = [id, customer, product, price, date]
    table.append(data_to_add)
    data_manager.write_table_to_file(DATAFILE, table)


def read(with_headers = False):
    file_content = data_manager.read_table_from_file(DATAFILE)
    if with_headers:
        file_content = HEADERS + file_content
    return file_content


def update(id, header, value):
    file_content = read()

    id_index = HEADERS.index("Id")
    header_index = HEADERS.index(header)

    for element in file_content:
        if element[id_index] == id:
            element[header_index] = value

    data_manager.write_table_to_file(DATAFILE, file_content)


def delete(id):
    table = read()
    new_table = []
    id_index = HEADERS.index("Id")

    for element in table:
        if element[id_index] != id:
            new_table.append(element)

    data_manager.write_table_to_file(DATAFILE, new_table)


