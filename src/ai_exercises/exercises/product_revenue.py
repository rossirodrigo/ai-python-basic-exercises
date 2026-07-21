import numpy as np
import pandas as pd


def build_products_dataframe(n=50, rng=None):
    rng = rng or np.random.default_rng()

    nomes_produtos = [f"Produto {i + 1}" for i in range(n)]
    categorias_produtos = rng.choice(
        ["Eletrônicos", "Livros", "Roupas", "Alimentos", "Brinquedos"], n
    )
    precos_produtos = rng.uniform(10.0, 500.0, n).round(2)
    itens_vendidos = rng.integers(1, 1000, n)
    avaliacoes_produtos = rng.uniform(1.0, 5.0, n).round(1)

    df_produtos = pd.DataFrame(
        {
            "Nome": nomes_produtos,
            "Categoria": categorias_produtos,
            "Preço": precos_produtos,
            "Itens Vendidos": itens_vendidos,
            "Avaliação": avaliacoes_produtos,
        }
    ).set_index("Nome")

    # Filter eletronics and add 50% to the price
    df_produtos.loc[df_produtos["Categoria"] == "Eletrônicos", "Preço"] *= 1.5

    # Add revenue column
    df_produtos["Receita"] = df_produtos["Preço"] * df_produtos["Itens Vendidos"]

    return df_produtos


def filter_by_revenue_and_rating(df_produtos, min_revenue=100000, min_rating=4.0):
    return df_produtos[
        (df_produtos["Receita"] > min_revenue) & (df_produtos["Avaliação"] > min_rating)
    ].sort_values(by="Receita", ascending=False)


def main():
    df_produtos = build_products_dataframe()
    revenue_filtered = filter_by_revenue_and_rating(df_produtos)

    print("Produtos com receita acima de 100.000 e avaliação acima de 4.0:")
    print(revenue_filtered)
    print("\n")

    print("Primeiros 3 produtos com receita acima de 100.000 e avaliação acima de 4.0:")
    print(revenue_filtered.head(3))
    print("\n")

    print("Últimos 3 produtos com receita acima de 100.000 e avaliação acima de 4.0:")
    print(revenue_filtered.tail(3))


if __name__ == "__main__":
    main()
