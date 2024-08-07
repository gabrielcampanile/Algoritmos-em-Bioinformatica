from Bio import SeqIO, pairwise2
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.pairwise2 import format_alignment

# Lendo as sequências
seq = "C:/Users/gabri/OneDrive/Documentos/UNIFESP/Semestres/3° semestre/Algoritmos em Bioinformática/Atividade 08/Seq1Seq2_corrigido.fasta"
read_seq = list(SeqIO.parse(seq, "fasta"))    

# Separando as sequências
seq1 = read_seq[0].seq
# print(seq1)
seq2 = read_seq[1].seq
# print(seq2)

# Calculando a identidade
identidade = 0

for i in range(len(seq1)):
    if seq1[i] == seq2[i] and seq1[i] != "-":
        identidade += 1

identidade_media = identidade / len(seq1) * 100

print("Identidade:", identidade)
print("Identidade média:", identidade_media, "%")

# Definindo as variáveis
index = {"A": 0, "C": 1, "G": 2, "T": 3, "-": 4}

# Matriz de score
score = [[5, -1, -2, -1, -3],
        [-1, 5, -3, -2, -4],
        [-2, -3, 5, -2, -2],
        [-1, -2, -2, 5, -1],
        [-3, -4, -2, -1, 0]]
                         
# Calculando o score
escore = 0

for i in range(len(seq1)):
    nucleotideo1 = seq1[i]
    nucleotideo2 = seq2[i]
    escore += score[index[nucleotideo1]][index[nucleotideo2]]

print("Escore:", escore)

# Alinhamento global
aligment1 = pairwise2.align.globalxx(seq1, seq2)
aligment2 = pairwise2.align.globalms(seq1, seq2, 5, -1, -2, -1)

print(format_alignment(*aligment1[0]))
print(format_alignment(*aligment2[0]))


