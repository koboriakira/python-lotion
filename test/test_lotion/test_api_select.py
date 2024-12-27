from unittest import TestCase

import pytest

from lotion import Lotion


@pytest.mark.api()
class TestApiSelect(TestCase):
    DATABASE_ID = "15a6567a3bbf80b4a76fc106b37fb92f"

    def setUp(self) -> None:
        self.suite = Lotion.get_instance()
