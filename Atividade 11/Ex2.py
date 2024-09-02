def global_alignment(seq1, seq2, match_score, mismatch_penalty, gap_penalty):
    m = len(seq1)
    n = len(seq2)
    score_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        score_matrix[i][0] = i * gap_penalty
    for j in range(1, n + 1):
        score_matrix[0][j] = j * gap_penalty

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                diag = score_matrix[i - 1][j - 1] + match_score
            else:
                diag = score_matrix[i - 1][j - 1] + mismatch_penalty
            up = score_matrix[i - 1][j] + gap_penalty
            left = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(diag, up, left)

    align1 = ""
    align2 = ""
    i = m
    j = n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and score_matrix[i][j] == score_matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty):
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif i > 0 and score_matrix[i][j] == score_matrix[i - 1][j] + gap_penalty:
            align1 = seq1[i - 1] + align1
            align2 = '-' + align2
            i -= 1
        else:
            align1 = '-' + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    return align1, align2, score_matrix

def write_fasta(seq1, seq2, id1, id2, filename, score_matrix):
    with open(filename, 'w') as file:
        file.write(f">{id1}\n{seq1}\n")
        file.write(f">{id2}\n{seq2}\n")
        file.write("\n# Score Matrix\n")
        for row in score_matrix:
            file.write(' '.join(map(str, row)) + '\n')

seq1 = "GATACA"
seq2 = "TAGCU"
match_score = 1
mismatch_penalty = -1
gap_penalty = -2

align1, align2, score_matrix = global_alignment(seq1, seq2, match_score, mismatch_penalty, gap_penalty)
print("Alignment 1:", align1)
print("Alignment 2:", align2)
print("Score Matrix:")
for row in score_matrix:
    print(row)

write_fasta(align1, align2, "aligned_seq1", "aligned_seq2", "alignment_output.fasta", score_matrix)