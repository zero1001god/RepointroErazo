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
print ("bienvenido a la calculadora")
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
  print("incorrecto")










