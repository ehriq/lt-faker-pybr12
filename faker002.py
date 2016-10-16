from faker import Faker
from collections import namedtuple
from json import dumps

all_data = []

fake = Faker('pt_BR')

for _ in range(10000):
    p = fake.simple_profile()
    all_data.append(p)

f = open("teste-simple-profile.json", "w")
f.write(dumps(all_data))
f.close()
