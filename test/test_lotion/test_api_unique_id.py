from unittest import TestCase

import pytest

from lotion import Lotion


@pytest.mark.api()
class TestApiUniqueId(TestCase):
    DATABASE_ID = "15d6567a3bbf80f9ac95e5153875b2c3"

    def setUp(self) -> None:
        self.suite = Lotion.get_instance()

    @pytest.mark.current()
    def test_ロールアップを取得する(self):
        # When
        page_id = "15d6567a3bbf8078bd6dfe1dc7688131"
        page = self.suite.retrieve_page(page_id=page_id)
        actual = page.get_unique_id(name="ID")

        # Then
        self.assertEqual(actual.number, 1)
        self.assertEqual(actual.prefix, None)

        # Then: 更新が可能なこともついでに確かめる
        self.suite.update_page(page_id=page_id, properties=page.properties.values)
