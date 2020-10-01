import os #Lib para manipulacao do S.O.

def pede_nome():
    return (input("Nome: "))


#edita o cpf em numeros para uma string formata com pontos e tracos
def pede_CPF():
    while True:
        try:
            cpfa = input("CPF (Apenas números): ")
            if len(cpfa) == 11:
                # essa parte edita o cpf no formato 000.000.000-00
                return "%s.%s.%s-%s" % (cpfa[0:3], cpfa[3:6], cpfa[6:9], cpfa[9:11])
        except ValueError:
            print("Número de cpf inválido, digite novamente")

#funcao pede codigos para disciplinas
def pede_codigo():
    while True:
        try:
            codd = input("Código com 5 digitos(apenas numeros): ")
            if len(codd) == 5:
                return codd
        except ValueError:
            print("Código inválido, digite novamente")

#funcao para validar as opcoes dos menus
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            num = int(input(pergunta))
            if inicio <= num <= fim:
                return (num)
            # raise ValueError
        except ValueError:
            print("Número inválido. Digite um número entre %d e %d" % (inicio, fim))

#funcao que valida e transforma o numero do periodo com pontos, periodo eh sinonimo de semestre
def pede_periodo():
    while True:
        try:
            per = input("Período com 5 digitos (Apenas números): ")
            if len(per) == 5:
                return "%s.%s" % (per[0:4], per[4:5])
        except ValueError:
            print("Período inválido, digite novamente")

#Limpa a tela no CMD(prompt de comando)
def limpa_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

