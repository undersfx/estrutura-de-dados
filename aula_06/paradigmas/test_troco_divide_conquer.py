import unittest
from collections import defaultdict
from itertools import combinations


def calcular_troco_nao_multiplo(valor: int, tipos_de_notas: set):
    """
    Divisão:
    - Considere a cada nota como parte da solução.
      (Se valor da nota maior que o total, ignorar, não é possível)
    - Considerar não usar uma nota de um tipo

    Conquista:
    - Considerar o menor número total entre a soma de notas 
    """
    def calcular_troco(valor: int, tipos_de_notas: set, solucao_inicial={}):
        notas_ordendas = sorted(tipos_de_notas, reverse=True)
        frequencia = defaultdict(int)
        frequencia.update(solucao_inicial)

        for nota in notas_ordendas:
            quantidade_de_notas, valor = divmod(valor, nota)
            if quantidade_de_notas > 0:
                frequencia[nota] += quantidade_de_notas
        
        if valor == 0:
            return dict(frequencia)
        else:
            return {}

    resultados = []
    for combination in combinations(tipos_de_notas, len(tipos_de_notas) - 1):
        troco_sem_uma_nota = calcular_troco(valor, set(combination))
        resultados.append(troco_sem_uma_nota)

    for nota in tipos_de_notas:
        troco_pelo_menos_nota = calcular_troco(valor - nota, tipos_de_notas, {nota: 1})
        resultados.append(troco_pelo_menos_nota)

    ganhador = {}
    for resultado in resultados:
        num_notas = sum(resultado.values())

        if not ganhador or num_notas < num_notas_ganhador:
            ganhador = resultado
            num_notas_ganhador = num_notas
            continue

    return ganhador


class TestTrocoNaoMultiplo(unittest.TestCase):
    def test_troco_nao_multipĺo_vazia(self):
        self.assertDictEqual({}, calcular_troco_nao_multiplo(9, {10}))
    def test_troco_nao_multipĺo_uma_nota(self):
        self.assertDictEqual({10: 1}, calcular_troco_nao_multiplo(10, {10}))
    def test_troco_nao_multipĺo_notas_multiplas(self):
        self.assertDictEqual({10: 2, 5: 1, 1: 4}, calcular_troco_nao_multiplo(29, {1, 5, 10}))
    def test_troco_nao_multipĺo_notas_nao_multiplas(self):
        self.assertDictEqual({7: 2}, calcular_troco_nao_multiplo(14, {1, 7, 10}))
