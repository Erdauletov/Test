from notebook import Notebook


def new_notebook():
    """Creates a new notebook"""

    while not (first_name := input('INPUT| Enter your name: ')).isalpha():
        print(' WARN| Enter correct values!')
    while not (last_name := input('INPUT| Enter your surname: ')).isalpha():
        print(' WARN| Enter correct values!')
    while not (phone_number := input('INPUT| Enter your phone number: ')).isnumeric():
        print(' WARN| Enter correct values!')

    address = input('INPUT| Enter your address (optional): ')
    birth_date = input('INPUT| Enter your birth date (optional): ')

    return Notebook(first_name, last_name, phone_number, address, birth_date)


def print_info(_notebook):
    print('----------------------------------------------------')
    print(f' Name:\t{_notebook.first_name}')
    print(f' Surname:\t{_notebook.last_name}')
    print(f' Phone number:\t{_notebook.phone_number}')
    print(f' Address:\t{_notebook.address}')
    print(f' Birth date:\t{_notebook.birth_date}')
    print('-----------------------------------------------------')
