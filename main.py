import datetime

ano_atual = datetime.datetime.now().year
def funcao():
    nome = input("Qual o seu nome?").title()
    try:
        idade = int(input("Idade:"))
    except ValueError:
        print("Só números inteiros!")
        idade = int(input("Idade:"))
    print(f"Olá {nome.split()[0]}!")
    print(f"Você nasceu em {ano_atual - idade}")
    print("Prazer em conhecê-lo")


if __name__ == "__main__":
    funcao()
