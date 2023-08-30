#mi primer main en phyton xd
#ejercicio 1
#print ("hola mundo")

#ejercicio 2
#mensaje = "hola mundooo"
#print (mensaje)

#ejercicio 3
#NOMBRE = input("ingresa tu nombre ")
#print ("hola " + NOMBRE + " MUCHO GUSTO")

#Numero = int(input("hola " + NOMBRE + " ingresa tu edad"))
#if Numero >= 18:
  #print("felicidades eres mayor de edad")
#if Numero < 18:
  #print("bro sos joven")
#if Numero < 1:
  #print ("no has nacido no seas pendejo")
#if Numero > 110:
  #print ("milagro que sigues vivo")

#ejercicio 4
#ejercicio = ((3+2)/(2*5)) ** 2
#print (ejercicio)

#ejercicio 5
#Horas = float(input("numero de horas diarias "))
#Costo = float(input("ahora cuanto te pagan por hora? "))
#operacion = str(Horas * Costo)
#print ("tu pago total en el día es " + operacion + " pesos")
''''''
''''print ("dame un entero positivo")
N = int(input())
print ("EL RESULTADO ES" + str(N*(N+1)//2) )'''
'''
#N = int(input("dame un entero"))
#suma = str(N*(N+1)//2)
#print ("el resultado es" + suma)
''''''
#ejercicio 7
print("cuanto pesas?")
peso = (input())
print("cuanto mides")
estatura =(input())
imc = round(float(peso)/float(estatura)**2,2)
print ("tu imc es" , imc)'''
''''''
#ejercicio 8
''''print("dame un numero entero")
n=int(input())
print("dame otro bro")
m=int(input())
print("el cociente es")
cociente = (n/m)
print(cociente)
print ("el residuo es")
residuo = (n%m)
print (residuo)'''

''''''
#ejercicio 
'''print("dime una cantidad a invertir")
c=float(input())
print("ahora el interes")
i=float(input())
print("a cuantos años quieres")
a=float(input())
inversion= c*(i/100+1)**a
print("el capital obtenido es ")
print(inversion)'''


'''print("cantidad muñecas")
mñ=int(input())
print("payaso")
py=int(input())
peso_muñecas = str(75 * mñ)
peso_payasos = str (112*py)
pt = peso_muñecas + peso_payasos 
print("el peso total de la caja es" + pt + " kg")'''

'''print ("dame un numero")
v1= int(input())
print ("dame otro")
V2= int(input())
if v1 < V2:
 print("la suma es" + str(v1+V2) )
elif v1> V2:
  print ("la suma es" + str(v1-V2))
else:
  print(str(v1*V2))'''

#ejercicio 1
'''print ("dame un entero positivo")
ent= int(input())
hola = (ent*(ent+1)//2)
print ("el resultado es "+str(hola))
if hola > 20:
  print("el numero es grande bro")
else:
  print("ta chiquito mi pana") '''

#ejercicio 2
'''print ("dame un numero entero")
n= int(input())
print ("dame otro")
m= int(input())
print("el cociente es")
c = (n//m)
print(c)
print ("el residuo es")
r = (n%m)
print (r)
if c<1:
  print("el divisor es mayor que el dividendo")
elif c>1:
  print("el divisor es menor que el dividendo")
else:
  print("el divisor y el dividendo son iguales")'''



#ejercicio 3.2
'''print("dime una cantidad a invertir")
c=float(input())
print("ahora el interes")
i=float(input())
print("a cuantos años quieres")
a=float(input())
inversion= c*(i/100+1)**a
print("el capital obtenido es ")
print(inversion)
if inversion < 100000:
  print("baja rentabilidad")
elif inversion >100000 and inversion <1000000: 
  print("inversion moderada")
else:
  print ("es una buena inversion")'''

#ejercicio 4.2
'''print("cantidad muñecas")
mñ=int(input())
print("payaso")
py=int(input())
peso_muñecas = int (75 * mñ)
peso_payasos = int (112*py)
pt = peso_muñecas + peso_payasos 
print("el peso total de la caja es" + str(pt) + " kg")
r1 = "si"
r2 = "no"
if pt > 3000:
  print("quieres enviarlo?")
  r3= input()
  if r3 == r1:
    print ("contenedor enviado")
  else:
    print ("no se envia")'''

