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
ID_INDEX = 0                     # index for column with customer id
NAME_INDEX = 1                   # index for column with customer name
EMAIL_INDEX = 2                  # index for column with customer email
SUBSCRIBE_STATUS_INDEX = 3       # index for column with customer subscribe status



def read_customers_data():
    '''Function read content of file and return it as a list'''
    file_content = data_manager.read_table_from_file(DATAFILE)
    return file_content



def create_customer(name, email, subscribe_status):
    '''Function gets name, email and subscribe_status as inputs from user, adds to them id, which is generated in model/util, 
    and write them into csv file as new customer'''
    file_content = read_customers_data()
    user_id = util.generate_id()
    user_inputs_table = [name, email, subscribe_status]
    
    user_inputs_table.insert(ID_INDEX, user_id)
    file_content.append(user_inputs_table)
    data_manager.write_table_to_file(DATAFILE, file_content)



def update_customer(id, updated_name, updated_email, updated_subscribe_status):
    '''Function gets id, updated_name, updated_email, updated_subscribe_status as an input and 
    if input id is same as id from loaded file we get acces to assigned user to id and we can update his data'''
    customer_table = read_customers_data()
    
    for line in customer_table:
        if id in line[ID_INDEX]:
            old_name =  line[NAME_INDEX]
            old_email = line[EMAIL_INDEX]
            old_subsribe_status = line[SUBSCRIBE_STATUS_INDEX]
            
            line[NAME_INDEX] = updated_name or old_name
            line[EMAIL_INDEX] = updated_email or old_email
            line[SUBSCRIBE_STATUS_INDEX] = updated_subscribe_status or old_subsribe_status

    data_manager.write_table_to_file(DATAFILE, customer_table)
    

def delete_customer(id):
    '''Function delete customer from file if input id is same as user id from loaded file'''
    customer_table = read_customers_data()
    
    for line in customer_table:
        if id in line[ID_INDEX]:
            line.clear()
            customer_table.remove(line)
            filtered_list = [x for x in customer_table if x != []]

    data_manager.write_table_to_file(DATAFILE, filtered_list)

def check_content_for_empty_value(input_content):
    '''Function checks if passed data is empty, if is  - prints the sentence'''
    if input_content == "":
        raise ValueError("Field can't be empty, type required content ")
    
    
def is_input_not_empty_and_is_integer(input_content):
    '''Function checks if passed data is empty or is not integer value, if is - prints the sentence'''
    if input_content == "" or type(input_content) != int:
        raise ValueError("Field can't be empty and must be number, type required content ")
    
    
    
def check_emails_of_subscribing_customers():
    '''Function returs list of subscribers from loaded file'''
    customer_table = read_customers_data()
    subscribers_list = []
    for word in customer_table:
        if word[SUBSCRIBE_STATUS_INDEX] == "1":
            subscribers_list.append(word[EMAIL_INDEX])
    return subscribers_list



def check_customer_id(id):
    '''Function checks if user Id is correct'''
    read_file = read_customers_data()
    table_for_id = []
    
    for line in read_file:
        table_for_id.append(line[ID_INDEX])
        
    if id not in table_for_id:
        raise ValueError("Wrong user id! Type required.")
    
    
    
def print_list_in_table(table):
    '''Function prints content passed as a table '''
    print(" SUBSCRIBERS EMAILS:\n")
    consecutive_number = 0
    for i in table:
        consecutive_number += 1
        print(f"{consecutive_number}. {i}")