from time import sleep
from colorama import Fore, Style

def linha(tamanho):
    """
    Função para escrever uma linha acima e abaixo do relatório
    obtido pela função notas()
    """
    print('~' * tamanho)


def notas(exibir_situacao=True):
    """
    Função para calcular estatísticas das notas dos alunos.

    Argumento:
    exibir_situação (opcional) determina se a situação será calculada.

    Retorna um dicionário com as seguintes informações:
    - Quantidade de notas
    - Maior nota
    - Menor nota
    - A média da turma
    - Situação (opcional)

    Exemplo de uso: >>> notas(8, 7, 6, 9, 10, 5)
    {'Quantidade de notas': 6, 'Maior nota': 10, 'Menor nota': 5, 'Média': 7.5, 'Situação': 'Aprovado'}

    """

    # DECLARANDO AS VARIÁVEIS ------------------------------------------------------------------------------------------
    boletin = {}
    quantidade_de_notas = 0
    soma_notas = 0
    maior = float('-inf') # inicialize com um valor muito baixo
    menor = float('inf')  # inicialize com um valor muito alto


    aluno = str(input('Nome do aluno:'))

    while True:
        nota = float(input(f'Digite a(s) nota(s) do {aluno}:  '))
        print(Fore.YELLOW +'Adicionando nota...'+ Style.RESET_ALL)
        sleep(2)
        quantidade_de_notas += 1
        soma_notas += nota

        # VERIFICANDO A MAIOR E A MENOR NOTA ---------------------------------------------------------------------------
        if nota > maior:
            maior = nota

        if nota < menor:
            menor = nota

        # OPÇÃO DE ADICIONAR MAIS NOTAS --------------------------------------------------------------------------------
        continuar = str(input('Adicionar mais uma nota? [S/N]')).upper()[0]
        if continuar == 'N':
            print()
            print(Fore.LIGHTBLUE_EX + 'Gerando relatório', end='')
            carregando = '.....'
            for pontinho in carregando:
                print(f'{Fore.LIGHTBLUE_EX}{pontinho}'+ Style.RESET_ALL, end='', flush=True)
                sleep(0.5)
            print()
            print()
        break

    print(f'>>> Relatório do Aluno {aluno}')

    # ADICIONANDO OS DADOS OBTIDOS NO DICIONÁRIO BOLETIN ---------------------------------------------------------------
    boletin['Total de notas'] = quantidade_de_notas
    boletin['Maior nota'] = maior
    boletin['Menor nota'] = menor
    boletin['Média'] = soma_notas / quantidade_de_notas

    # CALCULANDO A SITUAÇÃO DO ALUNO -----------------------------------------------------------------------------------
    if exibir_situacao:
        if boletin['Média'] >= 7:
            situacao = 'Aprovado'
        elif 5 <= boletin['Média'] < 7:
            situacao = 'Recuperação'
        else:
            situacao = 'Reprovado'

        boletin['Situação'] = situacao
    return boletin

resultado = notas(exibir_situacao=True)

## Calculando o comprimento do resultado convertido para string
tamanho_linha = len(str(resultado)) + 4  ## Adicionando espaço extra para formatação


# IMPRIMINDO RESULTADO NA TELA -----------------------------------------------------------------------------------------
linha(tamanho_linha)

for chave, valor in resultado.items():
    if chave == 'Média': ## Se a chave for méda, será arredondado para 2 casas decimais
        valor = round(valor, 2)
    print(f'{chave}: {valor}')

linha(tamanho_linha)
