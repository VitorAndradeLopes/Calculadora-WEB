#Lista 8 - Vitor Lopes

#Questão 1:
def Questao1(chave):
    dicio = {'Nome':'Fernanda Oliveira','Login':'fernanda.oliveira','CPF':14052378031,'Aniversario':'22/03','Idade':34,'Profissao':'professora','Altura':1.65,'Nacionalidade':'brasileira'}
    Valor = ''
    if chave not in dicio:
        return Valor
    else: 
        return dicio[chave]

#print(Questao1('Nome'))
#print(Questao1('nome'))
#print(Questao1('Altura'))
#print(Questao1('Aniversario'))

#Questão 2:
def Questao2(D_Jogos,NomeTime):
    L_Vitorias = []
    for chave in D_Jogos:
        if NomeTime in chave:
            if D_Jogos[chave].lower() == NomeTime.lower():
                L_Vitorias.append(chave)
            else:
                continue
    return L_Vitorias

#print(Questao2({'Warriors X Nuggets':'Warriors','Nets X Suns':'Nets','Nets X Celtics':'Nets','Knicks X Raptors':'Knicks','Pelicans X Spurs':'Spurs','Heat X Bulls':'Heat','Warriors X Wizards':'Wizards','Pelicans X Nets':'Nets','Celtics X Bulls':'Bulls','76ers X Warriors':'Warriors'},'Spurs'))
#print(Questao2({'Warriors X Nuggets':'Warriors','Nets X Suns':'Nets','Nets X Celtics':'Nets','Knicks X Raptors':'Knicks','Warriors X Wizards':'Wizards','Pelicans X Nets':'Nets','Celtics X Bulls':'Bulls','76ers X Warriors':'Warriors'},'Warriors'))
#print(Questao2({'Nets X Suns':'Nets','Nets X Celtics':'Nets','Knicks X Raptors':'Knicks','Pelicans X Spurs':'Spurs','Heat X Bulls':'Heat','Warriors X Wizards':'Wizards','Pelicans X Nets':'Nets','Celtics X Bulls':'Bulls','76ers X Warriors':'Warriors'},'Nets'))
#print(Questao2({'Knicks X Raptors':'Knicks', 'Heat X Bulls':'Heat', 'Knicks X Hawks':'Knicks', 'Knicks X Celtics':'Celtics'}, 'Knicks'))

#Questão 3:
def Questao3(L_NomeAlunos, L_NotaAlunos):
    D_AlunoNota = {}
    MudarNota = False
    Count = 0
    Nota = 0
    for Nome in L_NomeAlunos:
        for D_Nome in D_AlunoNota:
            if D_Nome == Nome:
                Nota = L_NotaAlunos[Count]
                if Nota > D_AlunoNota[Nome]:
                    MudarNota = True
        if Nome not in D_AlunoNota:
            D_AlunoNota[Nome] = L_NotaAlunos[Count]
        if MudarNota == True:
            MudarNota = False
            D_AlunoNota[Nome] = Nota
        Count += 1
    return D_AlunoNota

#print(Questao3(['Fernanda', 'Pedro', 'Joao', 'Ana', 'Alice'], [9, 8, 7, 9.5, 10]))
#print(Questao3(['Fernanda', 'Pedro', 'Fernanda', 'Joao', 'Ana', 'Alice', 'Fernanda'], [9, 8, 6, 7, 9.5, 10, 9.5]))
#print(Questao3(['Luiz', 'Fernanda', 'Luiz', 'Pedro', 'Luiz', 'Joao', 'Ana', 'Alice', 'Fernanda', 'Luiz', 'Luiz'], [7, 9, 5, 8, 8.1, 7, 9.5, 10, 10, 6, 6.9]))

#Questão 4:
import random

def SortearRifa4(Rifa):
    pos = 0
    encontrado = False
    Sorteados = ['']*3
    for i in range(len(Sorteados)):
        Sorteados[i] = random.randint(100,120)
    for i in Sorteados:
        for chave in Rifa:
            encontrado = False
            if chave == i:
                Sorteados[pos] = Rifa[chave]
                pos += 1
                encontrado = True
                break
        if encontrado == False:
            Sorteados[pos] = ''
            pos += 1
    return Sorteados

random.seed(0)
print(SortearRifa4({100:'Ana', 101:'Ana', 111:'Nina', 113:'Yuri', 104:'Renan', 112:'Antonio', 106:'Luiza', 107:'Luiz', 102:'Pedro', 109:'Alice', 120:'Gustavo'}))
print(SortearRifa4({101:'Ana', 102:'Nina', 103:'Yuri',104:'Renan', 105:'Antonio',106:'Luiza', 107:'Luiz', 108:'Pedro', 109:'Alice', 110:'Gustavo', 111:'Fernanda',112:'Andre',113:'Aline',114:'Joao', 115:'Augusto', 116:'Maria',117:'Jose',118:'Joaquim', 119: 'Jaqueline', 120: 'Cristina'}))
print(SortearRifa4({120:'Ana', 102:'Nina', 114:'Yuri', 104:'Renan', 11:'Fernanda',112:'Andre', 107:'Luiz', 108:'Pedro', 109:'Alice', 110:'Gustavo', 105:'Antonio',106:'Luiza', 113:'Aline', 103:'Joao', 115:'Augusto', 116:'Maria', 117:'Jose',118:'Joaquim', 119: 'Jaqueline', 101: 'Cristina'}))
print(SortearRifa4({101:'Ana', 3:'Nina', 4:'Nina', 105:'Antonio', 106:'Luiza', 107:'Luiz',108:'Pedro', 109:'Augusto', 110:'Gustavo', 111:'Andre', 112:'Andre',113:'Andre', 114:'Joao', 115:'Augusto', 116:'Augusto', 120:'Nina'}))
print(SortearRifa4({100:'Ana', 101:'Ana', 102:'Ana',103:'Ana', 110:'Ana',117:'Ana',104:'Ana', 120:'Ana',107:'Ana', 114:'Ana',108:'Ana',115:'Ana',109:'Ana', 116:'Ana'}))
#Questão 5:
def Questao5():
    return

#Questão 6:
def Questao6():
    return