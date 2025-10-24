# Crie um programa que solicita ao usuário que insira três
# notas e, em seguida, calcule a média dessas notas
# usando uma função. A função deve receber as três
# notas como argumentos e retornar a média. Por fim, o
# programa deve imprimir a média calculada.

notas = []


def pegar_nota():
    n = int(input(f"Informe a {len(notas)+1}ª nota (ou -1 para parar): "))
    notas.append(n)
   
def media():
    media_notas = sum(notas)/len(notas)
    print(media_notas)

while True:
    print('='*50)
    print('Calculadora de média')
    print('='*50)
    print('Selecione uma opção')
    print('1 - Adicionar nota ')
    print('2 - Calcular a média ')
    print('3 - Sair')
    op=int(input('->'))
    if op ==1:
        pegar_nota()
    elif op==2:
        media()
    elif op==3: 
        break
    else:
        print('\nOPÇÃO INVÁLIDA\n')