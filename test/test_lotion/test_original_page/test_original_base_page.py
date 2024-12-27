from typing import cast
from unittest import TestCase

import pytest
from lotion.lotion import Lotion
from test.test_lotion.test_original_page.original_page import OriginalBasePage


@pytest.mark.current()
class TestOriginalBasePage(TestCase):
    DATABASE_ID = "1686567a3bbf803c8c21e345cdd9d9d7"

    # def setUp(self) -> None:
    #     self.page = create_empty_page(database_id=self.DATABASE_ID)
    #     return super().setUp()

    # def tearDown(self) -> None:
    #     remove_page(page_id=self.page.id)
    #     return super().setUp()

    def test_オリジナルページを利用する(self):
        lotion = Lotion.get_instance()
        page_id = "1686567a3bbf809fae8fd87c0657f416"
        original_page = lotion.retrieve_page(page_id=page_id, cls=OriginalBasePage)
        original_text = original_page.original_text
        print(original_page)
        print(original_text)
        print(original_page.original_text.text)
        self.assertEqual(original_text.text, "This is a test.")
