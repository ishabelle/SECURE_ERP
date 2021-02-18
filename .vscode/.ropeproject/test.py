import random
import string


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

                generated_id = ""
                elements_of_id = []


                for _ in range(number_of_small_letters):
                    elements_of_id.append(random.choice(string.ascii_lowercase))
                for _ in range(number_of_capital_letters):
                    elements_of_id.append(random.choice(string.ascii_uppercase))
                for _ in range(number_of_digits):
                    elements_of_id.append(random.choice(range(0, 10)))
                for _ in range(number_of_special_chars):
                    elements_of_id.append(random.choice(allowed_special_chars))

                random.shuffle(elements_of_id)

                for element in elements_of_id:
                    element = str(element)
                    generated_id += element

                return generated_id   
            
def add_new_customer():
    user_id = 1
    user_input_table = ["adam","@", "0"]
    user_input_table.insert(0, user_id)
    
    with open("model/crm/crm.csv", "w") as file:
        for record in user_input_table:
            row = separator.join(record)
            DATAFILE.write(row + "\n") 
add_new_customer()

def add_new_customer2(name, email, subscribed_status):
    table = read_file()
    user_id = generate_id()
    user_input_table = [name, email, subscribed_status]
    user_input_table.insert(0, user_id)
    table.append(user_input_table)
    write_table_to_file(DATAFILE, user_input_table)        

def start():
    user_name = "Adam"
    user_email = "dupek"
    user_subscribed_status = "0"
    add_new_customer2(user_name, user_email, user_subscribed_status)
    
    
def read_file():
    file_content = read_table_from_file(DATAFILE)
    return file_content     
    
def write_table_to_file(file_name, table, separator=';'):
    """Write tabular data into a CSV file.

    Args:
        file_name: The name of the file to write to.
        table: list of lists containing tabular data.
        separator: The CSV separator character
    """
    with open(file_name, "w") as file:
        for record in table:
            row = separator.join(record)
            file.write(row + "\n")    
            

def read_table_from_file(file_name, separator=';'):
    """Read CSV file into a data table.

    Args:
        file_name: The name of the CSV data file.
        separator: The CSV separator character

    Returns:
        The data parsed into a list of lists.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "").split(separator) for element in lines]
    except IOError:
        return []     
    
    
