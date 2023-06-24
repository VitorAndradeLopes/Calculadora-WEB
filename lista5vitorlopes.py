#Lista 5 - Vitor Lopes

#Questão 1:

def Questao1(lista, n1, n2):
    count = 0
    if(n1 == n2):
        for elemento in lista:
            if(elemento >= n1 and elemento <= n2):
                count+=1
    elif(n1 < n2):
        for elemento in lista:
            if(elemento >= n1 and elemento <= n2):
                count+=1
    elif(n1 > n2):
        for elemento in lista:
            if(elemento >= n2 and elemento <= n1):
                count+=1
    return count

print('='*40)
print('Questão 1:')
print(Questao1([-1,0,1,1.2,3,4.5,4.9,5.1,6,7,8],1,5))
print(Questao1([1,7,1.2,3,8,6,4.9,5.1,4.5],10,50))
print(Questao1([0,0,0,0,0,0,0,0],0,0))
print(Questao1([-1,0.1,-1.2,4,10,2],-2,10))


#Questão 2:

def ProdutoLista2(lista):
    Produto = 1
    for elemento in lista:
        if(type(elemento) == int or type(elemento) == float):
            Produto *= elemento
    return Produto
    
print('='*40)
print('Questão 2:')
print(ProdutoLista2([4,2,3]))
print(ProdutoLista2([4,2,3,1,2,0]))
print(ProdutoLista2([1.5,2,1j,2,3.5,'100']))
print(ProdutoLista2([True,1.1,2,1j,2.2,3.2]))


#Questão 3:

def CalcH3(n1):
    denominador = 2
    soma = 0
    if(n1 == 0):
        return 0
    else:
        for i in range(n1):
            soma += 1/denominador
            denominador+=2
    return soma
    
print('='*40)
print('Questão 3:')
print(CalcH3(0))
print(CalcH3(1))
print(CalcH3(2))
print(CalcH3(4))


#Questão 4:

def Questao4(lista1, lista2):
    lista3= []
    count = 0
    for elemento in lista1:
        if elemento > lista2[count]:
            lista3.append(elemento)
        elif elemento < lista2[count]:
            lista3.append(lista2[count])
        else:
            lista3.append(elemento)
        count +=1
    return lista3

print('='*40)
print('Questão 4:')
print(Questao4([3,6,7,7,9],[4,6,4,8,5]))
print(Questao4([8,2,5,5,7,8],[7,2,7,4,9,10]))
print(Questao4([3,3,10,3,3,3,4],[2,1,7,10,4,1,8]))


#Questão 5:

def Tabuada5(n1):
    lista = []
    for i in range(1,11):
        lista.append(n1*i)
    return lista

print('='*40)
print('Questao 5:')
print(Tabuada5(-1))
print(Tabuada5(4))
print(Tabuada5(9))
print(Tabuada5(12))


#Questão 6:

def PreçoBeneficio6(lista):
    lista2 = []
    count = 0
    pos = 0
    if(lista == []):
        return lista
    else:
        for sublista in lista:
            lista2.append(sublista[0]/sublista[1])
        melhorPreço = lista2[0]
        for elemento in lista2:
            if(elemento < melhorPreço):
               pos = count 
            count+=1
    return lista[pos]
            
print('='*40)
print('Questão 6:')
print(PreçoBeneficio6([]))
print(PreçoBeneficio6([[12,0.01]]))
print(PreçoBeneficio6([[10.5,800],[5,300.8],[2,150],[1,60]]))
print(PreçoBeneficio6([[12,800],[4,300],[3.5,150]]))
print(PreçoBeneficio6([[10,800],[5,300],[2,150],[1,60],[20,1800]]))


#Questão 7:

def DistanciaPercorrida7(lista):
    lista2 = []
    DistPercorrida = 0
    for sublista in lista:
        lista2.append(sublista[0]*sublista[1])
    for elemento in lista2:
        DistPercorrida += elemento
    return DistPercorrida

print('='*40)
print('Questão 7:')
print(DistanciaPercorrida7([[12,19],[41,73],[61,7]]))
print(DistanciaPercorrida7([[10,0],[55,12],[75,120]]))
print(DistanciaPercorrida7([[37,24],[68,69],[28,26],[79,8],[36,0],[50,71],[13,68],[87,113]]))
print(DistanciaPercorrida7([[45,46], [46,101], [7,2], [95,104], [12,107], [78,29], [10,26], [52,86], [13,79],
[1,107]]))
