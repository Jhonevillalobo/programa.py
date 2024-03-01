print ("calcular el area de un triangulo") 

base=float(input("digite el valor de la base")) 

altura=float(input("digite el valor de la altura")) 

  

resultado=(base*altura)/2 

  

print("el resultado es"+ str (resultado)) 

  

print ("digite dos numeros y sumar") 

primer_digito=float(input("digite el valor")) 

segundo_digito=float(input("digite el valor")) 

  

resultado=(primer_digito+segundo_digito) 

  

print("el resultado es"+ str (resultado)) 

  

  

  

  

  

  

print ("ingrese un digito para asi elevarlo al cuadrado") 

digito=float(input("ingrese el valor")) 

  

resultado=digito*digito 

  

print ("el resultado es"+ str(resultado)) 

  

print("convierta euros a dolares") 

euros=float(input("digite la cantidad de euros")) 

dolares=1.08 

  

conversion=(euros*dolares) 

  

  

print("el resultado del perimetro es"+ str(conversion)) 

  

print ("ingrese el valor del lado de un cuadrado para asi hallar  el perimetro") 

  

digito=float(input("ingrese el valor")) 

  

  

resultado=digito+digito+digito+digito 

  

print ("el resultado del perimetro es"+ str(resultado)) 

  

print ("ingrese el valor del lado de un cuadrado para asi hallar  el area") 

  

digito=float(input("ingrese el valor")) 

resultado=digito*digito 

print ("el resultado del area es"+ str(resultado)) 



  

print ("cilindro para asi hallar  el volumen") 

  

radio=float(input("ingrese el valor del radio")) 

altura=float(input("ingrese el valor altura")) 

pi= 3.14 

resultado= pi* radio*radio* altura 

print ("el resultado del volumen es"+ str(resultado))   

 

import math

def longitud_circunferencia(radio):
    """
    Calcula la longitud de una circunferencia dado su radio.

    Args:
    radio (float): El radio de la circunferencia.

    Returns:
    float: La longitud de la circunferencia.
    """
    return 2 * math.pi * radio

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
    radio (float): El radio del círculo.

    Returns:
    float: El área del círculo.
    """
    return math.pi * radio ** 2

# Solicitar al usuario que ingrese el radio de la circunferencia
radio = float(input("Ingrese el radio de la circunferencia: "))

# Calcular la longitud de la circunferencia y el área del círculo
longitud = longitud_circunferencia(radio)
area = area_circulo(radio)

# Calcular el área del círculo inscrito
area_inscrito = area_circulo(radio / 2)

# Mostrar los resultados
print(f"La longitud de la circunferencia es: {longitud}")
print(f"El área del círculo es: {area}")
print(f"El área del círculo inscrito es: {area_inscrito}")

 
