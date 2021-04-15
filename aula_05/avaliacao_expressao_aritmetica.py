# Exercício de avaliação de expressão aritmética.
# Só podem ser usadas as estruturas Pilha e Fila implementadas em aulas anteriores.
# Deve ser análise de tempo e espaço para função avaliação

from numbers import Number

from aula_05.fila import Fila
from aula_04.pilha_com_lista_duplamente_ligada import Pilha, PilhaVaziaExcecao


class FilaHelper(Fila):
    def to_number(self):
        num = ''.join(self._deque)
        self._deque.clear()
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        return num

    def sanitizar(self) -> Fila:
        fila_sanitizada = Fila()
        for token in self._deque:
            if token in ('[', '{'):
                fila_sanitizada.enfileirar('(')
            elif token in (']', '}'):
                fila_sanitizada.enfileirar(')')
            else:
                fila_sanitizada.enfileirar(token)
        return fila_sanitizada


Fila = FilaHelper


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

    Time Complexity = O(n)
    Space Complexity = O(n)
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

    Time Complexity = O(n)
    Space Complexity = O(n)
    """
    if not fila:
        raise ErroSintatico()

    fila_sintatica = Fila()
    temp = Fila()
    caracteres_validos = ("+", "-", "*", "/", "(", ")", "{", "}", "[", "]")

    for token in fila:
        if token.isnumeric() or token == ".":
            temp.enfileirar(token)
            continue

        if token in caracteres_validos:
            if temp: fila_sintatica.enfileirar(temp.to_number())

            fila_sintatica.enfileirar(token)
            continue

        raise ErroSintatico()
    else:
        if temp: fila_sintatica.enfileirar(temp.to_number())

    return fila_sintatica


def _avaliar_operacao(n: Number, operation: str, m: Number) -> Number:
    """
    Avalia uma operação matemática e retorno o resultado.

    >>> _avaliar_operacao(1, "+", 2)
    3

    Time Complexity = O(1)
    Space Complexity = O(1)
    """
    case = {
        '+': lambda n, m: n + m,
        '-': lambda n, m: n - m,
        '*': lambda n, m: n * m,
        '/': lambda n, m: n / m,
    }
    try:
        return case[operation](n, m)
    except TypeError as e:  
        raise ValueError('Operação não suportada') from e


def _resolver_expressao_flat(expressao: Pilha) -> Number:
    """
    Avalia uma Pilha normalizada de operações sequenciais sem considerar precedência.

    >>> pilha = Pilha()
    >>> pilha._deque.extend([2, '*', 2, '/', 1, '+', 1])
    >>> _resolver_expressao_flat(pilha)  # 1 + 1 / 2 * 2
    2

    Time Complexity = O(n)
    Space Complexity = O(1)
    """
    n = expressao.desempilhar()
    try:
        operacao = expressao.desempilhar()
        m = expressao.desempilhar()
    except PilhaVaziaExcecao:
        return n

    resultado = _avaliar_operacao(n, operacao, m)

    while not expressao.esta_vazia:
        operacao = expressao.desempilhar()
        m = expressao.desempilhar()
        resultado = _avaliar_operacao(resultado, operacao, m)

    return resultado


def avaliar(expressao:str) -> Number:
    """
    Função que avalia expressão aritmetica retornando seu valor se não houver nenhum erro
    :param expressao: string com expressão aritmética
    :return: valor númerico com resultado

    Time Complexity = O(n**2)
    Space Complexity = O(n)
    """
    # Fazer análise léxica
    # Fazer análise sintática
    # Processar os tokens gerados

    expressao = analise_lexica(expressao)
    expressao = analise_sintatica(expressao)
    expressao = expressao.sanitizar()
    
    pilha_de_execucao = Pilha()
    temp = Pilha()

    for token in expressao:
        if token != ')':
            pilha_de_execucao.empilhar(token)
        else:
            token = pilha_de_execucao.desempilhar()

            while token != '(':
                temp.empilhar(token)
                token = pilha_de_execucao.desempilhar()

            pilha_de_execucao.empilhar(_resolver_expressao_flat(temp))
            temp = Pilha()

    resultado = _resolver_expressao_flat(pilha_de_execucao)

    return resultado
