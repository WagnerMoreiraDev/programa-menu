from time import sleep
import os

def screen_clear():   
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')   
   

print("-"*40)
print("Seja bem vindo ao nosso menu interativo! ")
print("-"*40)
while True:
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    print("""
    [1] somar,
    [2] subitrair,
    [3] multiplicar,
    [4] dividir,
    [5] porcentagem,
    [6] maior valor,
    [7]novo número,
    [8] sair do programa
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
        porcentagem = n1 * n2 /100
        print(f"A porcentagem de {n1} % {n2} e igual a{porcentagem}")
    elif opcao == 6:
        if n1 > n2:
            maior =n1
        else:
            maior = n2
            print(f"entre {n1} e {n2} o maior é {maior}")
    elif opcao == 7:
        print('Informe os números novamente: ')    
    elif opcao >= 8:
            print("Saindo do programa, até logo!")
            break
    else:
        print("Valor inválido, tente novamente!")
    print("\n"*5)
    input('Pressione "Enter" para continuar')
    screen_clear()
print("-"*30)
sleep(1)
print('Fim do programa, volte sempre!')