# ejercicio 555
'''n1= int(input())
n2= int(input())
def suma(n1, n2):
  return n1+n2
print (suma(n1,n2))'''

#ejercicio 556
'''n1 = int(input())
n2 = int(input())
def suma(n1,n2):
  s = n1 + n2
  return s
sum = suma(n1,n2)
print("la suma es"+ str(sum))'''

#ejercicio sdafgvdgersdfcsrewt
'''n1 = int(input())
n2 = int(input())
def resta(n1,n2):
  r = n1 - n2
  return r
dif = resta(n1,n2)
print("la resta es"+ str(dif))'''
#EJERCICIO FGDDREWDFEF
'''n1 = int(input())
n2 = int(input())
def resta(n1,n2):
  r = n1 - n2
  return r
dif = resta(n1,n2)
print("la resta es"+ str(dif))'''

#DFZGGHTYYHU
'''n1 = int(input())
n2 = int(input())
def multi(n1,n2):
  p = n1 * n2
  return p
PRO = multi(n1,n2)
print("die produkt ist"+ str(PRO))'''


'''n1 = int(input())
n2 = int(input())
def divi(n1,n2):
  d = n1 / n2
 if n2 == 0: 
  print ("no se hace mi pana")
  return d
def coc(n1,n2):
  c= n1%n2
  return c
div = divi(n1,n2)
xd = coc(n1,n2)
print("die ergebnis ist"+ str(div)+ "y el residuo es"+ str(xd))'''

#calculator
'''print ("bienvenido a la calculadora")
print ("ingrese el valor de A")
A= int(input())
print ("ingrese el valor de B")
B = int(input())
print ("seleccione la operación a realizar")
print ("""
1: suma
2: resta
3: multiplicación
4: división
""")
opción = int(input())
if opción == 1:
  def suma(A,B):
    s = A + B
    return s
  sum = suma(A,B)
  print("la suma es"+ str(sum))
elif opción == 2:
  def resta(A,B):
    r = A - B
    return r
  dif = resta(A,B)
  print("la resta es"+ str(dif))
elif opción == 3:
  def multi(A,B):
    p = A * B
    return p
  PRO = multi(A,B)
  print("El prodcucto es"+ str(PRO))
elif opción == 4: 
  def divi(A,B):
    d = A/ B
    return d
  def coc(A,B):
      c= A%B
      return c
  div = divi(A,B)
  xd = coc(A,B)
  print("EL cociente es"+ str(div)+ "y el residuo es"+ str(xd))
else:
  print("incorrecto")'''


#ejercicio cta de ahorros

'''print("Bienvenido a tu cuenta de ahorros")
print("inserte la cantidad depositada")
cantidad = int(input())
if cantidad > 0 and cantidad < 1000000:
  print ("la cantidad de ahorros es")
  print (cantidad *(1+2/100))
elif cantidad >= 1000000 and cantidad < 2000000:
      print ("la cantidad de ahorros es")
      print (cantidad *(1+5/100))
elif cantidad > 2000000:
     print ("la cantidad de ahorros es")
     print (cantidad *(1+7/100))
else:
  print ("error")'''


#Cte
'''def intereses(inv):
  d = inv

  if (d > 0 and d >1000000):
    return 2
  elif (d >= 1000000 and d < 2000000):
    return 5
  else: 
    return 7

def calbalance (int, inv):
  n= int
  d= inv 

  return round((d*(1+(n/100))),2)

def ctaAhorros():
  #inversion, interes, b1, b2, b3 = 0,0 
  inversion = float(input("ingrese el valor de la inversion:"))
  interes = intereses(inversion)
  b1 = calbalance(interes,inversion)
  b2 = calbalance(interes,b1)
  b3 = calbalance(interes,b2)
  print ("balance año 1:" + str(b1) + "balance año 2" + str(b2) + "balance año 3:" + str(b3))

ctaAhorros()'''

