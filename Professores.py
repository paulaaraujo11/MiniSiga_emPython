#CRUD PROFESSORES

#metodos e pacotes usados no crud
from Funcoes import *
import Turmas

#lista vazia que armazena os dados em memoria
prof_lista = []
ProfessorA = open("Professores.txt", "w")


def pede_departamento():
    return (input("Departamento: "))


def novoProfessor():
    print("\nCadastro Professor\n------")
    global prof_lista
    NomeProfessor = pede_nome()
    CPFProfessor = pede_CPF()
    Departamento = pede_departamento()
    #add dados em lista prof_lista
    prof_lista.append([NomeProfessor, CPFProfessor, Departamento])
    gravaProfessor()
    print("Professor cadastrado com sucesso!")


def mostra_dados_professores(NomeProfessor, CPFProfessor, Departamento):
    print("Nome: %s CPF: %s Departamento: %s" % (NomeProfessor, CPFProfessor, Departamento))


def pesquisaProfessor(NomeProfessor):
    mpnome = NomeProfessor.lower()
    for pp, ep in enumerate(prof_lista):
        if ep[0].lower() == mpnome:
            return pp
        return None


def apagaProfessor():
    #pede o nome do prof pesquisa e deleta da lista e grava a lista novamente no arquivo
    print("\nApaga Professor\n------")
    NomeProfessor = pede_nome()
    pp = pesquisaProfessor(NomeProfessor)
    if pp != None:
        del prof_lista[pp]
        gravaProfessor()
        print("Professor deletado com sucesso!")
    else:
        print("Nome não encontrado.")


def alteraProfessor():
    
    print("\Altera Professor\n------")
    pp = pesquisaProfessor(pede_nome())
    if pp != None:
        NomeProfessor = prof_lista[pp][0]
        CPFProfessor = prof_lista[pp][1]
        Departamento = prof_lista[pp][2]
        print("Encontrado:")
        mostra_dados_professores(NomeProfessor, CPFProfessor, Departamento)
        NomeProfessor = pede_nome()
        CPFProfessor = pede_CPF()
        Departamento = pede_departamento()
        #altera e ja salva em arquivo atraves da funcao gravaProfessor()
        prof_lista[pp] = [NomeProfessor, CPFProfessor, Departamento]
        gravaProfessor()
        print("Dados de professor alterados com sucesso!")
    else:
        print("Nome não encontrado.")


def gravaProfessor():
    arquivop = open("Professores.txt", "w", encoding="utf-8")
    for ep in prof_lista:
        arquivop.writelines("%s\n" % ep)
    arquivop.close()


#faz o READ na memoria
def listaProfessor():
    print("\nProfessores\n------")
    for posicaop, ep in enumerate(prof_lista):
        # imprimir posicao, sem saltar linha
        print("Posicao: %d " % posicaop, end="")
        mostra_dados_professores(ep[0], ep[1], ep[2])
    print("------\n")

#faz o READ no arquivo
def le_arquivo_Professor():
    print("\nConsulta Professores em arquivo.txt\n------")
    arquivop = open("Professores.txt", "r", encoding="utf-8")
    prof_lista = arquivop.readlines()
    for lp in prof_lista:
        print(lp)
    arquivop.close()


def menu_opcoes_professor():
    print("""
   1 - Cadastrar Professor
   2 - Alterar
   3 - Deletar
   4 - Consultar arquivo
   5 - Lista

   0 - Voltar
   """)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 5)


def menu_professor():
    while True:
        opcaop = menu_opcoes_professor()
        if opcaop == 0:
            limpa_tela()
            break
        elif opcaop == 1:
            limpa_tela()
            novoProfessor()
        elif opcaop == 2:
            limpa_tela()
            alteraProfessor()
        elif opcaop == 3:
            limpa_tela()
            apagaProfessor()
        elif opcaop == 4:
            limpa_tela()
            le_arquivo_Professor()
        elif opcaop == 5:
            limpa_tela()
            listaProfessor()
