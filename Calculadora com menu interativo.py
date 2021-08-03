
from time import sleep

print("-"*40)
print("Seja bem vindo ao nosso menu interativo! ")
print("-"*40)

n1 = float(input("Digite o primeiro valor: "))
n2 =float(input("Digite o segundo valor: "))

opcao = 0

while opcao != 10:
    print("""
    [1] somar,
    [2] subitrair,
    [3] multiplicar,
    [4] dividir,
    [5]resto da divisão inteira,
    [6] divisão inteira,
    [7] porcentagem,
    [8] maior valor,
    [9]novo número,
    [10] sair do programa
    """)

    print("-"*30)
    opcao = float(input("Qual é sua opção? "))
    print("-"*30)
    if opcao == 1:
        soma = n1 + n2
        print(f"a soma entre {n1:.1f} + {n2:.1f} = {soma:.1f}")
    elif opcao ==2:
        subtrair = n1 - n2
        print(f'A subtração entre {n1}  - {n2} = {subtrair}')
    elif opcao == 3:
        multiplica = n1 * n2
        print(f"A multiplicação entre {n1} x {n2} = {multiplica}")
    elif opcao == 4:
        divisão = n1 / n2
        print(f"A divisão entre {n1} / {n2} = {divisão:.2f}")
    elif opcao == 5:
     restoDivisão = n1 % n2
     print(f'o resto da divisão entre {n1} é  {n2} = {restoDivisão}')
    if opcao == 6:
        divisãoInteira = n1 // n2
        print(f'a divisão inteira entre {n1} e {n2} e igual a {divisãoInteira}')
    elif opcao == 7:
        porcentagem = n1 * n2 /100
        print(f"A porcentagem de {n1} % {n2} e igual a{porcentagem}")
    elif opcao == 8:
        if n1 > n2:
            maior =n1
        else:
            maior = n2
            print(f"entre {n1} e {n2} o maior é {maior}")
    elif opcao == 9:
        print('Informe os números novamente: ')
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    if opcao >= 10:
            print("Saindo do programa, até logo!")
    else:
        print("Valor inválido, tente novamente!")
print("-"*30)
sleep(1)
print('Fim do programa, volte sempre!')