'''print ("que figura quieres")
print ("""
1: Circulo
2: Cuadrado
3: triangulo
""")
opción = int(input())
if opción == 1:
  print("ingrese el radio")
  r = float(input())
  r1= 3.14*(r**2)
    
  print("el area del circulo es" + str(r1))
elif opción == 2:
  print ("dame la base y la altura")
  A= float (input())
  B= float (input())
  def multi(A,B):
    P = A * B
    return P
  pro = multi(A,B)
  print("el area del cuadrado es "+ str(pro))
elif opción == 3:
   print ("dame la base y la altura")
   A= float (input())
   B= float (input())
   tri = (A * B)/2
   print("El area del triangulo es "+ str(tri))
else:
  print("incorrecto")'''

'''def areatriangulo(b,a):
  return (b*a)/2
def areacuadrado(bc,ad):
  return (bc*ad)
def areacirculo(r):
  return (3.14159*(r**2))
def arearombo(D,d):
  return (D*d)/2
def areapenta(P,A):
  return (P*A)/2
def areafig():
  area=0.0
  figura= ""
  figura = input("escriba la figura que desea calcular el area: ")

  if ((figura.lower())=="triangulo"):
    base=0.0
    altura = 0.0
    base= float(input("ingresad la base"))
    altura = float(input("ingrese la altura"))
    area= areatriangulo(base,altura)
    print("la base es:", area)
  elif ((figura.lower())=="cuadrado"):
    base=0.0
    altura = 0.0
    base= float(input("ingresad la base"))
    altura = float(input("ingrese la altura"))
    area= areacuadrado(base,altura)
    print("la base es:", area)
  elif ((figura.lower())=="circulo"):
    radio=0.0
    radio= float(input("ingresad el radio"))
    area= areacirculo(radio)
    print("la base es:", area)
  elif ((figura.lower())=="rombo"):
    Diagonal_mayor=0.0
    Diagonal_menor=0.0
    Diagonal_mayor= float(input("ingresa la diagonal mayor"))
    Diagonal_menor= float(input("INGRESE LA DIAGONAL MENOR"))
    area= arearombo(Diagonal_mayor, Diagonal_menor)
    print("la base es:", area)
  elif ((figura.lower())=="pentagono"):
    Perimetro=0.0
    Apotema=0.0
    Perimetro= float(input("ingresa el perimetro"))
    Apotema= float(input("INGRESE LA apotema"))
    area= areapenta(Perimetro, Apotema)
    print("la base es:", area)
  else: 
    print("error")
areafig()'''
'''
def maximo (a,b):
  if x>y:
    return a
  if x<y:
    return b
def minimo (a,b):
  if x>y:
    return a
  if x<y:
    return b
x=int(input("dame un numero:"))
y=int(input("dame otro:"))
print(maximo(x-3, minimo(x+2,y-5)))'''

''''nombre = ("hola")
print (nombre)'''



def calcestereo(val,desc):
  return (val*(1+(desc/100)))
def valestereo():
  iva = 20
  VALORAI= 0.0
  VALORDI=0.0
  COSTO=0.0
  MARCA=""
  COSTO=float(input("dame el costo del producto"))
  MARCA= input("dame la marca del estereo: ")

  if COSTO >= 2000000 and MARCA.upper== "NOSY":
    VALORAI=calcestereo(COSTO,15)
    VALORDI=calcestereo(VALORAI,iva)
    print("el valor del estereo es "+ str(VALORDI))
  elif COSTO >= 2000000 and MARCA.upper != "NOSY":
    VALORAI=calcestereo(COSTO,10)
    VALORDI=calcestereo(VALORAI,iva)
    print("el valor ahora es"+ str(VALORDI))
  elif COSTO < 2000000 and MARCA.upper == "NOSY":
    VALORAI=calcestereo(COSTO,5)
    VALORDI=calcestereo(VALORAI,iva)
    print("el valor ahora es"+ str(VALORDI))
  elif COSTO < 2000000 and MARCA.upper != "NOSY":
    VALORAI=calcestereo(COSTO,0)
    VALORDI=calcestereo(VALORAI,iva)
    print("el valor ahora es"+ str(VALORDI))
valestereo()





































































