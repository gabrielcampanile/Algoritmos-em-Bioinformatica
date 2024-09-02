# 1a - Importar arquivo Fasta do Vírus da Dengue utilizando a importação de texto do Python:

# Abrir e ler o arquivo Fasta
with open('virus_dengue.fasta', 'r') as file:
    fasta_data = file.read()

# Extrair a sequência do arquivo Fasta
lines = fasta_data.split('\n')
sequence = ''.join(lines[1:])

print("Sequência de DNA do arquivo Fasta (importação de texto):")
print(sequence)

count_A = sequence.count('A')
count_C = sequence.count('C')
count_T = sequence.count('T')
count_G = sequence.count('G')

total = count_A + count_C + count_T + count_G

print("Quantidade de A:", count_A)
print("Quantidade de C:", count_C)
print("Quantidade de G:", count_G)
print("Quantidade de T:", count_T)
print("Total de nucleotideos:", total)

# Escrever os resultados em um arquivo de saída
with open('contagem_nucleotideos.txt', 'w') as output_file:
    output_file.write("Contagem de nucleotideos:\n")
    output_file.write("A: {}\n".format(count_A))
    output_file.write("C: {}\n".format(count_C))
    output_file.write("T: {}\n".format(count_T))
    output_file.write("G: {}\n".format(count_G))
    output_file.write("Total: {}\n".format(total))















# print("\n")
# f = open("contagem_de_nucleotideos.txt", "r")
# print(f.read())