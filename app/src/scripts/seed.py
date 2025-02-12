import argparse

from src.scripts.seeds.development.test_seeds import seed_tests
from src.scripts.seeds.master.post_seeds import seed_posts
from src.scripts.seeds.master.test_master_seeds import seed_test_masters


def run_development_seeds() -> None:
    """開発環境用のテストデータを投入"""
    seed_tests()


def run_master_seeds() -> None:
    """マスターデータを投入"""
    seed_test_masters()
    seed_posts()


def main() -> None:
    parser = argparse.ArgumentParser(description="データベースシードスクリプト")
    parser.add_argument(
        "--type",
        choices=["all", "development", "master"],
        default="all",
        help="投入するシードデータの種類",
    )

    args = parser.parse_args()

    if args.type in ["all", "master"]:
        run_master_seeds()

    if args.type in ["all", "development"]:
        run_development_seeds()


if __name__ == "__main__":
    main()
