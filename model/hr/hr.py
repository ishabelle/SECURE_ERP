""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

# CRUD (Create, read, update and delete)

def read(with_headers=False):
    file_content = data_manager.read_table_from_file(DATAFILE)
    if with_headers:
        file_content = HEADERS + file_content
    return file_content

def create(name, date_of_birth, department, clearance):
    table = read()
    id = util.generate_id()
    data_to_add = [id, name, date_of_birth, department, clearance]
    table.append(data_to_add)
    data_manager.write_table_to_file(DATAFILE, table)

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
    newtable = []
    id_index = HEADERS.index("Id")

    for element in table:
        if element[id_index] != id:
            newtable.append(element)

    data_manager.write_table_to_file(DATAFILE, newtable)