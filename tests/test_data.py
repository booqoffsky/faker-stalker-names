from typing import Dict, List

import pytest

from faker_stalker_names import de_DE as de
from faker_stalker_names import en_US as en
from faker_stalker_names import es_ES as es
from faker_stalker_names import fr_FR as fr
from faker_stalker_names import it_IT as it
from faker_stalker_names import pl_PL as pl
from faker_stalker_names import ru_RU as ru
from faker_stalker_names import uk_UA as uk


@pytest.mark.parametrize(
    "names",
    [
        de.first_names,
        de.last_names,
        en.first_names,
        en.last_names,
        es.first_names,
        es.last_names,
        fr.first_names,
        fr.last_names,
        it.first_names,
        it.last_names,
        pl.first_names,
        pl.last_names,
        ru.first_names,
        ru.last_names,
        uk.first_names,
        uk.last_names,
    ],
)
@pytest.mark.parametrize(
    "name_type",
    [
        "stalker",
        "bandit",
    ],
)
def test_names_are_unique(name_type: str, names: Dict[str, List[str]]):
    assert len(names[name_type]) == len(set(names[name_type]))
