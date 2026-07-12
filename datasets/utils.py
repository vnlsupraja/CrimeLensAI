import random

from faker import Faker

fake = Faker("en_IN")


def random_phone():
    return fake.phone_number()


def random_name():
    return fake.name()


def random_address():
    return fake.address().replace("\n", ", ")


def choose(lst):
    return random.choice(lst)


def uid(prefix, number):
    return f"{prefix}{number:05d}"


def percentage():
    return round(random.uniform(0, 100), 2)