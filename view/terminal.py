def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    
    print(title)
    count = -1
    for option in list_options:
        count += 1
        print(f'({count}) {option}', end='\n')


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """

    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """

    if type(result) == int:
        print(f"{label}: {result}")
    elif type(result) == float:
        result_formatted = "{:.2f}".format(result)
        print(f"{label}: {result_formatted}")
    elif type(result) == list or type(result) == tuple:
        print(f"{label}:")
        print("; ".join(f"{e}" for e in result))
    elif type(result) == dict:
        print(f"{label}:")
        print("; ".join(f"{k}: {v}" for k,v in result.items()))
    print("")


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table, HEADERS):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """

    headers = HEADERS

    whole_table = table
    whole_table.insert(0, headers)
    length_elements = [[len(x) for x in whole_table[i]] for i in range(len(whole_table))]

    cell_size = 10
    longest_elements = [0 for _ in range(len(headers))]
    for element in length_elements:
        for index, content in enumerate(element):
            if int(content) > longest_elements[index]:
                longest_elements[index] = int(content) + cell_size

    draw = [int(x) * '-' for x in longest_elements]

    print(f'/{"-".join(draw)}\\')
    for index, content in enumerate(whole_table):
        string = ""
        for i in range(len(content)):
            string += "|" + content[i].center(longest_elements[i])

        print(string + '|')
        if index == len(whole_table) - 1:
            print(f'\\{"-".join(draw)}/')
        else:
            print(f'|{"|".join(draw)}|')
    print("\n")


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """

    user_input = input(label)
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """

    list_with_new_inputs = []
    for i in labels:
        list_with_new_inputs.append(input(f"{i}: "))
        print()
    return list_with_new_inputs



def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """

    print(f"{message}")
