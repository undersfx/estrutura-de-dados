"""
Criar uma função que retorne mínimo e máximo de uma sequência numérica aleatória

Para a criação do algorítimo só podem ser utilizados os recursos abaixo:
- Estruturas de decisão (if, elif e else)
- Comparação (==, !=, >=, <=) e Atribuição
- Recursão
- Funções de própria autoria
- Laços (desafio adicional: não usar laço)

Em docstring deve ser informada a complexidade em tempo e espaço.
"""

from math import inf


def for_loop_minmax(lista: list) -> tuple:
    """
    Implementação iterativa comparando todos elementos da lista com os valores
    de maior e menor armazenados anteriormente.

    Doctests:
    >>> for_loop_minmax([0, 1, 2, 3])
    (0, 3)

    >>> for_loop_minmax([3, 2, 1, 0])
    (0, 3)

    >>> for_loop_minmax([0])
    (0, 0)


    Complexidade de Tempo:
    4 atribuições   -> f(n) = c -> 1
    2 comparações   -> f(n) = c -> 1
    1 decisão       -> f(n) = c -> 1
    1 laço          -> f(n) = n -> n

    Total: f(n) = 3 + n -> O(n)


    Complexidade de Espaço:
    3 variaveis (int) -> f(n) = c -> 1

    Total: f(n) = 3 -> O(1)
    """
    menor = inf
    maior = -inf

    if not lista:
        raise ValueError

    for item in lista:
        if item < menor:
            menor = item

        if item > maior:
            maior = item

    return (menor, maior)


def recursive_minmax(lista: list) -> tuple:
    """
    Implementação recursiva deixando todas as comparações na pilha de chamadas
    até alcançar a mínima lista para resolver a comparação dos elementos

    Doctests:
    >>> recursive_minmax([0, 1, 2, 3])
    (0, 3)

    >>> recursive_minmax([3, 2, 1, 0])
    (0, 3)

    >>> recursive_minmax([0])
    (0, 0)

    Complexidade de Tempo:
    2n comparações      -> f(n) = 2n -> n
    2n slicing          -> f(n) = 2n -> n
    2n+2 atribuições    -> f(n) = 2n + 2 -> n
    2n+1 decisão        -> f(n) = 2n + 1 -> n

    Total: f(n) = 4n -> O(n)


    Complexidade de Espaço:
    2 funções           -> f(n) = c -> 1
    2n variaveis (list) -> f(n) = 2n -> n
    n^2 call stack      -> f(n) = n^2 -> n^2

    Total: f(n) = 1 + n + n^2 -> O(n^2)
    """
    def recursive_menor(lista: list) -> int:
        primeiro = lista[0]

        if tamanho(lista) == 1:
            return primeiro
        else:
            menor = recursive_menor(lista[1:])
            return menor if menor < primeiro else primeiro


    def recursive_maior(lista: list) -> int:
        primeiro = lista[0]

        if tamanho(lista) == 1:
            return primeiro
        else:
            maior = recursive_maior(lista[1:])
            return maior if maior > primeiro else primeiro


    if not lista:
        raise ValueError

    _menor = recursive_menor(lista)
    _maior = recursive_maior(lista)

    return (_menor, _maior)


def tail_recursive_minmax(lista: list) -> tuple:
    """
    Implementação recursiva com otimização de calda passando o maior ou menor
    valor encontrado até o momento como parâmetro para a próxima chamada.

    Doctests:
    >>> tail_recursive_minmax([0, 1, 2, 3])
    (0, 3)

    >>> tail_recursive_minmax([3, 2, 1, 0])
    (0, 3)

    >>> tail_recursive_minmax([0])
    (0, 0)

    Complexidade de Tempo:
    2n slicing          -> f(n) = 2n -> n
    2n comparações      -> f(n) = 2n -> n
    2n+2 atribuições    -> f(n) = 2n + 2 -> n
    2n+1 decisão        -> f(n) = 2n + 1 -> n

    Total: f(n) = 4n -> O(n)


    Complexidade de Espaço:
    2 funções           -> f(n) = c -> 1
    2 variaveis (int)   -> f(n) = c -> 1
    1 variavel (list)   -> f(n) = n - 1 -> n

    Total: f(n) = 2 + n -> O(n)
    """
    def tail_recursive_menor(lista: list, tail=inf) -> int:
        primeiro = lista[0]

        if primeiro < tail:
            tail = primeiro

        if tamanho(lista) == 1:
            return tail

        return tail_recursive_menor(lista[1:], tail)


    def tail_recursive_maior(lista: list, tail=-inf) -> int:
        primeiro = lista[0]

        if primeiro > tail:
            tail = primeiro

        if tamanho(lista) == 1:
            return tail

        return tail_recursive_maior(lista[1:], tail)

    if not lista:
        raise ValueError

    _menor = tail_recursive_menor(lista)
    _maior = tail_recursive_maior(lista)

    return (_menor, _maior)


# Helper Functions ------------------------------------------
def tamanho(iteravel):
    '''
    >>> tamanho([1, 2, 3])
    3

    >>> tamanho([1])
    1

    >>> tamanho([])
    0

    Complexidade de Tempo:
    n atribuições   -> f(n) = c -> 1
    1 descisão      -> f(n) = c -> 1
    1 laço          -> f(n) = n -> n

    Total: f(n) = 2 + n -> O(n)


    Complexidade de Espaço:
    1 variavel (int) -> f(n) = c -> 1

    Total: f(n) = 1 -> O(1)
    '''
    i = 0
    if not iteravel:
        return 0

    while True:
        try:
            iteravel[i]
        except IndexError:
            break
        i += 1

    return i