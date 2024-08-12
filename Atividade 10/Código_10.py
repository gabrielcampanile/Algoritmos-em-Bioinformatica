import numpy as np

def smith_waterman(seq1, seq2, match=5, mismatch=-3, gap=-4):
    m, n = len(seq1), len(seq2)
    M = np.zeros((m + 1, n + 1), dtype=int)

    max_score = 0
    max_pos = None

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score_diag = M[i - 1, j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            score_up = M[i - 1, j] + gap
            score_left = M[i, j - 1] + gap
            M[i, j] = max(0, score_diag, score_up, score_left)

            if M[i, j] > max_score:
                max_score = M[i, j]
                max_pos = (i, j)

    aligned_seq1 = []
    aligned_seq2 = []
    i, j = max_pos

    while M[i, j] != 0:
        current_score = M[i, j]
        diagonal_score = M[i - 1, j - 1]
        up_score = M[i - 1, j]
        left_score = M[i, j - 1]

        if current_score == diagonal_score + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif current_score == up_score + gap:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append('-')
            i -= 1
        elif current_score == left_score + gap:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j - 1])
            j -= 1

    aligned_seq1 = ''.join(aligned_seq1[::-1])
    aligned_seq2 = ''.join(aligned_seq2[::-1])

    return max_score, aligned_seq1, aligned_seq2, M

# Teste com as sequências fornecidas
# seq1 = 'CGTGAATTCAT'
# seq2 = 'GACTTAC'
seq1 = 'GAATTCAGTTA'
seq2 = 'GGATCGA'

score, align1, align2, score_matrix = smith_waterman(seq2, seq1)

# Imprimindo a matriz de escore
print("Matriz de Escore:")
print(score_matrix)

# Exibindo o alinhamento e pontuação
print(f"\nPontuação: {score}")
print(f"Sequência 1 alinhada: {align1}")
print(f"Sequência 2 alinhada: {align2}")
