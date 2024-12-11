from datetime import date, datetime

from src.properties.date import Date
from src.datetime_utils import convert_to_date_or_datetime


class LastEditedTime(Date):
    NAME = "最終更新日時"

    @classmethod
    def create(cls, value: str | date | datetime) -> "LastEditedTime":
        if isinstance(value, str):
            value = convert_to_date_or_datetime(value)
        return LastEditedTime.from_start_date(name=cls.NAME, start_date=value)
