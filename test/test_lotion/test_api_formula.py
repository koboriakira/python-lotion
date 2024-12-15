from unittest import TestCase

import pytest

from lotion import Lotion
from lotion.properties import Title


@pytest.mark.api()
@pytest.mark.current()
class TestApiFormula(TestCase):
    DATABASE_ID = "15d6567a3bbf80fe8855d0383a7eb7dd"

    def setUp(self) -> None:
        self.suite = Lotion.get_instance()

    def test_数式の入ったページを取得する(self):
        # Then
        actual = self.suite.retrieve_page(page_id="15d6567a3bbf803d9c3eeebb80b24d89")
