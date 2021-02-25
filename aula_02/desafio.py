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
    Implementação iterativa comparando todos elementos da lista com
    os valores de maior e menor armazenados anteriormente.

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
        raise ValueError('Lista vazia')

    for item in lista:
        if item < menor:
            menor = item

        if item > maior:
            maior = item

    return (menor, maior)


def recursive_minmax(lista) -> tuple:
    """
    Implementação recursiva transformando o objeto lista em um iterador.

    Doctests:
    >>> recursive_minmax([0, 1, 2, 3])
    (0, 3)

    >>> recursive_minmax([3, 2, 1, 0])
    (0, 3)

    >>> recursive_minmax([0])
    (0, 0)

    Complexidade de Tempo:
    2n comparações      -> f(n) = 2n -> n
    2n+1 atribuições    -> f(n) = 2n + 1 -> n
    2n+1 decisões        -> f(n) = 2n + 1 -> n

    Total: f(n) = 3n -> O(n)


    Complexidade de Espaço:
    1 função        -> f(n) = c -> 1
    1 iterador      -> f(n) = c -> 1
    n call stack    -> f(n) = n -> n

    Total: f(n) = 2 + n -> O(n)
    """
    def _recursive_minmax(iteravel, _min, _max):
        try:
            elemento = next(iteravel)
        except StopIteration:
            return _min, _max
        else:
            if elemento < _min:
                _min = elemento
            if elemento > _max:
                _max = elemento
            return _recursive_minmax(iteravel, _min, _max)


    iteravel = iter(lista)
    _menor, _maior = _recursive_minmax(iteravel, inf, -inf)
    if _menor is inf:
        raise ValueError('Lista vazia')

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
    2n comparações      -> f(n) = 2n -> n
    4n atribuições      -> f(n) = 4n -> n
    3n decisões         -> f(n) = 3n -> n

    Total: f(n) = 3n -> O(n)


    Complexidade de Espaço:
    1 função            -> f(n) = c -> 1
    4n atribuições      -> f(n) = 4c -> 1
    2 variaveis (int)   -> f(n) = c -> 1

    Total: f(n) = 2 + n -> O(1)
    """
    def _tail_recursive_minmax(lista, pos, _min, _max):
        if pos == len(lista):
            return _min, _max

        i = lista[pos]

        if i < _min:
            _min = i

        if i > _max:
            _max = i

        pos += 1
        return _tail_recursive_minmax(lista, pos, _min, _max)

    return _tail_recursive_minmax(lista, 0, inf, -inf)


if __name__ == '__main__':
    for_loop_minmax([0, 1, 2, 3])
    recursive_minmax([0, 1, 2, 3])
    tail_recursive_minmax([0, 1, 2, 3])