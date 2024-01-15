from faker import Faker

fake = Faker()

def fake_user():
    return fake.email(), fake.password()