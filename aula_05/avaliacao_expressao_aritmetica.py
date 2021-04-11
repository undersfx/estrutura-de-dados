# Exercício de avaliação de expressão aritmética.
# Só podem ser usadas as estruturas Pilha e Fila implementadas em aulas anteriores.
# Deve ser análise de tempo e espaço para função avaliação
import unittest
from numbers import Number

from aula_05.fila import Fila


class ErroLexico(Exception):
    pass


class ErroSintatico(Exception):
    pass


def analise_lexica(expressao:str) -> Fila:
    """
    Executa análise lexica transformando a expressao em fila de objetos:
    e verificar se demais caracteres são validos: +-*/(){}[]
    :param expressao: string com expressao a ser analisada
    :return: fila com tokens
    """
    fila_lexica = Fila()
    temp = Fila()
    caracteres_validos = (".", "+", "-", "*", "/", "(", ")", "{", "}", "[", "]")

    for token in expressao:
        if not token.isnumeric() and token not in caracteres_validos:
            raise ErroLexico(f"{token} não é um caractere válido.")

        if token.isnumeric():
            temp.enfileirar(token)
            continue
        elif temp:
            fila_lexica.enfileirar(''.join(temp))
            temp = Fila()

        fila_lexica.enfileirar(token)

    else:
        if temp:
            fila_lexica.enfileirar(''.join(temp))

    return fila_lexica


def analise_sintatica(fila:Fila) -> Fila:
    """
    Função que realiza analise sintática de tokens produzidos por analise léxica.
    Executa validações sintáticas e se não houver erro retorn fila_sintatica para avaliacao
    Transforma inteiros em ints
    Flutuantes em floats

    :param fila: fila proveniente de análise lexica
    :return: fila_sintatica com elementos tokens de numeros
    """
    pass


def avaliar(expressao:str) -> Number:
    """
    Função que avalia expressão aritmetica retornando seu valor se não houver nenhum erro
    :param expressao: string com expressão aritmética
    :return: valor númerico com resultado
    """
    # Fazer análise léxica
    # Fazer análise sintática
    # Processar os tokens gerados
    pass