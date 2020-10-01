#CRUD em Turmas

#importa modulos e pacotes de funcoes, dados de professores e alunos
from Funcoes import *
import Professores
import Alunos

#lista vazia que guarda turmas em memoria
turma_lista = []
#abri arquivo ja existente para salvar turmas
TurmaA = open("Turmas.txt", "w")
#lista que sera usada para salvar alunos em uma turma
cpfaluno_lista = []

def pede_codigo_turma():
    while True:
        try:
            codt = input("Código para a turma com 5 digitos: ")
            if len(codt) == 5:
                if codt in turma_lista:
                    print("Código já cadastrado")
                else:
                    return codt
        except ValueError:
            print("Código inválido, digite novamente")


def pede_codigo_discturma():
    global disc_lista
    arquivod = open("Disciplinas.txt", "r", encoding="utf-8")
    discturma = arquivod.read()

    while True:
        try:
            coddt = input("Código da disciplina com 5 digitos: ")
            if len(coddt) == 5:
                if coddt in discturma:
                    return coddt
        except ValueError:
            print("Código inválido, digite novamente")
    arquivod.close()


def pede_CPF_prof_turma():
    while True:
        try:
            cpfp = input("CPF do professor (apenas números): ")
            
            #muda cpf digitado que estava em numero para string, para pesquisar no arquivo
            if len(cpfp) == 11:
                cpfpt = "%s.%s.%s-%s" % (cpfp[0:3], cpfp[3:6], cpfp[6:9], cpfp[9:11])
                arquivop = open("Professores.txt", "r", encoding="utf-8")
                learquivop = arquivop.read()

                if cpfpt in learquivop:
                    return cpfpt
                else:
                    return None
                arquivop.close()
        except ValueError:
            print("Número de cpf inválido, digite novamente")


def pede_CPF_aluno_turma():
    #abre e le arquivo de turmas e alunos
    turmarqr = open("Turmas.txt", "r", encoding="utf-8")
    lerarquivotr = turmarqr.read()

    alunosarq = open("Alunos.txt", "r", encoding="utf-8")
    lerarquivoa = alunosarq.read()

    turma = input("Digite o código da turma: ")

    if turma in lerarquivotr:#se ja existir a turma pede cpf do aluno
        cpf = input("Digite o CPF do aluno: ")

        if len(cpf) == 11:#valida o cpf
            cpfat = "%s.%s.%s-%s" % (cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])

            if cpfat in lerarquivoa:#se o cpf estiver no arquivo de alunos
                if cpfat not in lerarquivotr:# e ainda nao esta cadastrado na turma
                    print("Aluno cadastrado na turma %s com sucesso!" % turma)
                    return cpfaluno_lista.append(cpfat)#retorna e add na lista, depois é gravada a informacao em arquivo
        else:
            return None
    else:
        print("aluno não cadastrado!")

def novaTurma():
    print("\nCadastrar Nova Turma\n-----------")
    CodTurma = pede_codigo_turma()
    Periodo = pede_periodo()
    CodDiscTurma = pede_codigo_discturma()
    ProfessorTurma = pede_CPF_prof_turma()

    turma_lista.append([CodTurma, Periodo, CodDiscTurma, ProfessorTurma, cpfaluno_lista])
    print("Turma cadastrada com sucesso!")
    gravaTurma()


def mostra_dados_turma(CodTurma, Periodo, CodDiscTurma, ProfessorTurma, AlunosTurma):
    print("Código da Turma: %s Período: %s \n Código da disciplina: %s \n Professor: %s \n Alunos: %s"
          % (CodTurma, Periodo, CodDiscTurma, ProfessorTurma, AlunosTurma))


def pesquisaTurma(CodTurma):
    ptCodTurma = CodTurma
    for pt, et in enumerate(turma_lista):
        if et[0] == ptCodTurma:
            return pt
        return None

def apagaTurma():
    print("\nApaga Turma\n-----------")
    CodTurma = pede_codigo_turma()
    pt = pesquisaTurma(CodTurma)
    if pt != None:
        del turma_lista[pt]
        print("Turma deletada com sucesso!!")
        gravaTurma()
    else:
        print("Turma nao encontrada.")


def alteraTurma():
    print("\nAltera Turma\n-----------")
    pat = pesquisaTurma(pede_codigo_turma())
    if pat != None:
        CodTurma = turma_lista[pat][0]
        Periodo = turma_lista[pat][1]
        CodDiscTurma = turma_lista[pat][2]
        ProfessorTurma = turma_lista[pat][3]

        print("Encontrado:")
        mostra_dados_turma(CodTurma, Periodo, CodDiscTurma, ProfessorTurma, cpfaluno_lista)

        CodTurma = pede_codigo_turma()
        Periodo = pede_periodo()
        CodDiscTurma = pede_codigo_discturma()
        ProfessorTurma = pede_CPF_prof_turma()

        turma_lista[pat] = [CodTurma, Periodo, CodDiscTurma, ProfessorTurma, cpfaluno_lista]
        gravaTurma()
        print("Dados da turma alterados com sucesso!")
    else:
        print("Turma nao encontrada.")


def gravaTurma():
    arquivot = open("Turmas.txt", "w", encoding="utf-8")

    for gt in turma_lista:
        arquivot.writelines("Código da turma: %s\nPeríodo: %s\nCódigo da disciplina: %s\nCPF do professor: %s\nAlunos: %s\n\n" %(gt[0], gt[1], gt[2], gt[3], gt[4]))
    arquivot.close()


def add_aluno_turma():
    print("\nAdiciona Aluno a Turma\n-----------")
    pede_CPF_aluno_turma()
    gravaTurma()

#READ em memoria
def listaTurma():
    print("\nTurmas\n-----------")
    for posicaot, gt in enumerate(turma_lista):
        print("Posicao: %d " % posicaot, end="")
        mostra_dados_turma(gt[0], gt[1], gt[2], gt[3], gt[4])
    print("-----------\n")
#READ em arquivo
def leTurma():
    print("\nConsulta de turma em arquivo.txt\n-----------")
    arquivot = open("Turmas.txt", "r", encoding="utf-8")
    turma_lista = arquivot.readlines()
    for lt in turma_lista:
        print(lt)
    arquivot.close()


def menu_opcoes_turma():
    print("""
  1 - Cadastrar Turma
  2 - Alterar
  3 - Deletar
  4 - Consultar arquivo
  5 - Lista
  6 - Add aluno em turma

  0 - Voltar
  """)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)


def menu_turma():
    while True:
        opcaot = menu_opcoes_turma()
        if opcaot == 0:
            limpa_tela()
            break
        elif opcaot == 1:
            limpa_tela()
            novaTurma()
        elif opcaot == 2:
            limpa_tela()
            alteraTurma()
        elif opcaot == 3:
            limpa_tela()
            apagaTurma()
        elif opcaot == 4:
            limpa_tela()
            leTurma()
        elif opcaot == 5:
            limpa_tela()
            listaTurma()
        elif opcaot == 6:
            limpa_tela()
            add_aluno_turma()
