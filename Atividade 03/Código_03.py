# Importar dados FASTA utilizando a biblioteca Biopython:
from Bio import SeqIO
import matplotlib.pyplot as plt

# Lista para armazenar os dados de conteúdo de GC e temperatura de melting (Tm)
conteudp_GC = []
conteudo_TM = []
n = 0

# Abrir arquivo de saída para salvar os resultados
with open('C:/Users/gabri/OneDrive/Documentos/UNIFESP/3° semestre/Algoritmos em Bioinformática/Atividade 03/Resultados.txt', 'w') as output_file:
    for record in SeqIO.parse("C:/Users/gabri/OneDrive/Documentos/UNIFESP/3° semestre/Algoritmos em Bioinformática/Atividade 03/dengue.fasta", "fasta"):
        n += 1
        
        # Extrair a sequência do registro
        sequence = str(record.seq)

        # Contar os nucleotídeos
        count_A = sequence.count('A')
        count_C = sequence.count('C')
        count_T = sequence.count('T')
        count_G = sequence.count('G')
        total_count = len(sequence)

        # Calculando o conteúdo de GC
        GC = count_G + count_C
        GC_percent = GC / total_count * 100

        # Calculando a temperatura de melting (Tm)
        TM = 64.9 + (0.41 * GC_percent) - (500 / total_count)

        # Salvando informações em forma de lista para o gráfico
        conteudp_GC.append(GC_percent)
        conteudo_TM.append(TM)

        # Escrever os resultados em um arquivo de saída
        output_file.write("Sequencia {}:\n".format(n))
        output_file.write("Contagem de nucleotideos:\n")
        output_file.write("A: {}\n".format(count_A))
        output_file.write("C: {}\n".format(count_C))
        output_file.write("T: {}\n".format(count_T))
        output_file.write("G: {}\n".format(count_G))
        output_file.write("Total de nucleotideos: {}\n".format(total_count))
        output_file.write("Conteudo de GC: {:.2f}%\n".format(GC_percent))
        output_file.write("Temperatura de Melting (Tm): {:.2f}\n".format(TM))
        output_file.write("\n")

# Plotar gráfico de pontos do conteúdo de GC e temperatura de melting (Tm)
plt.scatter(conteudp_GC, conteudo_TM, marker='o', color='blue')
plt.title('Conteúdo de GC x Temperatura de Melting (Tm)')
plt.xlabel('Conteúdo de GC (%)')
plt.ylabel('Temperatura de Melting (Tm)')
plt.grid(True)
plt.show()