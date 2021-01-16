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

# - Once the CRM module is selected, choosing option 1 will ask the user to type the name, email and subscribed status for a new customer.
        # After the last field is introduced a new customer is introduced with an random id.
def create_customer(name, email, subscribed_status):
    table = read_file()
    user_id = util.generate_id()
    user_input_table = [name, email, subscribed_status]
    table.append(user_input_table)
    user_input_table.insert(0, user_id)
    
    data_manager.write_table_to_file(DATAFILE, user_input_table)
        
def 
    
    
    
    
    