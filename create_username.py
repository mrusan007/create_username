from os import read
import unicodedata
import csv

def create_username(f_name, l_name):
        
    # getting rid of slavec letters and turn it to lower case
    first_name = str(unicodedata.normalize('NFKD', f_name).encode('ascii', 'ignore').decode('ascii')).lower()
    last_name = str(unicodedata.normalize('NFKD', l_name).encode('ascii', 'ignore').decode('ascii')).lower()
        
    name_sum = first_name + '.' + last_name

    return name_sum

    
def write_csv():
    '''
    Write username in given csv.
    '''

    with open('users.csv', newline='') as csv_dict:
        field_names = ['first_name', 'last_name', 'phone','email']
        reader = csv.DictReader(csv_dict, fieldnames=field_names)
        

        for user in reader:
            new_username = create_username(user['first_name'], user['last_name'])

            with open('users_edit.csv', 'a', newline='') as csv_file:
                field_names_bigger = ['first_name', 'last_name', 'phone','email', 'username']
                writer = csv.DictWriter(csv_file, fieldnames=field_names_bigger)
                writer.writerow({'first_name': user['first_name'], 'last_name': user['last_name'], 
                    'phone': user['phone'], 'email': user['email'], 'username': new_username})