from unittest import TestCase

import pytest

from lotion import Lotion
from lotion.properties import Title
from lotion.page import PageId
from lotion.properties import Relation


@pytest.mark.api()
@pytest.mark.current()
class TestApiSelect(TestCase):
    DATABASE_ID = "15d6567a3bbf804e942dc49d808bf73a"

    def setUp(self) -> None:
        self.suite = Lotion.get_instance()

    @pytest.mark.minimum()
    def test_リレーションを変更する(self):
        page = self.suite.create_page_in_database(
            database_id=self.DATABASE_ID, properties=[Title.from_plain_text(text="テスト")]
        )

        # Given
        page_id = PageId("15d6567a3bbf804191c4e0dbd42644fe")
        relation_prop = Relation.from_id(name="リレーション", id=page_id.value)

        # When, Then
        properties = page.properties.append_property(relation_prop)
        self.suite.update_page(page_id=page.page_id.value, properties=properties.values)
        actual = self.suite.retrieve_page(page_id=page.page_id.value)
        actual_relation = actual.get_relation(name="リレーション")
        self.assertEqual(actual_relation.id_list, [page_id.value])
