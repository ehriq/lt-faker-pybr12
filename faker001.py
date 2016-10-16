from faker import Faker
from collections import namedtuple
from json import dumps

all_data = []

Pessoa = namedtuple("Pessoa", ['nome', 'endereco', 'idade'])

fake = Faker('pt_BR')

for _ in range(1000000):
    p = Pessoa(nome=fake.name(),
               endereco=fake.street_address(),
               idade=fake.random_int(min=18, max=90))
    all_data.append(p._asdict())

f = open("teste.json", "w")
f.write(dumps(all_data))
f.close()
