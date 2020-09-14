from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((item.value, item.name) for item in cls)

    @classmethod
    def values(cls):
        return [item.value for item in cls]

    def __str__(self):
        return self.name

    def __int__(self):
        return self.value
