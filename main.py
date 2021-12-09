import pandas as pd

import openpyxl

if __name__ == '__main__':
#Trazer a base de dados para o Python e ver o que tem nela
    tabela = pd.read_excel('Vendas.xlsx')
    print(tabela)
#Fazer um panorama
    fatoramento_total = tabela['Valor Final'].sum()
    print(fatoramento_total)
#Fazer uma análise top -> down
    #fatoramento por loja
    faturamento_por_loja = tabela[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
    print(faturamento_por_loja)
#Entre no detalhe
    faturamento_por_produto = tabela[['ID Loja', 'Produto', 'Valor Final']].groupby(['ID Loja', 'Produto']).sum()
    print(faturamento_por_produto)





