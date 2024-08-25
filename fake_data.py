from faker import Faker
import random
import re

def generate_fake_data(custom_username=None, custom_firstname=None, custom_lastname=None):
    fake = Faker()

    # Generate custom or random login (username)
    if custom_username:
        login = custom_username
    else:
        long_login = ''.join(e for e in (fake.user_name() * 10) if e.isalnum())
        while not long_login[0].isalpha():
            long_login = ''.join(e for e in (fake.user_name() * 10) if e.isalnum())
        login_length = random.randint(13, 25)
        login = long_login[:login_length]

    # Generate random password
    password = fake.password(length=random.randint(13, 25), special_chars=False)
    while len(re.findall(r"\d", password)) < 2:
        password = fake.password(length=random.randint(13, 25), special_chars=False)

    # Use custom or random first name
    first_name = custom_firstname if custom_firstname else fake.first_name()

    # Use custom or random last name
    last_name = custom_lastname if custom_lastname else fake.last_name()

    # Generate a random birth date for someone aged 18 to 30
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=30)

    return login, password, first_name, last_name, birth_date

# Example usage:
if __name__ == "__main__":
    custom_user = "my_custom_username"
    custom_first = "John"
    custom_last = "Doe"

    fake_account = generate_fake_data(custom_username=custom_user, custom_firstname=custom_first, custom_lastname=custom_last)

    print("Generated Outlook Account Data:")
    for key, value in fake_account.items():
        print(f"{key}: {value}")
