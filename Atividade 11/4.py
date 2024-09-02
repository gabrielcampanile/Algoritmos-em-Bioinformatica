from alinhamentoGlobal import needleman_wunsch

# Definindo as sequências
seq1 = "AGCT"
seq2 = "ATGCT"

# Aplicando o algoritmo de Needleman-Wunsch
matriz, alinhamento1, alinhamento2 = needleman_wunsch(seq1, seq2)

# Exibindo a matriz de escores
print("Matriz de Escores:")
for row in matriz:
    print(row)

# Exibindo o alinhamento final
print("\nAlinhamento Final:")
print(alinhamento1)
print(alinhamento2)
