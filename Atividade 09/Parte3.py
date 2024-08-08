# Knapsack Problem
# Dynamic programming solution

def max(a, b):
    if a > b:
        return a
    else:
        return b

weights = [4, 5, 6, 8]
values = [7, 5, 4, 7]
n = 4
W = 13
T = [[-1 for i in range(W+1)] for j in range(n+1)]
for i in range(n+1):
    T[i][0] = 0
for j in range(W+1):
    T[0][j] = 0
for i in range(1, n+1):
    for j in range(1, W+1):
        if j < weights[i-1]:
            T[i][j] = T[i-1][j]
        else:
            T[i][j] = max(T[i-1][j], T[i-1][j-weights[i-1]] + values[i-1])
print("Valor máximo:", T[n][W])

# Function to find the selected items
def find_selected_items(T, weights, values, n, W):
    selected_items = []
    total_weight = 0
    total_value = 0
    i = n
    j = W
    while i > 0 and j > 0:
        if T[i][j] != T[i-1][j]:
            selected_items.append(i-1)
            total_weight += weights[i-1]
            total_value += values[i-1]
            j -= weights[i-1]
        i -= 1
    return selected_items, total_weight, total_value

selected_items, total_weight, total_value = find_selected_items(T, weights, values, n, W)
# print("Itens selecionados:", selected_items)
print("Peso total:", total_weight)
print("Valor total:", total_value)

# Function to write output to a FASTA file
def write_fasta(filename, total_weight, total_value):
    with open(filename, 'w') as f:
        f.write(">Total Weight\n")
        f.write(str(total_weight) + "\n")
        f.write(">Total Value\n")
        f.write(str(total_value) + "\n")

# Write the output to a FASTA file
write_fasta("C:/Users/gabri/OneDrive/Documentos/UNIFESP/Semestres/3° semestre/Algoritmos em Bioinformática/Atividade 09/Parte4.fasta", selected_items, total_weight, total_value)

# Recursive solution
# Time complexity: O(2^n)
# Space complexity: O(n)
def knapsack(i, j):
    if i == 0 or j == 0:
        return 0
    if T[i][j] != -1:
        return T[i][j]
    if j < weights[i-1]:
        T[i][j] = knapsack(i-1, j)
    else:
        T[i][j] = max(knapsack(i-1, j), knapsack(i-1, j-weights[i-1]) + values[i-1])
    return T[i][j]

weights = [4, 5, 6, 8]
values = [7, 5, 4, 7]
n = 4
W = 13
T = [[-1 for i in range(W+1)] for j in range(n+1)]
print("Valor máximo (recursivo):", knapsack(n, W))