# Exemplo 2: Identificação de motivos em uma sequência de DNA e gravação das posições

# Função para ler a sequência de DNA de um arquivo FASTA
def ler_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence

# Função para buscar uma subsequência específica na sequência de DNA
def encontrar_motivo(dna_sequence, motivo):
    posicoes = []
    posicao_atual = dna_sequence.find(motivo)
    while posicao_atual != -1:
        posicoes.append(posicao_atual)
        posicao_atual = dna_sequence.find(motivo, posicao_atual + 1)
    return posicoes

# Função para salvar as posições em um arquivo de saída
def salvar_posicoes(posicoes, output_file):
    with open(output_file, 'w') as file:
        for pos in posicoes:
            file.write(f"Posição: {pos}\n")

# Nome do arquivo de entrada e saída
input_filename = 'sequencia_dna.fasta'
output_filename = 'posicoes_motivo.txt'

# Motivo a ser encontrado
motivo = 'ATG'

# Leitura da sequência de DNA a partir do arquivo FASTA
sequencia_dna = ler_fasta(input_filename)

# Buscar o motivo na sequência de DNA
posicoes_motivo = encontrar_motivo(sequencia_dna, motivo)

# Salvando as posições onde o motivo foi encontrado em um arquivo de saída
salvar_posicoes(posicoes_motivo, output_filename)

print(f"As posições do motivo '{motivo}' foram salvas em '{output_filename}'.")
