from faker import Faker

faker = Faker()

#Позитивная генерация
def generate_registarion():
    random_email = faker.email()
    random_password = faker.password(length=6, special_chars=True, upper_case=True, lower_case=True, digits=True)
    return random_email, random_password

#Генерация емаил без домена
def generate_registration_validation_email():
    random_email_no_domain = faker.email(domain=False)
    password_2 = faker.password(length=6, special_chars=True, upper_case=True, lower_case=True, digits=True)
    return random_email_no_domain, password_2

#Генерация пароля в 5 символов
def generate_registration_validation_password():
    email_3 = faker.email()
    password_invalid_length = faker.password(length=4, special_chars=True, upper_case=True, lower_case=True, digits=True )
    return email_3, password_invalid_length











