#Lista 2 - Vitor Lopes

#Questão 1:

def RaizQuadrada1(n1):
    if(n1<0):
        n1 *= -1
    return n1**(1/2)

print('='*40)
print('Questão 1:')
print(RaizQuadrada1(16))
print(RaizQuadrada1(0))
print(RaizQuadrada1(-16))

#Questão 2:

def TestarTipo2(n1,n2):
    tipo1 = type(n1)
    tipo2 = type(n2)
    if(tipo1 ==  int and tipo2 == int):
        return 1
    elif(tipo1 == float and tipo2 == float):
        return 2
    else:
        return 3

print('='*40)
print('Questão 2:')
print(TestarTipo2(1,2))
print(TestarTipo2(1.0,-4.4))
print(TestarTipo2(True,0))
print(TestarTipo2(1j,2.2))
print(TestarTipo2('1',2))

#Questão 3:

def ProcessoSeletivo3(n1,n2,n3,n4,n5,n6):
    
    Count = n1+n2+n3+n4+n5+n6
    Grupo1 = 5
    Grupo2 = 3
    Grupo3 = 1

    if(Count >= Grupo1):
        return 1
    elif(Count >= Grupo2 and Count < Grupo1):
        return 2
    elif(Count >= Grupo3 and Count < Grupo2):
        return 3
    else:
        return 0

print('='*40)
print('Questão 3:')
print(ProcessoSeletivo3(1,1,1,1,1,1))
print(ProcessoSeletivo3(1,0,1,1,0,0))
print(ProcessoSeletivo3(1,0,1,0,0,0))
print(ProcessoSeletivo3(0,0,0,0,0,0))


#Questão 4:

def Prioridade4(idade, gravidez, VIP, fileira):
    if (idade <= 3 or idade >= 65 or gravidez == True or (VIP == True and fileira < 10)): 
        return True
    else:
        return False

print('='*40)
print('Questão 4:')
print(Prioridade4(2, False, False, 15))
print(Prioridade4(70, False, False, 14))
print(Prioridade4(30, True, False, 4))
print(Prioridade4(30, False, True, 2))
print(Prioridade4(30, False, True, 10))
print(Prioridade4(30, False, False, 2))


#Questão 5:

def IdadeCamila5(n1,n2,n3):
    if(n1>n2):
        if(n1<n3):
            return n1
    elif(n1>n3):
        if(n1<n2):
            return n1
    elif(n2>n1):
        if(n2<n3):
            return n2
    elif(n2>n3):
        if(n2<n1):
            return n2
    if(n3>n2):
        if(n3<n1):
            return n3
    elif(n3>n1):
        if(n3<n2):
            return n3


print('='*40)
print('Questão 5:')
print(IdadeCamila5(14,15,16))
print(IdadeCamila5(20,15,16))
print(IdadeCamila5(13,12,18))
print(IdadeCamila5(13,15,11))
print(IdadeCamila5(19,21,20))
print(IdadeCamila5(22,18,20))



#Questão 6: 

def CustoViagem6(distancia, tempo, horario):
    Custo = 0
    if ((type(distancia) == int or type(distancia) == float) and type(tempo) == int and type(horario) == int):
        if((distancia > 0 and distancia <200) and (tempo >0 and tempo<480) and (horario >=0 and horario <=23)):
            if(distancia<5 and tempo <20):
                Custo = distancia*8
            elif(distancia<5 and tempo >=20):
                Custo = distancia*8 + (tempo*0.1)
            elif((distancia>=5 and distancia <10) and tempo <40):
                Custo = distancia*9
            elif((distancia>=5 and distancia <10) and tempo >=40):
                Custo = distancia*9 + (tempo*0.15)
            elif(distancia>=10 and tempo<80):
                Custo = distancia*10
            elif(distancia>=10 and tempo>=80):
                Custo = distancia*10 + (tempo*0.2)
            if(horario <=5 or horario >=22):
                Custo = Custo*1.2
            return Custo

        else:
            return -2
    else:
        return -1

print('='*40)
print('Questão 6:')
print(CustoViagem6(4.9,19,8))
print(CustoViagem6(4,20,21))
print(CustoViagem6(4.9,19,3))
print(CustoViagem6(5.5,39,10))
print(CustoViagem6(5,40,22))
print(CustoViagem6(12.5,70,10))
print(CustoViagem6(12.5,70,0))
print(CustoViagem6(30.2,85,0))
print(CustoViagem6('a',19,8))
print(CustoViagem6(4.5,19.1,8))
print(CustoViagem6(-4.1,19,True))
print(CustoViagem6(-4.1,19,8))
print(CustoViagem6(4.1,0,8))



#Questão 7:

def CustoIngresso7(n1,n2,n3):
    Custo = 0
    if(n1>=60):
        Custo += 15
    else:
        if(n1>=18 and n1<60):
            Custo += 40
        else:
            if(n1>= 7 and n1<18):
                Custo += 20
            else:
                Custo += 5
    if(n2>=60):
        Custo += 15
    else:
        if(n2>=18 and n2<60):
            Custo += 40
        else:
            if(n2>= 7 and n2<18):
                Custo += 20
            else:
                Custo += 5
    if(n3>=60):
        Custo += 15
    else:
        if(n3>=18 and n3<60):
            Custo += 40
        else:
            if(n3>= 7 and n3<18):
                Custo += 20
            else:
                Custo += 5
    return Custo

print('='*40)
print('Questão 7:')
print(CustoIngresso7(6,8,18))
print(CustoIngresso7(60,8,18))
print(CustoIngresso7(60,5,18))
print(CustoIngresso7(5,5,6))
print(CustoIngresso7(17,19,6))
