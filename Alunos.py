#CRUD ALUNOS

#Modulos e pacotes que serao usados no crud
from Funcoes import *
import Turmas

#lista que vai armazenar os dados na memoria
aluno_lista = []
AlunoA = open("Alunos.txt", "w")


def novoAluno():
    print("\nCadastro de alunos\n-------------------------------")
    global aluno_lista
    NomeAluno = pede_nome()
    CPFAluno = pede_CPF()
    aluno_lista.append([NomeAluno, CPFAluno])
    gravaAluno()
    print("Aluno cadastrado com sucesso!")


def mostra_dados_alunos(NomeAluno, CPFAluno):
    print("Nome: %s CPF: %s" % (NomeAluno, CPFAluno))


def pesquisaAluno(NomeAluno):
    manome = NomeAluno.lower()
    for pa, ea in enumerate(aluno_lista):
        if ea[0].lower() == manome:
            return pa
        return None


def apagaAluno():
    print("\nApagar aluno\n-------------------------------")
    NomeAluno = pede_nome()
    pa = pesquisaAluno(NomeAluno)
    if pa != None:
        del aluno_lista[pa]
        gravaAluno()
        print("Aluno deletado com sucesso!")
    else:
        print("Nome não encontrado.")


def alteraAluno():
    print("\nAltera aluno\n-------------------------------")
    pa = pesquisaAluno(pede_nome())
    if pa != None:
        NomeAluno = aluno_lista[pa][0]
        CPFAluno = aluno_lista[pa][1]
        print("Encontrado:")
        mostra_dados_alunos(NomeAluno, CPFAluno)
        NomeAluno = pede_nome()
        CPFAluno = pede_CPF()
        aluno_lista[pa] = [NomeAluno, CPFAluno]
        gravaAluno()
        print("Dados de aluno alterados com sucesso!")
    else:
        print("Nome não encontrado.")


def gravaAluno():
    arquivoa = open("Alunos.txt", "w", encoding="utf-8")
    for ea in aluno_lista:
        arquivoa.writelines("%s\n" % ea)
    arquivoa.close()


def listaAluno():
    print("\nLista de Alunos\n-------------------------------")
    for posicaoa, ea in enumerate(aluno_lista):
        # imprimir posicao, sem saltar linha
        print("Posicao: %d " % posicaoa, end="")
        mostra_dados_alunos(ea[0], ea[1])
    print("------\n")


def leAluno():
    print("\nConsulta aluno em arquivo .txt\n-------------------------------")
    arquivoa = open("Alunos.txt", "r", encoding="utf-8")
    aluno_lista = arquivoa.readlines()
    for la in aluno_lista:
        print(la)
    arquivoa.close()


def menu_opcoes_alunos():
    print("""
   1 - Cadastrar Aluno
   2 - Alterar
   3 - Deletar
   4 - Consultar arquivo
   5 - Lista

   0 - Voltar
   """)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 5)


def menu_alunos():
    while True:
        opcaoa = menu_opcoes_alunos()
        if opcaoa == 0:
            limpa_tela()
            break
        elif opcaoa == 1:
            limpa_tela()
            novoAluno()
        elif opcaoa == 2:
            limpa_tela()
            alteraAluno()
        elif opcaoa == 3:
            limpa_tela()
            apagaAluno()
        elif opcaoa == 4:
            limpa_tela()
            leAluno()
        elif opcaoa == 5:
            limpa_tela()
            listaAluno()
