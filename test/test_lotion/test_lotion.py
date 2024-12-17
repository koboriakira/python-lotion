from unittest import TestCase

import pytest
from lotion import Lotion
from lotion.base_page import BasePage


@pytest.mark.api()
class TestLotion(TestCase):
    def setUp(self):
        self.suite = Lotion.get_instance()

    def test_ページを取得する(self):
        # pipenv run pytest test/test_lotion/test_lotion.py -k test_ページを取得する
        page_id = "15a6567a3bbf814b9b06e0fd3c6959e0"
        page = self.suite.retrieve_page(page_id=page_id)
        self.assertIsInstance(page, BasePage)
