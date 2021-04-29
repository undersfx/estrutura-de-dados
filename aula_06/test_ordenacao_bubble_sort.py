import unittest


def ordenar(seq):
<<<<<<< HEAD
    pass
    # [5, 1, 3, 2] original
    # [1, 3, 2, 5] passada 1
    # [1, 2, 3, 5] passada2

    # [5, 4, 3, 2] original
    # [4, 3, 2, 5] original
    # [3, 2, 4, 5] original
    # [2, 3, 4, 5] original  O (n ** 2)
=======
    for i in range(len(seq)):
        sentinel = True

        for j in range(i + 1, len(seq)):
            if seq[j] < seq[i]:
                seq[j], seq[i] = seq[i], seq[j]
                sentinel = False
        
        if sentinel: return seq

    return seq

>>>>>>> add: execicio algoritimos de ordenaçao

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], ordenar([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], ordenar([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], ordenar([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ordenar([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_ordenada(self):
        self.assertListEqual([0, 1, 2, 3], ordenar([0, 1, 2, 3]))


if __name__ == '__main__':
    unittest.main()