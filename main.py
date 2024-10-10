import datetime

agora = datetime.datetime.now()

nome = input("Qual é o seu nome:")

anoQueNasceu = int(input("Coloque o ano em que você nasceu:"))

idade = agora.year - anoQueNasceu

print("Seja bem vindo " + nome + " Sua idade é " + str(idade) + "anos")