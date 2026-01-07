#!/usr/bin/env python3
"""
create-notion-pages CLI コマンド

JSONファイルからNotionページを作成するCLIツール。
現在はRecipeタイプのみをサポート。
"""

import argparse
import json
import os
import sys
from pathlib import Path

from lotion import Lotion
from lotion.recipe import CreateRecipe


def create_recipe_page(lotion: Lotion, database_id: str, recipe_data: dict) -> dict:
    """レシピページを作成する

    Args:
        lotion: Lotionインスタンス
        database_id: レシピデータベースのID
        recipe_data: レシピのデータ

    Returns:
        作成されたページのIDとURLを含む辞書
    """
    recipe = CreateRecipe.from_dict(recipe_data)
    page = lotion.create_page_in_database(
        database_id=database_id,
        properties=recipe.build_properties(),
        blocks=recipe.build_blocks(),
    )
    return page.get_id_and_url()


def process_json_file(json_path: Path, database_id: str, lotion: Lotion) -> list[dict]:
    """JSONファイルを処理してページを作成する

    Args:
        json_path: JSONファイルのパス
        database_id: データベースID
        lotion: Lotionインスタンス

    Returns:
        作成されたページの情報リスト
    """
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    # 単一オブジェクトの場合はリストに変換
    if isinstance(data, dict):
        data = [data]

    results = []
    for item in data:
        item_type = item.get("type", "").lower()
        if item_type == "recipe":
            result = create_recipe_page(lotion, database_id, item)
            results.append({"title": item.get("title"), **result})
            print(f"Created recipe: {item.get('title')}")
        else:
            print(f"Skipping unsupported type: {item_type}", file=sys.stderr)

    return results


def main():
    """メインエントリポイント"""
    parser = argparse.ArgumentParser(
        prog="create-notion-pages",
        description="JSONファイルからNotionページを作成します",
    )
    parser.add_argument(
        "json_file",
        type=Path,
        help="ページデータが含まれるJSONファイルのパス",
    )
    parser.add_argument(
        "--database-id",
        "-d",
        type=str,
        default=os.getenv("RECIPE_DATABASE_ID"),
        help="レシピを保存するNotionデータベースのID（環境変数 RECIPE_DATABASE_ID でも指定可能）",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="実際にページを作成せずに内容を確認します",
    )

    args = parser.parse_args()

    # JSONファイルの存在確認
    if not args.json_file.exists():
        print(f"Error: JSON file not found: {args.json_file}", file=sys.stderr)
        sys.exit(1)

    # データベースIDの確認
    if not args.database_id:
        print(
            "Error: Database ID is required. Use --database-id or set RECIPE_DATABASE_ID environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    # dry-runモード
    if args.dry_run:
        with open(args.json_file, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            data = [data]
        print("Dry run mode - pages that would be created:")
        for item in data:
            item_type = item.get("type", "").lower()
            if item_type == "recipe":
                recipe = CreateRecipe.from_dict(item)
                print(f"\n  Recipe: {recipe.title}")
                print(f"    Reference URL: {recipe.reference_url or 'N/A'}")
                print(f"    Ingredients: {len(recipe.ingredients)} items")
                print(f"    Steps: {len(recipe.steps)} steps")
            else:
                print(f"\n  Skipping: {item.get('type')} (unsupported)")
        sys.exit(0)

    # Lotionインスタンスを取得
    lotion = Lotion.get_instance()

    # ページを作成
    try:
        results = process_json_file(args.json_file, args.database_id, lotion)
        print(f"\nSuccessfully created {len(results)} page(s)")
        for result in results:
            print(f"  - {result['title']}: {result['url']}")
    except Exception as e:
        print(f"Error creating pages: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
