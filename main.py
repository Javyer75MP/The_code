import sys
from modelos.persona import Persona
from modelos.alumno import Alumno


def agregar(numero,bbdd =[]):

    for i in range(numero):

        nombre = str(input("introduce el nombre: "))
        apellidos = str(input("introduce los apellidos: "))
        edad = int(input("introduce la edad: "))
        asignatura = str(input("Introduce las asignaturas: "))

        bbdd.append(Alumno(nombre,apellidos,edad,asignatura))

    return bbdd

def mostrar(lista):
    for persona in lista: 
        print (persona)

def mostrar_adultos(bbdd):
    print("++++++++++++++++++++ Estas son las personas mayores de edad +++++++++++++++++")
    for persona in bbdd:
        if persona.mayoredad:
            print(i)

bbdd = [Alumno('javi','montiel',20,'php'),
        Alumno('samu','rondon',30,'java'),
        Alumno('almu','miguel',40,'html'),
        Alumno('alberto','sanchez',15,'css'),
        Alumno('dani','moreno',17,'xml')
]


try:
    numero = int(input("Indroduce el numero de personas a añadir :"))
except ValueError:
    print ("Introduce un numero, por favor")
    sys.exit()

bbdd = agregar(numero,bbdd)
mostrar(bbdd)
#mostrar_adultos(bbdd)
