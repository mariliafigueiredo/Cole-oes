from collections import Counter

# contador de letras
texto1 = """
Após o download ser finalizado, abra-o e logo na primeira tela é importante marcar a checkbox Add Python 3.5 to PATH.
 Essa opção é importante para conseguirmos executar o Python dentro do Prompt de Comando do Windows.
Vamos selecionar a instalação customizada somente para vermos a instalação com mais detalhes. Na segunda 
tela, podemos clicar em Next. Já na terceira tela, também vamos deixar como está, mas vamos 
"""
# quebra o texto em palavras
print(texto1.split( ))

# quantas vezes cada letra "A"apareceu, em minúsculo
# Agora eu tenho a contagem de cada letra, eu quero saber o quão frequente apareceu a letra "A"
print(Counter(texto1.lower()))

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]  #O contador recebe um iterável ou um mapping, um dicionário
    proporcoes = Counter(dict(proporcoes))  #Vou pegar esse meu dicionário, na verdade vou criar um contador em cima dele
    mais_comuns = proporcoes.most_common(10) #E agora eu vou querer saber os mais comum – most_common() - 10 mais comuns
    for caractere, proporcao in mais_comuns:
        print(" {} => {:.2f}%".format(caractere, proporcao * 100))   #proporção em porcentagem formatação de dois dígitos decimais

print(analisa_frequencia_de_letras(texto1))

