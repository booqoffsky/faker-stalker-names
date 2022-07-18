from enum import Enum
from typing import Any, List, Dict

from faker.providers import BaseProvider

localized = True


class StalkerNameType(str, Enum):
    STALKER = "stalker"
    BANDIT = "bandit"


class Provider(BaseProvider):
    first_names: Dict[str, List[str]] = {}
    last_names: Dict[str, List[str]] = {}

    all_first_names: List[str] = []
    all_last_names: List[str] = []

    def __init__(self, generator: Any):
        super().__init__(generator)
        for name_type in self.first_names.values():
            self.all_first_names.extend(name_type)
        for name_type in self.last_names.values():
            self.all_last_names.extend(name_type)

    def stalker_first_name(self, name_type: str = None) -> str:
        if not name_type:
            return self.random_element(self.all_first_names)
        return self.random_element(self.first_names[name_type])

    def stalker_last_name(self, name_type: str = None) -> str:
        if not name_type:
            return self.random_element(self.all_last_names)
        return self.random_element(self.last_names[name_type])

    def stalker_name(self, name_type: str = None) -> str:
        first_name = self.stalker_first_name(name_type)
        last_name = self.stalker_last_name(name_type)
        return f"{first_name} {last_name}"
