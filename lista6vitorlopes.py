#Lista 6 - Vitor Lopes

#Questão 1:

def Questao1(lista):
    tupla = ()
    tupla2 = ([])
    for ElementoLista in lista:
        tupla2 += (ElementoLista, )
        for ElementoTupla2 in tupla2:
            if(ElementoLista in tupla):
                tupla = tupla
            else:
                tupla += (ElementoLista, )
    return tupla

print('='*40)
print('Questão 1:')
print(Questao1([1,2,3,4,5,6,7,8]))
print(Questao1([0,0,0,0,0,0,0,0]))
print(Questao1(['Harry Potter','Percy Jackson','A Arma Escarlate','Percy Jackson']))


#Questão 2:

def Compras2(t_ListaCompras, t_EstoqueMercado):
    Total = 0
    Subtotal = 0
    NotaFiscal = ()
    NomeItem = ''
    QntdItem = 0
    for item in t_ListaCompras:
        NomeItem = item[0].lower()
        QntdItem = item[1]
        for produto in t_EstoqueMercado:
            NomeProduto = produto[0].lower()
            PreçoProduto = produto[1]
            Subtotal = 0
            if(NomeItem == NomeProduto):
                Subtotal += PreçoProduto*QntdItem
                NotaFiscal += ((NomeProduto.upper(), Subtotal,),)
                Total += Subtotal
    return Total, NotaFiscal

print('='*40)
print('Questão 2:')
print(Compras2( (('Arroz',2),), (('Arroz',5),) ))
print(Compras2( ( ('Arroz', 2), ('Feijao', 1), ('tomaTe', 4) ), ( ('tomate', 2.5), ('feijao', 7.4), ('ARROZ', 5.1)) ))
print(Compras2( ( ('biscoito', 2), ('BATATA FRITA', 10), ('queijo', 5), ('presunto',8), ('Salame', 3), ('Mortadela Defumada', 5) ), ( ('Pao de queijo', 3), ('BiScoitO', 3.8), ('Batata Frita', 11.4), ('mortadela DEFUMADA', 0.9), ('SALAME', 2.3), ('pao', 1.5), ('Presunto', 1.2) ) ))


#Questão 3:

def RetirarTrecho3(Trecho, Frase):
    Intervalo = 0
    for caracter in Frase:
        if(Trecho in Frase[Intervalo:len(Trecho)+Intervalo]):
            Frase = Frase[0:Intervalo] + Frase[Intervalo+len(Trecho):len(Frase)]
        else:
            Intervalo += len(Trecho)
            
    return Frase

print('='*40)    
print('Questão 3:')
print(RetirarTrecho3(' ','Ola, turma de Engenharia Eletronica!'))
print(RetirarTrecho3('E','Ola, turma de Engenharia Eletronica!'))
print(RetirarTrecho3('e','Ola, turma de Engenharia Eletronica!'))


#Questão 4: (Inacabado)

def TestarIntervalo(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if((num1>=0 and num1<=9) and (num2>=0 and num2<=9)):
        return True
    return False

def CaçaAoTesouro4():
    
    #Variáveis:
    Histórico = ()
    LinhaUsuário = 0
    ColunaUsuário = 0
    ErroIntervalo = 'Os valores devem ser maiores ou iguais a 0 e menores ou iguais a 9.'
    
    #Tela
    print('Vamos começar o jogo!')
    print('O primeiro usuário deve digitar onde quer esconder o tesouro.')
    print('Digite valores maiores ou iguais a 0 e menores ou iguais a 9.')
    print('Nesse momento, o segundo usuário não deve olhar para a tela do computador.')
    LinhaTesouro = input('Digite a linha:')
    ColunaTesouro = input('Digite a coluna:')
    while TestarIntervalo(LinhaTesouro, ColunaTesouro) != True:
        print(ErroIntervalo)
        LinhaTesouro = input('Digite a linha:')
        ColunaTesouro = input('Digite a coluna:')
    return Histórico
    
print(CaçaAoTesouro4())

#Inacabado








