from unittest import TestCase

import pytest

from datetime_utils import jst_now
from potion import Potion
from properties.title import Title


class TestFetchProperty(TestCase):
    DATABASE_ID = "1596567a3bbf80fc9aacdc21f9f5c516"

    def setUp(self) -> None:
        self.suite = Potion.get_instance()
        created_page = self.suite.create_page_in_database(
            database_id=self.DATABASE_ID, properties=[Title.from_plain_text(text="テスト")]
        )
        self.page = self.suite.retrieve_page(page_id=created_page["id"])
        self.now = jst_now().replace(second=0, microsecond=0)
        return super().setUp()

    def tearDown(self) -> None:
        self.suite.remove_page(self.page.page_id.value)
        return super().setUp()

    @pytest.mark.post_api()
    @pytest.mark.current()
    def test_作成日時と更新日時を取得する(self):
        self.assertEqual(self.page.created_at, self.now)
        self.assertEqual(self.page.updated_at, self.now)
