import pandas as pd

from ai_exercises.exercises.reviews_challenge import (
    build_result_dataframe,
    parse_reviews,
)


def test_parse_reviews_splits_id_user_review():
    raw_lines = ["1$alice$Great game!", "2$bob$Too hard"]

    parsed = parse_reviews(raw_lines)

    assert parsed == [
        {"id": "1", "user": "alice", "review": "Great game!"},
        {"id": "2", "user": "bob", "review": "Too hard"},
    ]


def test_build_result_dataframe_sorts_by_rating():
    result = [
        {"id": "1", "user": "alice", "review": "a", "translation": "a", "rating": "Mixed"},
        {"id": "2", "user": "bob", "review": "b", "translation": "b", "rating": "Positive"},
        {"id": "3", "user": "carl", "review": "c", "translation": "c", "rating": "Negative"},
    ]

    df = build_result_dataframe(result)

    assert isinstance(df, pd.DataFrame)
    assert df.index.name == "id"
    assert list(df["rating"]) == ["Positive", "Negative", "Mixed"]
