from datetime import date, datetime

from src.properties.date import Date
from src.datetime_utils import convert_to_date_or_datetime


class CreatedTime(Date):
    NAME = "作成日時"

    @classmethod
    def create(cls: "CreatedTime", value: str | date | datetime) -> "CreatedTime":
        if isinstance(value, str):
            value = convert_to_date_or_datetime(value)
        return CreatedTime.from_start_date(name=cls.NAME, start_date=value)
