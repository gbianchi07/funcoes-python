def exibir_mensagem():
    print('olá')


def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f'area: {area}')


for i in range(10):
    exibir_mensagem()  # chamada de funçao  sempre depois de definir a funçaõ primeiro

    b = float(input('Base do triangulo: '))
    a = float(input('altura do triangulo: '))
    calcular_area_triangulo(b,  a)


def par_ou_impar(numero):
    if numero % 2 == 0:
        print('o numero é par')

    else:
        print('o numero é impar')


print('1-Exibir uma mensagem')
print('2- Verificar se número é par ou impar')
print('3- calcular a área de um triangulo')
print('4-finalizar')
opcao = int(input('escolha uma opção: '))
if opcao == 1:
    exibir_mensagem()
elif opcao == 2:
    numero = int(input('informe um numero: '))
    par_ou_impar(numero)
elif opcao == 3:
    b = float(input('Base do triangulo: '))
    a = float(input('altura do triangulo: '))
    calcular_area_triangulo(b, a)


elif opcao == 4:
    print('fim da execução')
