#Lista 9 - Vitor Lopes

#Questão 1:

def Questao1(NomeArquivo, Tema):
    Resultado = ''
    ArquivoLeitura = open(NomeArquivo, 'r')
    for linha in ArquivoLeitura:
        if Tema in linha:
            Resultado = linha
            break
    ArquivoLeitura.close()
    return Resultado

#print('='*40)
#print('Questão 1:')
#print(Questao1('2023_1_gabarito.txt','Matematica'))
#print(Questao1('2023_1_gabarito.txt','Fisica'))
#print(Questao1('2023_1_gabarito.txt','Ingles'))
#print(Questao1('2023_1_gabarito.txt','biologia'))

#Questão 2:

def Questao2(NomeArquivo):
    SubTotal = 0
    Total = 0
    ListaAux = ['']
    Count = 0
    ArquivoLeitura = open(NomeArquivo, 'r')
    for Linha in ArquivoLeitura:
        for caracter in Linha:
            if caracter != ',':
                ListaAux[Count] += caracter
            else:
                ListaAux.append('')
                Count += 1
        Peso = int(ListaAux[1])
        SubTotal = Peso * (len(ListaAux) - 2)
        Total += SubTotal
        ListaAux = ['']
        Count = 0
    ArquivoLeitura.close()
    return Total

#print('='*40)
#print('Questão 2:')
#print(Questao2('2023_1_gabarito.txt'))
#print(Questao2('2023_1_gabarito2.txt'))

#Questão 3:
def Alternativas(NomeArquivo, N_Linha):
    ListaAlternativas = []
    ListaAux = ['']
    Count = 0
    ArquivoLeitura = open(NomeArquivo, 'r')
    Linha = ArquivoLeitura.readlines()
    for caracter in Linha[N_Linha]:
        if caracter != ',' and caracter != '\n':
            ListaAux[Count] += caracter
        else:
            if caracter != '\n':
                ListaAux.append('')
                Count += 1
    Peso = int(ListaAux[1])
    for i in range(2, len(ListaAux)):
        ListaAlternativas.append(ListaAux[i])
    ArquivoLeitura.close()
    return ListaAlternativas, Peso

def Questao3(Gabarito, Respostas):
    Count = 0
    Acertos = 0
    NotaTotal = 0
    SubTotal = 0
    Questao = 0
    ArquivoLeitura = open(Gabarito, 'r')
    for Tema in ArquivoLeitura:
        ListaGabarito, Peso = Alternativas(Gabarito, Count)
        ListaRespostas, Peso = Alternativas(Respostas, Count)
        for Resposta in ListaRespostas:
            if Resposta == ListaGabarito[Questao]:
                Acertos += 1
            Questao += 1
        Questao = 0
        SubTotal = Peso * Acertos
        Acertos = 0
        NotaTotal += SubTotal
        Count += 1
    ArquivoLeitura.close()
    return NotaTotal


#print('='*40)
#print('Questão 3:')
#print(Questao3( '2023_1_gabarito.txt' , '2023_1_resposta.txt' ))
#print(Questao3( '2023_1_gabarito2.txt' , '2023_1_resposta2.txt' ))

#Questão 4:

def Questao4(Gabarito, Respostas, NovoArquivo):
    Escritor = open(NovoArquivo, 'w')
    LeitorGabarito = open(Gabarito, 'r')
    LeitorRespostas = open(Respostas, 'r')
    for Tema in LeitorGabarito:
        LinhaRespostas = LeitorRespostas.readline()
        Escritor.write(Tema)
        Escritor.write(LinhaRespostas)
    Escritor.close()
    LeitorGabarito.close()
    LeitorRespostas.close()
    return 0


#print('='*40)
#print('Questão 4:')
#print(Questao4( '2023_1_gabarito.txt' , '2023_1_resposta.txt' , '2023_1_comparacao.txt'))
#print(Questao4( '2023_1_gabarito2.txt' , '2023_1_resposta2.txt' , '2023_1_comparacao2.txt'))

#Questão 5:

#Questão 6: