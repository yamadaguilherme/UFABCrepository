'''
 Uma empresa de cosmeticos pretende estimular a venda de algumas linhas de seus produtos em determinadas regioes.
Escreva um programa para processar os dados coletados para cada pedido de vendas. O usuario ira informar inicialmente
o codigo da linha do produto. Considere que a digitacao sera encerrada quando for digitado o codigo da linha do produto
igual a 0 (zero) indicando que nao ha mais pedidos com dados a serem processados.
Apos ler o codigo da linha do produto o programa devera solicitar o valor do pedido e em seguida o codigo da regiao.
• Para linha do produto o usuario ira digitar um codigo, sendo 1 para Basica e 3 para Top. Nao e necessario fazer
a validacao de dados da linha do produto.
• Para regiao o usuario ira digitar um codigo, sendo 4 para Centro-Norte e 6 para Centro-Sul. Nao e necessario
fazer a validacao de dados da regiao do produto.
As seguintes situacoes poderao ou nao ocorrer dependendo das regras: (a) vendedor recebera bonus na comissao e/ou
(b) cliente recebera desconto no pedido. O bonus e/ou desconto deve ser calculado sobre o valor do pedido.
As regras sao as seguintes:
Linha   Valor Pedido      Regioes      Bonus Vendedor     Desconto Cliente
Basica  ≥ 300 reais     Centro-Sul          -                   8%
Top         -           Centro-Norte        3%                  12%
Top         -           Centro-Sul          6%                   9%
Caso as entradas do usuario nao se enquadrem nas condicoes da tabela acima, deve-se assumir Bonus Vendedor = 0
e/ou Desconto Cliente = 0. Note que o Bonus Vendedor somente sera exibido se a linha for Top.
O programa deve imprimir para cada PEDIDO: (a) A linha do produto; (b) o valor do pedido; (c) a regiao do produto
(quando for o caso), o valor do desconto obtido (desconto = 0 se nao obteve desconto), o valor do bonus da comissao (quando
for o caso). Vide os casos de teste (exemplos).
Ao final, apos encerrar a entrada de dados o programa deve imprimir (uma unica vez) - Vide os casos de teste
(exemplos):
(a) Quantidade total de pedidos;
(b) Valor medio dos pedidos entre 100 reais (inclusive) e 300 reais (inclusive), independentemente de regiao;
(c) Soma dos bonus das comissoes (dos pedidos) da regiao Centro-Norte;
(d) Quantidade de pedidos que nao obtiveram descontos.

'''
def entrada():
    mystr = ""
    acumuladorlinha, contadorvalor, contabonus, acumuladordesc, somavalor = 0, 0, 0, 0, 0
    linha = 1
    while linha != 0:
        linha = int(input())
        if linha == 0:
            continue
        acumuladorlinha += 1
        valor = int(input())
        if 100< valor <300:
            somavalor += valor
            contadorvalor += 1
        regiao = int(input())
        if linha == 3:
            if regiao == 6:
                bonus = 6
                descont = 9
            else:
                bonus = 3
                descont = 12
                contabonus += (valor*(bonus/100))
            mystr += f"Linha: {linha} Pedido: {valor:.1f} Regiao: {regiao} Desconto: {((valor)*(descont/100)):.1f} Bonus: {(valor*(bonus/100)):.1f}\n"
        else:
            if regiao == 6 and valor>=300:
                descont = 8
            else:
                descont = 0
                acumuladordesc += 1
            mystr += f"Linha: {linha} Pedido: {valor:.1f} Regiao: {regiao} Desconto: {((valor)*(descont/100)):.1f}\n"
        if contadorvalor == 0:
            pedidomedio = 0.0
        else:
            pedidomedio = somavalor/contadorvalor
            
    mystr += f"Quantidade de pedidos: {acumuladorlinha}\n"
    mystr += f"Valor medio de pedidos entre 100 e 300 reais: {pedidomedio:.1f}\n"
    mystr += f"Soma dos bonus de pedidos da regiao 4: {contabonus:.1f} \n"
    mystr += f"Quantidade de pedidos sem descontos: {acumuladordesc}\n"
    print(mystr)

entrada()
        
        
        