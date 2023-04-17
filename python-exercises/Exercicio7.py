nome_arquivo = 'names.txt'

frequencia_names = {}
with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            if nome in frequencia_names:
                frequencia_names[nome] += 1
            else:
                frequencia_names[nome] = 1


for nome, frequencia in frequencia_names.items():
        
    print(f"{nome}: {frequencia}")