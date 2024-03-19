sequence = input("Digite a sequência de nucleotídeos: ")

count_A = sequence.count('A')
count_C = sequence.count('C')
count_T = sequence.count('T')
count_G = sequence.count('G')

total = count_A + count_C + count_T + count_G

print("Quantidade de A:", count_A)
print("Quantidade de C:", count_C)
print("Quantidade de G:", count_G)
print("Quantidade de T:", count_T)
print("Total de nucleotídeos:", total)