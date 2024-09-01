# Exemplo 3: Tradução de Sequência de DNA para Proteína

# Dicionário do código genético padrão (códons para aminoácidos)
codigo_genetico = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

# Função para ler a sequência de DNA de um arquivo FASTA
def ler_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence

# Função para traduzir uma sequência de DNA em uma sequência de proteína
def traduzir_dna_para_proteina(dna_sequence):
    proteina = []
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i + 3]
        aminoacido = codigo_genetico.get(codon, 'X')  # 'X' para códons desconhecidos
        proteina.append(aminoacido)
    return ''.join(proteina)

# Função para salvar a sequência de proteína em um arquivo de saída
def salvar_proteina(protein_sequence, output_file):
    with open(output_file, 'w') as file:
        file.write(f">Proteina traduzida\n")
        file.write(protein_sequence)

# Nome do arquivo de entrada e saída
input_filename = 'sequencia_dna.fasta'
output_filename = 'sequencia_proteina.txt'

# Leitura da sequência de DNA a partir do arquivo FASTA
sequencia_dna = ler_fasta(input_filename)

# Tradução da sequência de DNA para uma sequência de proteína
sequencia_proteina = traduzir_dna_para_proteina(sequencia_dna)

# Salvando a sequência de proteína em um arquivo de saída
salvar_proteina(sequencia_proteina, output_filename)

print(f"A sequência de proteína foi salva em '{output_filename}'.")
