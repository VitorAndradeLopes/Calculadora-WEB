#Lista 3 - Vitor Lopes

#Questão 1:

def Divisores1(n1):
	count = 1
	Divisores = 0
	while(count <= n1):
		if(n1%count == 0):
			Divisores +=1
		count +=1
	return Divisores

print('='*40)
print('Questão 1:')
print(Divisores1(13))
print(Divisores1(6))
print(Divisores1(20))

#Questão 2:

def LogNeperiano2(x, k):
    count = 1
    denominador = 1
    resultado = 1
    while count <= k:
        denominador *= 2
        resultado = resultado * (2/(1+x**(1/denominador)))
        count +=1
    return resultado * (x-1)

print('='*40)
print('Questão 2:')
print (LogNeperiano2(2,50))
print (LogNeperiano2(2,8))
print (LogNeperiano2(2.71828, 100))
print (LogNeperiano2(10,40))

#Questão 3:

#a)

def OrdemCresc3a(n1,n2):
    if n1>n2:
        return n2,n1
    else:
        return n1,n2

#b)

def SomaMultCinco3b(n1,n2):
    menor, maior = OrdemCresc3a(n1,n2)
    soma = 0
    while menor <= maior:
        if(menor%5 == 0):
            soma = soma + menor
        menor += 1
    return soma

print('='*40)
print('Questão 3:')
print(SomaMultCinco3b(10,100))
print(SomaMultCinco3b(100,1000))
print(SomaMultCinco3b(10,10))
print(SomaMultCinco3b(7,7))


#Questão 4:

def NewthonRaphson4(a,b,c,erro,xi):
    stop = False
    xii = xi - (a*xi**2 + b*xi + c)/(2*a*xi + b)
    while stop != True:
        if(xii - xi > 0):
            Vabs = xii - xi
            xi = xii
        else:
            Vabs = xi - xii
            xi = xii
        if Vabs > erro:
            xii = xi - (a*xi**2 + b*xi + c)/(2*a*xi + b)
        else:
            stop = True
    return xii

print('='*40)
print('Questão 4:')
print(NewthonRaphson4(2,1,0,0.001,0.1))
print(NewthonRaphson4(2,1,0,0.001,-1.1))
print(NewthonRaphson4(1,-5,-10,0.1,5))
print(NewthonRaphson4(1,-5,-10,0.1,-4))
print(NewthonRaphson4(-1,2,4,0.0005,2))
print(NewthonRaphson4(-1,2,4,0.0005,5))

#Questão 5:

#a)

def SomaDigitos5a(n1):
    soma = 0
    resto = 0
    while n1 > 0:
        resto = n1%10
        n1 = n1 // 10
        soma = soma + resto
    return soma

#b)

def somaDigIgualAlvo5b(inicio, fim, alvo):
    stop = False
    teste = 0
    while fim != inicio and stop != True:
        if SomaDigitos5a(fim) == alvo:
            stop = True
        else:
            fim -= 1
    if fim == inicio:
        return -1
    else:
        return fim

print('='*40)
print('Questão 5:')
print(somaDigIgualAlvo5b(0,49,5))
print(somaDigIgualAlvo5b(150,190,12))
print(somaDigIgualAlvo5b(150,190,10))
print(somaDigIgualAlvo5b(10,15,8))
