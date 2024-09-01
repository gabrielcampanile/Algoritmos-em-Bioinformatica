# Exemplo 1: Leitura de Sequência de DNA de um arquivo FASTA e cálculo da frequência de nucleotídeos

# Função para ler a sequência de DNA de um arquivo FASTA
def ler_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Ignora a linha de cabeçalho (inicia com '>')
        sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence

# Função para contar os nucleotídeos em uma sequência de DNA
def contar_nucleotideos(dna_sequence):
    frequencias = {
        'A': dna_sequence.count('A'),
        'T': dna_sequence.count('T'),
        'C': dna_sequence.count('C'),
        'G': dna_sequence.count('G')
    }
    return frequencias

# Função para salvar as frequências em um arquivo de saída
def salvar_frequencias(frequencias, output_file):
    with open(output_file, 'w') as file:
        for nucleotideo, frequencia in frequencias.items():
            file.write(f"{nucleotideo}: {frequencia}\n")

# Nome do arquivo de entrada e saída
input_filename = 'sequencia_dna.fasta'
output_filename = 'frequencias_nucleotideos.txt'

# Leitura da sequência de DNA a partir do arquivo FASTA
sequencia_dna = ler_fasta(input_filename)

# Cálculo das frequências dos nucleotídeos
frequencias = contar_nucleotideos(sequencia_dna)

# Salvando as frequências em um arquivo de saída
salvar_frequencias(frequencias, output_filename)

print(f"As frequências dos nucleotídeos foram salvas em '{output_filename}'.")
