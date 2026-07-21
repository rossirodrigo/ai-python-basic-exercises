import numpy as np

from ai_exercises.exercises.product_revenue import (
    build_products_dataframe,
    filter_by_revenue_and_rating,
)


def test_build_products_dataframe_shape():
    df = build_products_dataframe(n=10, rng=np.random.default_rng(0))

    assert len(df) == 10
    assert list(df.columns) == [
        "Categoria",
        "Preço",
        "Itens Vendidos",
        "Avaliação",
        "Receita",
    ]
    assert (df["Receita"] == df["Preço"] * df["Itens Vendidos"]).all()


def test_eletronicos_price_is_increased_by_50_percent():
    rng = np.random.default_rng(1)
    df = build_products_dataframe(n=20, rng=rng)

    eletronicos = df[df["Categoria"] == "Eletrônicos"]
    assert not eletronicos.empty


def test_filter_by_revenue_and_rating_sorts_descending_by_revenue():
    df = build_products_dataframe(n=200, rng=np.random.default_rng(2))

    filtered = filter_by_revenue_and_rating(df, min_revenue=100000, min_rating=4.0)

    assert (filtered["Receita"] > 100000).all()
    assert (filtered["Avaliação"] > 4.0).all()
    assert filtered["Receita"].is_monotonic_decreasing
