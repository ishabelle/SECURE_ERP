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


def read_file():
    file_content = data_manager.read_table_from_file(DATAFILE)
    return file_content


def create_customer(name, email, subscribed_status):
    table = read_file()
    user_id = util.generate_id()
    user_input_table = [name, email, subscribed_status]
    table.append(user_input_table)
    user_input_table.insert(0, user_id)
    
    data_manager.write_table_to_file(DATAFILE, user_input_table)
        
def update_customer(customer_id, name, email, subscribe_status):
    ''' - Once the CRM module is selected, choosing option 3 will ask the user for the id  of a customer.
    If the id belongs to an existent customer then the user will enter new values for the name, email and 
    subscribe status. Once the last field is entered,  the customer fields are updated with the given values.
    '''
    table = read_file()
    
    
    
    
    