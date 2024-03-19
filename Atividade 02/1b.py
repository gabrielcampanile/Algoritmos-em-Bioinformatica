# 1b - Importar dados FASTA utilizando a biblioteca Biopython:

from Bio import SeqIO

# Carregar o arquivo FASTA usando o Biopython
record = SeqIO.read("virus_dengue.fasta", "fasta")
# Extrair a sequência do registro
sequence = str(record.seq)

# for seq_record in SeqIO.parse("virus_dengue.fasta", "fasta"):
#     sequence = str(seq_record.seq)

print("Sequência de DNA do arquivo Fasta (Biopython):")
print(sequence)

# Contar os nucleotídeos
count_A = sequence.count('A')
count_C = sequence.count('C')
count_T = sequence.count('T')
count_G = sequence.count('G')
total_count = len(sequence)

print("Quantidade de A:", count_A)
print("Quantidade de C:", count_C)
print("Quantidade de G:", count_G)
print("Quantidade de T:", count_T)
print("Total de nucleotídeos:", total_count)

# Escrever os resultados em um arquivo de saída
with open('contagem_nucleotideos_2b.txt', 'w') as output_file:
    output_file.write("Contagem de nucleotideos:\n")
    output_file.write("A: {}\n".format(count_A))
    output_file.write("C: {}\n".format(count_C))
    output_file.write("T: {}\n".format(count_T))
    output_file.write("G: {}\n".format(count_G))
    output_file.write("Total: {}\n".format(total_count))

print("\nArquivo contagem_nucleotideos_2b.txt criado com sucesso!")