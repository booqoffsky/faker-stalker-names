from faker_stalker_names import Provider as StalkerNameProvider
from faker_stalker_names.de_DE.data import first_names, last_names


class Provider(StalkerNameProvider):
    first_names = first_names
    last_names = last_names
