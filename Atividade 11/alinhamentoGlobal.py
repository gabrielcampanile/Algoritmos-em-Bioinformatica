def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-1):
    # Inicialização da matriz de escores
    n, m = len(seq1), len(seq2)
    matriz = [[0 for j in range(m + 1)] for i in range(n + 1)]
    
    # Preenchimento da primeira linha e primeira coluna com penalidades de gap
    for i in range(1, n + 1):
        matriz[i][0] = i * gap
    for j in range(1, m + 1):
        matriz[0][j] = j * gap
    
    # Preenchimento da matriz de escores
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                score_diag = matriz[i - 1][j - 1] + match
            else:
                score_diag = matriz[i - 1][j - 1] + mismatch
            score_up = matriz[i - 1][j] + gap
            score_left = matriz[i][j - 1] + gap
            matriz[i][j] = max(score_diag, score_up, score_left)
    
    # Traceback para construir o alinhamento
    alinhamento1, alinhamento2 = '', ''
    i, j = n, m
    while i > 0 and j > 0:
        current_score = matriz[i][j]
        if current_score == matriz[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            alinhamento1 = seq1[i - 1] + alinhamento1
            alinhamento2 = seq2[j - 1] + alinhamento2
            i -= 1
            j -= 1
        elif current_score == matriz[i - 1][j] + gap:
            alinhamento1 = seq1[i - 1] + alinhamento1
            alinhamento2 = '-' + alinhamento2
            i -= 1
        else:
            alinhamento1 = '-' + alinhamento1
            alinhamento2 = seq2[j - 1] + alinhamento2
            j -= 1
    
    while i > 0:
        alinhamento1 = seq1[i - 1] + alinhamento1
        alinhamento2 = '-' + alinhamento2
        i -= 1
    while j > 0:
        alinhamento1 = '-' + alinhamento1
        alinhamento2 = seq2[j - 1] + alinhamento2
        j -= 1

    return matriz, alinhamento1, alinhamento2
