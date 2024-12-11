from unittest import TestCase

from block.bookmark import Bookmark
from block.bulleted_list_item import BulletedlistItem
from block.callout import Callout
from block.divider import Divider
from block.embed import Embed
from block.paragraph import Paragraph
from potion import Potion
from properties.text import Text

import pytest


class Test(TestCase):

    PAGE_ID = "1596567a3bbf8049803de1ffe3616d9e"

    def setUp(self):
        self.suite = Potion.get_instance()

    @pytest.mark.post_api()
    def test_パラグラフを追加する(self):
        text_block = Paragraph.from_plain_text(text="テスト")
        self._append_block_test(block=text_block)

    @pytest.mark.post_api()
    def test_ブックマークを追加する(self):
        bookmark = Bookmark.from_url(url="https://www.google.com/")
        self._append_block_test(block=bookmark)

    @pytest.mark.post_api()
    def test_リストを追加する(self):
        list_block = BulletedlistItem.from_plain_text(text="テスト")
        self._append_block_test(block=list_block)

    @pytest.mark.post_api()
    def test_区切り線を追加する(self):
        divider = Divider()
        self._append_block_test(block=divider)

    @pytest.mark.post_api()
    @pytest.mark.current()
    def test_埋め込みを追加する(self):
        embed = Embed.from_url(url="https://www.google.com/")
        self._append_block_test(block=embed)

    # @pytest.mark.post_api()
    # @pytest.mark.current()
    # def test_コールアウトを追加する(self):
    #     callout = Callout.from_plain_text(text="テスト")
    #     self._append_block_test(block=callout)

    # @pytest.mark.post_api()
    # @pytest.mark.current()
    # def test_コードを追加する(self):
    #     code = Code.from_plain_text(text="テスト")
    #     self._append_block_test(block=code)

    def _append_block_test(self, block):
        # When, Then
        actual = self.suite.append_block(block_id=self.PAGE_ID, block=block)
        self.assertTrue("results" in actual)
