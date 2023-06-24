#Lista 4 - Vitor Lopes

#Questão 1:

def Questao1(lista, num1, num2):
	count = 0
	qntd1 = 0
	qntd2 = 0
	while count < len(lista):
		if(num1  == lista[count]):
			qntd1 += 1
		if(num2 == lista[count]):
			qntd2 += 1
		count += 1
	return qntd1, qntd2

print('='*40)
print('Questão 1:')
print(Questao1([1,2,3,4,1,2,3],1,2))
print(Questao1([1,1,1,1,1,1],1,0))
print(Questao1([4,1,2,5,0,1,2,0,0,0,1,2,4,0],1,0))

#Questão 2:

def Questao2(lista, numIn, position):
	lista1 = lista[0:position]
	lista2 = lista[position:len(lista)]
	lista1.append(numIn)	
	return lista1 + lista2

print('='*40)
print('Questão 2:')
print(Questao2([1,2,3,4],-1,0))
print(Questao2([1,2,3,4],1.5,1))
print(Questao2([1,2,3,4],7,4))
print(Questao2([4,3,6,1,0,10,12,11,3,2],-2,8))


#Questão 3:

def MediaAritmeticaSimples(lista):
        count = 0
        soma = 0
        media = 0
        while count < len(lista):
                soma += lista[count]
                count += 1
        media = soma / len(lista)
        return media

def Variancia(lista):
    Variancia = 0
    Media = MediaAritmeticaSimples(lista)
    Soma = 0
    count = 0
    while count < len(lista):
        Soma += (lista[count] - Media)**2
        count += 1
    Variancia = Soma / len(lista)
    return Variancia
        


print('='*40)
print('Questão 3:')
print(Variancia([5,0,1,2]))
print(Variancia([5,1,1,-3]))
print(Variancia([1,1,1,1,1,1,1,1]))
print(Variancia([2,1,2,1,1,2,2,1,2,1]))


#Questão 4:

def Questao4(lista1, lista2):
    lista3 = []
    count1 = 0
    count2 = 0
    Elementos = 0
    while count2 < len(lista2):
        while count1 < len(lista1):
            if(lista1[count1] == lista2[count2]):
                Elementos += 1
            count1 += 1
        lista3.append(Elementos)
        count1 = 0
        Elementos = 0
        count2 +=1
    return lista3

print('='*40)
print('Questão 4:')
print(Questao4([0,0,1,0,0,2,1,3,4,0,1],[0,1,2,3,4]))
print(Questao4([7,0,1,7],[1,2,3,4,5,6,7]))
print(Questao4([1,2,3,4],[4,3,2,1]))
print(Questao4([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],[5]))
print(Questao4([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],[4,5]))


#Questão 5:

def Questao5(lista1, lista2):
    lista3 = lista2
    lista4 = []
    count1 = -1
    count2 = 0
    Bool = True
    Elementos = 0
    while count2 < len(lista2):
        while count1 < len(lista1) and Bool:
            count1 += 1
            if (lista1[count1] == lista2[count2]):
                Bool = False
        if(Bool == False):
            lista4.append(lista1[count1])
        if(len(lista2) != 1):
            lista2 = lista2[1:len(lista2)]
        Bool = True
        count1 = 0
        count2 = 0
        if(lista4 == lista3):
            return True
    return False

print('='*40)
print('Questão 5:')
print(Questao5([0,1,2],[1,2]))
print(Questao5([0,1,0,2,0,0,3,0],[1,2,3]))
print(Questao5([0,1,1,2,0,3,4,5,6],[1,2,0,5]))
print(Questao5([0,1,1,2,0],[1,3]))
print(Questao5([0,1,1,2,0],[1,3]))

#Questão 6: (A fazer)




