from collections import deque

class KleeneLanguage:
    def __init__(self, base, allow_empty=True):
        """
        Inicializa a linguagem com um conjunto (ou lista) de cadeias base.

        :param base: coleção (lista, tupla ou set) de cadeias (strings).
        :param allow_empty: se True, permite a cadeia vazia (ε).
        """
        self.base = set(base)
        self.allow_empty = allow_empty

    def __xor__(self, max_len):
        """
        Sobrescreve o operador circunflexo (^) para realizar a operação de fecho de Kleene
        até um comprimento máximo max_len.

        Exemplo de uso:
            L = KleeneLanguage(["0", "1"])
            resultado = L ^ 3     # fecho de Kleene até comprimento 3
        """
        if max_len == float('inf'):
            raise ValueError(
                "Fecho infinito gera cadeias infinitas. "
                "Use um gerador apropriado ou limite o tamanho."
            )

        return self._kleene_up_to_length(max_len)

    def _kleene_up_to_length(self, max_length):
        """
        Gera o conjunto de todas as cadeias do fecho de Kleene, com tamanho total
        (soma de caracteres) até max_length.
        """
        L = self.base
        # Usamos BFS (busca em largura) para evitar duplicadas
        queue = deque()
        visited = set()

       
        queue.append("")
        visited.add("")

        results = []

        while queue:
            current_str = queue.popleft()
            results.append(current_str)

            for w in L:
                new_str = current_str + w
                if len(new_str) <= max_length and new_str not in visited:
                    visited.add(new_str)
                    queue.append(new_str)
        if not self.allow_empty:
            results.remove("")

        return results

if __name__ == "__main__":

    L = KleeneLanguage(["0", "1"], allow_empty=True)
    resultado_ate_3 = L ^ 3
    print("Fecho de Kleene até comprimento 3 (L = {0,1}):")
    print(resultado_ate_3)


    L2 = KleeneLanguage(["ab", "c"], allow_empty=False)
    resultado_ate_4 = L2 ^ 4
    print("\nFecho de Kleene até comprimento 4 (L = {ab, c}, sem ε):")
    print(resultado_ate_4)

    resultado_ate_5 = L ^ 5
    print("\nFecho de Kleene até comprimento 5 (L = {0, 1}, sem ε):")
    print(resultado_ate_5)