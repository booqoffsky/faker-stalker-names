import uuid

import pytest
from faker import Faker

from faker_stalker_names import Provider as BaseProvider


class Provider(BaseProvider):
    first_names = {
        "bandit": [uuid.uuid4().hex for _ in range(4)],
        "stalker": [uuid.uuid4().hex for _ in range(8)],
    }
    last_names = {
        "bandit": [uuid.uuid4().hex for _ in range(8)],
        "stalker": [uuid.uuid4().hex for _ in range(16)],
    }


@pytest.mark.parametrize("name_type", ["stalker", "bandit"])
def test_first_name_call_with_name_type(name_type: str) -> None:
    fake = Faker()
    fake.add_provider(Provider)
    assert fake.stalker_first_name(name_type=name_type) in (
        Provider.first_names[name_type]
    )


@pytest.mark.parametrize("name_type", ["stalker", "bandit"])
def test_last_name_call_with_name_type(name_type: str) -> None:
    fake = Faker()
    fake.add_provider(Provider)
    assert fake.stalker_last_name(name_type=name_type) in (
        Provider.last_names[name_type]
    )


@pytest.mark.parametrize("name_type", ["stalker", "bandit"])
def test_name_call_with_name_type(name_type: str) -> None:
    fake = Faker()
    fake.add_provider(Provider)
    firstname, lastname = fake.stalker_name(name_type=name_type).split(" ")
    assert firstname in Provider.first_names[name_type]
    assert lastname in Provider.last_names[name_type]


def test_name_call() -> None:
    fake = Faker()
    fake.add_provider(Provider)
    firstname, lastname = fake.stalker_name().split(" ")
    assert firstname in (
            Provider.first_names["stalker"] + Provider.first_names["bandit"]
    )
    assert lastname in (
            Provider.last_names["stalker"] + Provider.last_names["bandit"]
    )


def test_first_name_call() -> None:
    fake = Faker()
    fake.add_provider(Provider)
    firstname = fake.stalker_first_name()
    assert firstname in (
            Provider.first_names["stalker"] + Provider.first_names["bandit"]
    )


def test_last_name_call() -> None:
    fake = Faker()
    fake.add_provider(Provider)
    lastname = fake.stalker_last_name()
    assert lastname in (
            Provider.last_names["stalker"] + Provider.last_names["bandit"]
    )
