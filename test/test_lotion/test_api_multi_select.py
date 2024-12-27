from unittest import TestCase

import pytest

from lotion import Lotion


@pytest.mark.api()
class TestApiMultiSelect(TestCase):
    DATABASE_ID = "15c6567a3bbf80818512f43db108616f"

    def setUp(self) -> None:
        self.suite = Lotion.get_instance()
