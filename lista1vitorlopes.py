#Lista 1 - Vitor Lopes

#Questão 1:

def mediaGeometrica1(n1, n2, n3, n4, n5):
  return((n1*n2*n3*n4*n5)**0.2)

print('='*40)
print('Questão 1:')
print(mediaGeometrica1(10,10,10,10,10))
print(mediaGeometrica1(2,4,8,16,32))
print(mediaGeometrica1(5,4,3,2,1))



#Questão 2:

def distanciaPercorrida2(veloc, tempo):
  return veloc*tempo

print('='*40)
print('Questão 2:')
print(distanciaPercorrida2(2,10))
print(distanciaPercorrida2(9,3))
print(distanciaPercorrida2(5,5))



#Questão 3:

def funcao3(x):
  return (4*x+2)/(3*x**2+1) - (8*x**4) + ((x**2 + x/5 + 10)*2*x)**(1/2)

print('='*40)
print('Questão 3:')
print(funcao3(0))
print(funcao3(1))
print(funcao3(5))



#Questão 4:

def QtndSegundos4(horas, minutos, segundos):
  return horas*3600 + minutos*60 + segundos

print('='*40)
print('Questão 4:')
print(QtndSegundos4(0,0,20))
print(QtndSegundos4(0,50,40))
print(QtndSegundos4(1,30,10))
print(QtndSegundos4(4,0,0))



#Questão 5:

def CelsiusToFahrenheit5(Celsius):
  F = Celsius*9.0/5.0 + 32
  return F 

print('='*40)
print('Questão 5:')
print(CelsiusToFahrenheit5(30))
print(CelsiusToFahrenheit5(25))
print(CelsiusToFahrenheit5(0))



#Questão 6:

def AreaRetangulo6(Diagonal, LadoA):
    return ((Diagonal**2 - LadoA**2)**(1/2)) * LadoA

print('='*40)
print('Questão 6:')
print(AreaRetangulo6(5,4))
print(AreaRetangulo6(13,12))
print(AreaRetangulo6(10,2))



#Questão 7:

def CossenoAngulo7(x):
    return 1 - (x**2)/(2*1) + (x**4)/(4*3*2*1) - (x**6)/(6*5*4*3*2*1) + (x**8)/(8*7*6*5*4*3*2*1)

print('='*40)
print('Questão 7:')
print(CossenoAngulo7(0))
print(CossenoAngulo7(3.1416/3))
print(CossenoAngulo7(3.1416))










