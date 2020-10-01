#ARQUIVO QUE NAO FOI USADO :/

import Turmas

#Eu faço pesquisar a turma  q ele deseja ler e exibo ela
def ataTurma():
    turmac = int(input("Digite o código da turma que deseja consultar: "))

    arquivoler = open("Turmas.txt", "r", encoding="utf-8")

    if turmac in arquivoler:
            print(cod)
    else:
        print ("Turma não encontrada")
