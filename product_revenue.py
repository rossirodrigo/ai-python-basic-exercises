import pandas as pd
import numpy as np

nomes_produtos = [f"Produto {i+1}" for i in range(50)]
categorias_produtos = np.random.choice(
    ["Eletrônicos", "Livros", "Roupas", "Alimentos", "Brinquedos"], 50
)
precos_produtos = np.random.uniform(10.0, 500.0, 50).round(2)
itens_vendidos = np.random.randint(1, 1000, 50)
avaliacoes_produtos = np.random.uniform(1.0, 5.0, 50).round(1)

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

# Filter by revenue and rating, sort by revenue
revenue_filtered = df_produtos[
    (df_produtos["Receita"] > 100000) & (df_produtos["Avaliação"] > 4.0)
].sort_values(by="Receita", ascending=False)

print("Produtos com receita acima de 100.000 e avaliação acima de 4.0:")
print(revenue_filtered)
print("\n")

print("Primeiros 3 produtos com receita acima de 100.000 e avaliação acima de 4.0:")
print(revenue_filtered.head(3))
print("\n")

print("Últimos 3 produtos com receita acima de 100.000 e avaliação acima de 4.0:")
print(revenue_filtered.tail(3))
