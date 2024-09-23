from utilitarios import cadastrar_categoria, cadastrar_transacao, saldo_total

# categorias
categoria_receitas = cadastrar_categoria("Receitas")
categoria_contas = cadastrar_categoria("contas fixas")
categoria_viagens = cadastrar_categoria("Viagens")
categoria_lazer = cadastrar_categoria("LAZER")

# transacoes

cadastrar_transacao(
    descricao= "Salário Jan/2024",
    valor=2000,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao= "mesada",
    valor=500,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao= "ingresso show",
    valor=-200,
    categoria=categoria_lazer
)

cadastrar_transacao(
    descricao= "conta de luz",
    valor=-90,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao= "viagem",
    valor=-900,
    categoria=categoria_viagens
)

total = saldo_total()

print("Saldo total: ", total) 