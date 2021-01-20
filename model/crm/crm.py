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



def read():
    '''Function read content of file and return it as a list'''
    file_content = data_manager.read_table_from_file(DATAFILE)
    return file_content



def create_customer(name, email, subscribe_status): #nazwa do ujednolicenia
    '''Function gets name, email and subscribe_status as inputs from user, adds to them id, which is generated in model/util, 
    and write them into csv file as new customer'''
    file_content = read()
    user_id = util.generate_id()
    user_inputs_table = [name, email, subscribe_status]
    user_inputs_table.insert(ID_INDEX, user_id)
    file_content.append(user_inputs_table)
    data_manager.write_table_to_file(DATAFILE, file_content)



def update(id, updated_name, updated_email, updated_subscribe_status):
    '''Function gets id, updated_name, updated_email, updated_subscribe_status as an input and 
    if input id is same as id from loaded file we get acces to assigned user to id and we can update his data'''
    customer_table = read()
    
    for line in customer_table:
        if id in line[ID_INDEX]:
            # old_id = line[ID_INDEX]
            old_name =  line[NAME_INDEX]
            old_email = line[EMAIL_INDEX]
            old_subsribe_status = line[SUBSCRIBE_STATUS_INDEX]
            
            # line[ID_INDEX] = id or old_id
            line[NAME_INDEX] = updated_name or old_name
            line[EMAIL_INDEX] = updated_email or old_email
            line[SUBSCRIBE_STATUS_INDEX] = updated_subscribe_status or old_subsribe_status
        # else:
        #     pass
    data_manager.write_table_to_file(DATAFILE, customer_table)
    
    
    
def check_id(id):
    '''Function checks if user Id is correct if not exit program'''
    read_file = read()
    table_for_id = []
    
    for line in read_file:
        table_for_id.append(line[ID_INDEX])
        
    if id not in table_for_id:
        raise ValueError("The id is a lie!")
    
    

def delete(id):
    '''Function delete customer from file if input id is same as user id from loaded file (maby base in future)'''
    customer_table = read()
    
    for line in customer_table:
        if id in line[ID_INDEX]:
            # could be DEL, read about it :D
            line.clear()
            filtered_list = [x for x in customer_table if x != []]
            
    data_manager.write_table_to_file(DATAFILE, filtered_list)



def get_subscribers():
    '''Function returs list of subscribers from loaded file'''
    customer_table = read()
    subscribers_list = []
    consecutive_number_for_mail = 0
    for customer in customer_table:
        if customer[SUBSCRIBE_STATUS_INDEX] == "1":
            consecutive_number_for_mail += 1
            # subscribers_list.append(f"{consecutive_number_for_mail}. {customer[2]}\n")
            subscribers_list.append(customer)

    return subscribers_list