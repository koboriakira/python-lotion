from unittest import TestCase

import pytest
from lotion.properties.relation import Relation


@pytest.mark.current
class TestRelation(TestCase):
    def test_重複したページIDを整理する(self):
        # Given, When
        actual = Relation.from_id_list(["a", "b", "a", "c"])

        # Then
        self.assertEqual(3, len(actual.id_list))
        self.assertTrue("a" in actual.id_list)
        self.assertTrue("b" in actual.id_list)
        self.assertTrue("c" in actual.id_list)
