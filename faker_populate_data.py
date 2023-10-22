'''
Readme area ************************************************************************************************************************************
Using Faker Library - [Link](https://faker.readthedocs.io/en/master/index.html)
Faker is a Python package that generates fake data for you.

Prerequisites [Important] :-
pip install Faker
[Link](https://pypi.org/project/Faker/)

How to run this script :-

1. If you have already installed the Faker library in your global Python environment or if you have a dedicated virtual environment, activate it.
2. Run this Faker script in the root folder where the `manage.py` is located.
3. Run the script by executing the following command: "python faker_populate_data.py"
4. When prompted, enter your data generation limit, the script will generate fake user profiles for you. It will create User and Profile models, similar to the signup process.

Readme area ************************************************************************************************************************************
'''


# Faker main code area - start -----------------------------------------------------------------------------------------------
# this will configure django apps, models, settings etc. and sync correctly
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_book.settings')
import django
django.setup()
# this will configure django apps, models, settings etc. and sync correctly

from django.contrib.auth import get_user_model
from core.models import Profile
User = get_user_model()

try:
    from faker import Faker
    faker = Faker()

    def populate(counter=5):
        for _ in range(counter):

            username = faker.name()
            username = "".join(username.lower().split())

            user = User.objects.create_user(
                username = username,
                email = f'{username}@gmail.com',
                password = '1111111'
            )
            Profile.objects.create(
                user=user,
                id_user=user.id,
                bio = faker.paragraph(nb_sentences=1),
                location = faker.address()
                )
            print(f'User "{username}" data is generated and saved into database')


    if __name__  == '__main__':
        while True:
            limit = input("Enter your data generation limit : ")

            if not limit.isdigit() or int(limit) <= 0:
                print("Please enter a valid limit.\n")
            else:
                print('Populating data.........\n')
                populate(int(limit))
                print(f'\nThe Faker library has successfully inserted {int(limit)} data entries into the database.[Models: User, Profile]')
                break
                
                
except ModuleNotFoundError:
    print('The "Faker" library is not installed. Please install it using "pip install Faker"')

# Faker main code area - end -----------------------------------------------------------------------------------------------

'''
Readme area ************************************************************************************************************************************
Using Faker Library - [Link](https://faker.readthedocs.io/en/master/index.html)
Faker is a Python package that generates fake data for you.

Prerequisites [Important] :-
pip install Faker
[Link](https://pypi.org/project/Faker/)

How to run this script :-

1. If you have already installed the Faker library in your global Python environment or if you have a dedicated virtual environment, activate it.
2. Run this Faker script in the root folder where the `manage.py` is located.
3. Run the script by executing the following command: "python faker_populate_data.py"
4. When prompted, enter your data generation limit, the script will generate fake user profiles for you. It will create User and Profile models, similar to the signup process.

Readme area ************************************************************************************************************************************
'''
