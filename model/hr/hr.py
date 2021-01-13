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

def create():
    pass

def read():
    file_content = HEADERS + data_manager.read_table_from_file(DATAFILE)
    return file_content

def update(id, header, value):
    file_content = read()

    id_index = HEADERS.index("Id")
    header_index = HEADERS.index(header)

    for element in file_content:
        if element[id_index] == id:
            element[header_index] = value

    data_manager.write_table_to_file(DATAFILE, file_content)

def delete():