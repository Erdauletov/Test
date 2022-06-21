class Notebook:
    """This is a notebook"""

    _counter = 0

    def __init__(self, first_name, last_name, phone_number, address='unknown', birth_date='unknown'):
        self.serial_number = Notebook._counter
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address if address.strip() != '' else 'unknown'
        self.birth_date = birth_date if birth_date.strip() != '' else 'unknown'
        Notebook._counter += 1
