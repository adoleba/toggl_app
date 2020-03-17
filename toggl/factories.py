from dataclasses import dataclass, field
from datetime import date, time

import factory
from factory.fuzzy import FuzzyDate


@dataclass
class CorrectEntry:
    task: str = field(default=None)
    date_start: date = field(default=None)
    date_end: date = field(default=None)
    different_hours: str = field(default=None)
    hour_start: time = field(default=None)
    hour_end: time = field(default=None)
    toggl_login: str = field(default=None)
    toggl_password: str = field(default=None)
    toggl_id_number: int = field(default=None)
    monday_hour_start: time = field(default=None)
    monday_hour_end: time = field(default=None)
    tuesday_hour_start: time = field(default=None)
    tuesday_hour_end: time = field(default=None)
    wednesday_hour_start: time = field(default=None)
    wednesday_hour_end: time = field(default=None)
    thursday_hour_start: time = field(default=None)
    thursday_hour_end: time = field(default=None)
    friday_hour_start: time = field(default=None)
    friday_hour_end: time = field(default=None)


class CorrectEntryFactory(factory.Factory):
    class Meta:
        model = CorrectEntry

    task = 'task'
    date_end = date(2020, 2, 29)
    date_start = date(2020, 2, 1)
    different_hours = 'R'
    hour_start = time(10, 0)
    hour_end = time(18, 0)
    toggl_login = 'abc@example.com'
    toggl_password = factory.fuzzy.FuzzyText(length=10)
    toggl_id_number = factory.fuzzy.FuzzyInteger(100, 1000)


class InCorrectEntryFactory(factory.Factory):
    class Meta:
        model = CorrectEntry

    date_end = date(2020, 3, 1)
    date_start = factory.fuzzy.FuzzyDate(date(2020, 1, 1), date_end)
    different_hours = 'R'
    toggl_login = factory.fuzzy.FuzzyText(length=10)
    toggl_id_number = factory.fuzzy.FuzzyInteger(100, 1000)
