import random
from datetime import datetime, timedelta, timezone

from src.database import SessionLocal
from src.models import Post

# 俳句のサンプルデータ
HAIKU_SAMPLES = [
    {
        "first": "古池や",
        "second": "蛙飛び込む",
        "third": "水の音",
        "season": "夏",
        "kigo": "蛙",
        "author": "松尾芭蕉",
    },
    {
        "first": "閑かさや",
        "second": "岩にしみ入る",
        "third": "蝉の声",
        "season": "夏",
        "kigo": "蝉",
        "author": "松尾芭蕉",
    },
    {
        "first": "柿食えば",
        "second": "鐘が鳴るなり",
        "third": "法隆寺",
        "season": "秋",
        "kigo": "柿",
        "author": "正岡子規",
    },
    {
        "first": "菜の花や",
        "second": "月は東に",
        "third": "日は西に",
        "season": "春",
        "kigo": "菜の花",
        "author": "与謝蕪村",
    },
    {
        "first": "春の海",
        "second": "終日のたり",
        "third": "のたりかな",
        "season": "春",
        "kigo": "春の海",
        "author": "与謝蕪村",
    },
]

# 季節と代表的な季語のマッピング
SEASON_KIGO = {
    "春": ["桜", "春風", "若葉", "蝶", "霞", "花見", "梅", "春雨"],
    "夏": ["蛍", "夕立", "入道雲", "朝顔", "風鈴", "蝉", "夏草"],
    "秋": ["月", "紅葉", "秋風", "コスモス", "稲穂", "虫の音", "秋雨"],
    "冬": ["雪", "霜", "北風", "木枯らし", "冬鳥", "寒月", "氷柱"],
}

# 一般的な俳句のフレーズ
PHRASES = {
    "春": {
        "first": ["春風や", "花の下", "春の日に", "桜咲く", "春の雨"],
        "second": ["そよそよと吹く", "心弾む", "散りゆくは", "風そよぐ"],
        "third": ["春の空", "山の端", "川の流れ", "野の道を"],
    },
    "夏": {
        "first": ["夏の日や", "青空に", "夕立や", "暑き日に"],
        "second": ["照りつける日", "風涼し", "雲流る", "波さわぐ"],
        "third": ["入道雲", "夏の海", "夕暮れに", "山の端"],
    },
    "秋": {
        "first": ["秋の夜", "月明かり", "秋風や", "木枯らしや"],
        "second": ["虫の音や", "紅葉散る", "雁渡る", "露光る"],
        "third": ["里の秋", "野山かな", "夕暮れに", "秋の空"],
    },
    "冬": {
        "first": ["冬の日や", "寒風や", "雪降りて", "霜の朝"],
        "second": ["木枯らしの", "氷結ぶ", "寒月や", "霜柱"],
        "third": ["冬の空", "冬の海", "山眠る", "夜の底"],
    },
}


def generate_random_haiku(base_date: datetime) -> dict:
    """ランダムな俳句データを生成する"""
    # ランダムに季節を選択
    season = random.choice(list(SEASON_KIGO.keys()))

    if random.random() < 0.3:  # 30%の確率で既存の俳句を使用
        haiku = random.choice(HAIKU_SAMPLES)
        first = haiku["first"]
        second = haiku["second"]
        third = haiku["third"]
        kigo = haiku["kigo"]
        note = f"{haiku['author']}の句"
    else:  # 70%の確率でランダム生成
        first = random.choice(PHRASES[season]["first"])
        second = random.choice(PHRASES[season]["second"])
        third = random.choice(PHRASES[season]["third"])
        kigo = random.choice(SEASON_KIGO[season])
        note = "自動生成された句"

    # ランダムな投稿日時を生成（基準日から前後30日以内）
    random_days = random.randint(-30, 30)
    posted_at = base_date + timedelta(days=random_days)

    return {
        "first_phrase": first,
        "second_phrase": second,
        "third_phrase": third,
        "full_text": f"{first} {second} {third}",
        "note": note,
        "season": season,
        "kigo": kigo,
        "posted_at": posted_at,
    }


def seed_posts() -> None:
    db = SessionLocal()
    try:
        # 基準となる日付を設定
        base_date = datetime(2024, 1, 1, tzinfo=timezone.utc)

        # 100件の俳句データを生成
        posts = []
        for _ in range(100):
            haiku_data = generate_random_haiku(base_date)
            posts.append(Post(**haiku_data))

        db.add_all(posts)
        db.commit()
        print(f"{len(posts)}件の俳句データを追加しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_posts()
