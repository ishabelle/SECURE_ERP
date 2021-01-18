""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def read():
    file_content = data_manager.read_table_from_file(DATAFILE)
    return file_content

def create_customer(name, email, subscribe_status):
    file_content = read()
    user_id = util.generate_id()
    user_inputs_table = [name, email, subscribe_status]
    user_inputs_table.insert(user_id)
    file_content.append(user_inputs_table)
    data_manager.write_table_to_file(file_content)

def update(id, updated_name, updated_email, updated_subscribe_status):
    customer_table = read()
    
    for i in customer_table:
        if id in i[0]:
            i[0] = id 
            i[1] = updated_name
            i[2] = updated_email
            i[3] = updated_subscribe_status
    data_manager.write_table_to_file(DATAFILE, customer_table)
    
#  - Once the CRM module is selected, choosing option 4 will ask the user for the id  of a customer.
#  If the id belongs to an existent customer then that it will be deleted from the database.
def delete(id):
    customer_table = read()
    
    for line in customer_table:
        if id in line[0]:
            line.clear()
            filtered_list = [x for x in customer_table if x != []]
            
    data_manager.write_table_to_file(DATAFILE, filtered_list)
    