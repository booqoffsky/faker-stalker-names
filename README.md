# Description
_Faker-stalker-names_ is an provider for the [Faker](https://github.com/joke2k/faker) Python package. 

Generate stalker names for your tests and other tasks. Don't forget your friends)

# Localization
The following localizations are present: `ru_RU`, `en_US`, `uk_UA`.

# Installation
From PyPi:

`pip3 install faker-stalker-names`

# Usage
Just add the `Provider` to your `Faker` instance:

```
from faker import Faker
from faker_stalker_names.en_US import Provider as StalkerNamesProvider

fake = Faker()
fake.add_provider(StalkerNamesProvider)
```
Or pass to constructor:
```
from faker import Faker

fake = Faker(includes=["faker_stalker_names"], locale="ru_RU")
```
Now you can start to generate data:
```
fake.stalker_name()
# Яшка Нытик

fake.stalker_first_name()
# Саня

fake.stalker_last_name()
# Резкий
```

You can specify the desired type of name (`stalker` or `bandit` are available). 
By default, the first and last names are randomly selected.
```
fake.stalker_name(name_type="stalker")
# Slava Smartass

fake.stalker_first_name(name_type="bandit")
# Vasyan
```

In addition, a way to replace the standard `name` method at your own risk:
```
StalkerNamesProvider.name = StalkerNamesProvider.stalker_name
fake = Faker()
fake.add_provider(StalkerNamesProvider)
fake.name()
# Shurik Professor
```
