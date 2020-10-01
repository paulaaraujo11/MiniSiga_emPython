#----------------MENU PRINCIPAL----------------------#
#---ATRAVES DE MODULOS E PACOTES CHAMA TODOS OS ARQUIVOS, POR ONDE INICIA O PROGRAMA E MOSTRA O MENU PRINCIPAL QUE DIRECIONA OS MENUS SECUNDARIOS
from Funcoes import *
from Alunos import menu_alunos
from Professores import menu_professor
from Disciplinas import menu_disciplina
from Turmas import menu_turma
# O RELATÓRIO FICOU PARA A PRÓXIMA ETAPA :( #
#from Relatorios import menu_relatorio


def menu_principal():
    print("""
   1 - Professor
   2 - Aluno
   3 - Disciplina
   4 - Turma
   

   0 - Sair
   """)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 4)


while True:
    opcao = menu_principal()
    if opcao == 0:
        break
    elif opcao == 1:
        limpa_tela()
        menu_professor()
    elif opcao == 2:
        limpa_tela()
        menu_alunos()
    elif opcao == 3:
        limpa_tela()
        menu_disciplina()
    elif opcao == 4:
        limpa_tela()
        menu_turma()
  #  elif opcao == 5:
       # limpa_tela()
        #menu_relatorio()
