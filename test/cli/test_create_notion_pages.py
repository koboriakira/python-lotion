import json
import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


class TestCLI:
    def test_dry_run_mode(self, capsys):
        """dry-runモードでページ情報が表示されることを確認"""
        # Given
        recipe_data = [
            {
                "type": "Recipe",
                "title": "テストレシピ",
                "reference_url": "https://example.com",
                "ingredients": [
                    {"name": "材料A", "quantity": "100g"},
                ],
                "steps": ["手順1"],
            }
        ]

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(recipe_data, f, ensure_ascii=False)
            temp_path = f.name

        try:
            # When
            with patch.object(
                sys,
                "argv",
                [
                    "create-notion-pages",
                    temp_path,
                    "--database-id",
                    "test-db-id",
                    "--dry-run",
                ],
            ):
                from lotion.cli.create_notion_pages import main

                with pytest.raises(SystemExit) as exc_info:
                    main()

            # Then
            assert exc_info.value.code == 0
            captured = capsys.readouterr()
            assert "Dry run mode" in captured.out
            assert "テストレシピ" in captured.out
            assert "1 items" in captured.out
            assert "1 steps" in captured.out

        finally:
            Path(temp_path).unlink()

    def test_error_when_json_file_not_found(self, capsys):
        """存在しないJSONファイルを指定した場合にエラーになることを確認"""
        # When
        with patch.object(
            sys,
            "argv",
            [
                "create-notion-pages",
                "/nonexistent/path/to/file.json",
                "--database-id",
                "test-db-id",
            ],
        ):
            from lotion.cli.create_notion_pages import main

            with pytest.raises(SystemExit) as exc_info:
                main()

        # Then
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "Error: JSON file not found" in captured.err

    def test_error_when_database_id_not_provided(self, capsys, monkeypatch):
        """database-idが指定されていない場合にエラーになることを確認"""
        # Given
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump([], f)
            temp_path = f.name

        # 環境変数をクリア
        monkeypatch.delenv("RECIPE_DATABASE_ID", raising=False)

        try:
            # When
            with patch.object(
                sys,
                "argv",
                ["create-notion-pages", temp_path],
            ):
                from lotion.cli.create_notion_pages import main

                with pytest.raises(SystemExit) as exc_info:
                    main()

            # Then
            assert exc_info.value.code == 1
            captured = capsys.readouterr()
            assert "Database ID is required" in captured.err

        finally:
            Path(temp_path).unlink()

    def test_skip_unsupported_type_in_dry_run(self, capsys):
        """サポートされていないタイプはスキップされることを確認"""
        # Given
        data = [
            {"type": "UnsupportedType", "title": "無効なタイプ"},
        ]

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(data, f, ensure_ascii=False)
            temp_path = f.name

        try:
            # When
            with patch.object(
                sys,
                "argv",
                [
                    "create-notion-pages",
                    temp_path,
                    "--database-id",
                    "test-db-id",
                    "--dry-run",
                ],
            ):
                from lotion.cli.create_notion_pages import main

                with pytest.raises(SystemExit) as exc_info:
                    main()

            # Then
            assert exc_info.value.code == 0
            captured = capsys.readouterr()
            assert "Skipping: UnsupportedType" in captured.out

        finally:
            Path(temp_path).unlink()

    def test_single_object_json(self, capsys):
        """単一オブジェクトのJSONも処理できることを確認"""
        # Given
        recipe_data = {
            "type": "Recipe",
            "title": "単一レシピ",
            "ingredients": [],
            "steps": [],
        }

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(recipe_data, f, ensure_ascii=False)
            temp_path = f.name

        try:
            # When
            with patch.object(
                sys,
                "argv",
                [
                    "create-notion-pages",
                    temp_path,
                    "--database-id",
                    "test-db-id",
                    "--dry-run",
                ],
            ):
                from lotion.cli.create_notion_pages import main

                with pytest.raises(SystemExit) as exc_info:
                    main()

            # Then
            assert exc_info.value.code == 0
            captured = capsys.readouterr()
            assert "単一レシピ" in captured.out

        finally:
            Path(temp_path).unlink()
