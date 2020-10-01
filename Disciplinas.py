#CRUD das disciplina

#importa funcoes que serao usadas no codigo
from Funcoes import *

#lista vazia onde sera add os dados em memoria
disc_lista = []

#abre arquivo a ser usado
DisciplinaA = open("Disciplinas.txt", "w")


def pede_nome_disciplina():
    return (input("Nome da Disciplina: "))


def novaDisciplina():
    print("\n Cadastrar nova disciplina\n-------------------------------")
    global disc_lista
    NomeDisciplina = pede_nome_disciplina()
    CodDisciplina = pede_codigo()
    #add novos dados na lista e depois grava essas informacoes em arquivo
    disc_lista.append([NomeDisciplina, CodDisciplina])
    gravaDisciplina()
    print("Disciplina cadastrada com sucesso!")


def mostra_dados_disciplina(NomeDisciplina, CodDisciplina):
    print("Disciplina: %s Código: %s" % (NomeDisciplina, CodDisciplina))

#funcao pesquisa, usada para alterar e consultar
def pesquisaDisciplina(NomeDisciplina):
    mdnome = NomeDisciplina.lower()
    for pd, ed in enumerate(disc_lista):
        if ed[0].lower() == mdnome:
            return pd
        return None


def apagaDisciplina():
    print("\n Apagar disciplina\n-------------------------------")

    NomeDisciplina = pede_nome_disciplina()
    pd = pesquisaDisciplina(NomeDisciplina)
    if pd != None:
        #se o nome da discplina digitada existir deleta da lista e grava de novo no arquivo a lista atualizada
        del disc_lista[pd]
        gravaDisciplina()
        print("Disciplina deletada com sucesso!")
    else:
        print("Nome não encontrado.")


def alteraDisciplina():
    print("\n Alteração de disciplina\n-------------------------------")
    pd = pesquisaDisciplina(pede_nome_disciplina())
    if pd != None:
        NomeDisciplina = disc_lista[pd][0]
        CodDisciplina = disc_lista[pd][1]
        print("Encontrado:")
        mostra_dados_disciplina(NomeDisciplina, CodDisciplina)
        NomeDisciplina = pede_nome_disciplina()
        CodDisciplina = pede_codigo()
        #altera em memoria e grava no arquivo
        disc_lista[pd] = [NomeDisciplina, CodDisciplina]
        gravaDisciplina()
        print("Dados de disciplina alterados com sucesso!")
    else:
        print("Nome não encontrado.")


def gravaDisciplina():
    arquivod = open("Disciplinas.txt", "w", encoding="utf-8")
    for ed in disc_lista:
        arquivod.writelines("%s\n" % ed)
    arquivod.close()

#READ em memoria
def listaDisciplina():
    print("\n disciplinas\n-------------------------------")
    for posicaod, ed in enumerate(disc_lista):
        # imprimir posicao, sem saltar linha
        print("Posicao: %d " % posicaod, end="")
        mostra_dados_disciplina(ed[0], ed[1])
    print("------\n")

#READ EM ARQUIVO
def leDisciplina():
    print("\n Consulta de disciplina em arquivos em .txt\n-------------------------------")
    arquivod = open("Disciplinas.txt", "r", encoding="utf-8")
    disc_lista = arquivod.readlines()
    for ld in disc_lista:
        print(ld)
    arquivod.close()


def menu_opcoes_disciplina():
    print("""
   1 - Cadastrar Disciplina
   2 - Alterar
   3 - Deletar
   4 - Consultar arquivo
   5 - Lista

   0 - Voltar
   """)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 5)


def menu_disciplina():
    while True:
        opcaod = menu_opcoes_disciplina()
        if opcaod == 0:
            limpa_tela()
            break
        elif opcaod == 1:
            limpa_tela()
            novaDisciplina()
        elif opcaod == 2:
            limpa_tela()
            alteraDisciplina()
        elif opcaod == 3:
            limpa_tela()
            apagaDisciplina()
        elif opcaod == 4:
            limpa_tela()
            leDisciplina()
        elif opcaod == 5:
            limpa_tela()
            listaDisciplina()
