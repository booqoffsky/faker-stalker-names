import pytest
from faker_stalker_names import ru_RU as ru
from faker_stalker_names import en_US as en


@pytest.mark.parametrize(
    "names",
    [
        ru.first_names,
        ru.last_names,
        en.first_names,
        en.last_names,
    ],
)
@pytest.mark.parametrize(
    "name_type",
    [
        "stalker",
        "bandit",
    ],
)
def test_names_are_unique(name_type: str, names: dict[str, list[str]]):
    assert len(names[name_type]) == len(set(names[name_type]))
