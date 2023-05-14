# Inteligent Wordlist Generator
#
# By: Fabio Troncao
# Little Wordlist Generator
#
##################

import itertools
import random

ban = '''
                                                    '''

print('\n------------------\n\n L ! T T L E \033[32m3.0\033[m | WORDLISTGENERATOR\n\n-> by: Fábio Troncão\n\n------------------\n')

def generate_wordlist(keywords, file):
    # Adiciona as palavras-chave originais à wordlist
    for word in keywords:
        file.write(word + '\n')

    # Permutações
    for perm in itertools.permutations(keywords):
        file.write(''.join(perm) + '\n')

    # Combinações
    for i in range(2, len(keywords) + 1):
        for comb in itertools.combinations(keywords, i):
            file.write(''.join(comb) + '\n')

    # Mesclagens e inserções
    for word in keywords:
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                # Mescla aleatória
                merged = word[:i] + random.choice(keywords) + word[j:]
                file.write(merged + '\n')
                # Inserção aleatória
                for k in range(len(keywords)):
                    inserted = word[:i] + keywords[k] + word[i:]
                    file.write(inserted + '\n')


use_steps = 'y'
keywords = []
while True:
    strwords = input("\n\033[36m[?] Insira uma palavra (ou deixe em branco para continuar): ")
    if not strwords:
        break
    keywords.append(strwords)

# o seguinte codigo simula o exemplo da retirada de informaçoes pessoais a serem incluidos. 
# OBS quantos mais dados maior o decumento e maior o tamanho do arquivo.  

# use_steps = str(input("\n\033[36m[?] Quer inserir dados pessoais do alvo, para complementar? [y/N]: "))
# if use_steps == 'y':    
# 	first_name = str(input("\n\033[36m[*] Primeiro nome: "))       
# 	last_name = str(input("\n\033[36m[*] Ultimo nome: "))
# 	birthday = str(input("\n\033[36m[*] Aniversário - dia: "))
# 	month = str(input("\n\033[36m[*] Aniversário - mes: "))
# 	year = str(input("\n\033[36m[*] Aniversárioano: "))     
           
# keywords.extend([first_name, last_name, birthday, month, year])    


# O codigo comentado era o original mas devido ao gerar imensas palavras resolvi simplificar so para teste.
# keywords_up = [string.upper() for string in keywords]
# keywords_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
# keywords_numerics = '1234567890'

keywords_up = [string.upper() for string in keywords]
keywords_specials = '_\' '
keywords_numerics = '12'

if input('\n\033[36m[?] Quer usar caracteres maiúsculos? (y/n): ') == 'y':
	keywords.extend(keywords_up)
if input('\n\033[36m[?] Quer usar caracteres especiais? (y/n): ') == 'y':
	keywords.append(keywords_specials)
if input('\n\033[36m[?] Quer usar caracteres numéricos? (y/n): ') == 'y':
	keywords.append(keywords_numerics)

output_file = str(input("\n\033[36m[?] Insira o nome do arquivo de saída: "))
with open(output_file + '.txt', 'w') as file:
    generate_wordlist(keywords, file)

print("\n\033[32m[+] Wordlist gerada com sucesso! Nome do arquivo: {}\033[m".format(output_file))