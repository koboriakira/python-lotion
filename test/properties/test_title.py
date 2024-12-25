from unittest import TestCase
from lotion.properties.title import Title


class TestTitle(TestCase):
    def test_シンプルなテキスト(self) -> None:
        input = "dummy"
        actual = Title.from_plain_text(text=input)

        # Then
        self.assertEqual(actual.text, input)
