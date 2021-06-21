import unicodedata

class Username:
    '''
    Class for creating username.
    '''

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def create_username(self):
        
        # getting rid of slavec letters and turn it to lower case
        first_name = str(unicodedata.normalize('NFKD', self.first_name).encode('ascii', 'ignore').decode('ascii')).lower()
        last_name = str(unicodedata.normalize('NFKD', self.last_name).encode('ascii', 'ignore').decode('ascii')).lower()
        
        name_sum = first_name + '.' + last_name

        return name_sum