from Funcoes import *
from AtaExercicios import ataTurma
from TurmaProfessor import testandotp
from DisciplinaAluno import testandoda


def menu_opcoes_relatorio():
    print("""
   1 - Ata de exercício
   2 - Lista de turmas por professor
   3 - Lista de disciplinas por aluno
   
   0 - Sair
   """)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 3)


def menu_relatorio():
    while True:
        opcao = menu_opcoes_relatorio()
        if opcao == 0:
            break
        elif opcao == 1:
            ataTurma()
        elif opcao == 2:
            testandotp()
        elif opcao == 3:
            testandoda()