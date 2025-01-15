from unittest import TestCase

import pytest
from lotion import Lotion
from lotion.base_page import BasePage
from lotion.block.rich_text.rich_text_element import RichTextElement


class TestReadBlock(TestCase):
    def test_link_mentionのリッチテキストを扱える(self):
        # Given
        input = {
            "type": "mention",
            "mention": {
                "type": "link_mention",
                "link_mention": {
                    "href": "https://miro.com/app/board/uXjVMxYuGhI=/?moveToWidget=3458764560855121283&cot=14",
                    "title": "A private Miro board",
                    "padding": 75,
                    "icon_url": "https://miro.com/favicon.ico",
                    "iframe_url": "https://miro.com/app/live-embed/uXjVMxYuGhI=/?moveToWidget=3458764560855121283&cot=14&embedId=927451861288&embedSource=oembed&embedMode=view_only_without_ui",
                    "link_provider": "Miro",
                    "thumbnail_url": "https://miro.com/app/images/application/icons/board_vis_230905/board-ava.png"
                },
            },
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": "https://miro.com/app/board/uXjVMxYuGhI=/?moveToWidget=3458764560855121283&cot=14",
            "href": "https://miro.com/app/board/uXjVMxYuGhI=/?moveToWidget=3458764560855121283&cot=14"
        }

        # When
        rich_text = RichTextElement.from_entity(input)

        # Then
        self.assertEqual(rich_text.href, "https://miro.com/app/board/uXjVMxYuGhI=/?moveToWidget=3458764560855121283&cot=14")
        self.assertEqual(rich_text.to_plain_text(), "A private Miro board")
