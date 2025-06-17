from os import system
from msvcrt import getch
from colorama import Fore,Style

def limpiar():
    print("presione tecla para continuar")
    getch()
    system("cls")

def imprimir(texto,c):
    if c=="error":
        print(f"{Fore.RED}❌ {texto} ❌{Style.RESET_ALL}")
    elif c=="bien":
        print(f"{Fore.GREEN}✅ {texto} ✅{Style.RESET_ALL}")
    elif c=="titulo":
        print(f"🔱{Fore.BLUE}{Style.BRIGHT} {texto} {Style.RESET_ALL}🔱")
    else:
        print(texto)
productos=[]

def buscar(id):
    for i in range(len(productos)):
        if productos[i]["id"]==id:
            return i #retornamos la coordenada del id
    return -1 #el -1 se asegura que el id no existe


def calculariva():
    nombre=input("Ingrese nombre del producto : ")
    precio=int(input("Ingrese precio : "))
    precioconiva=round(precio*0.19)
    imprimir(f"Iva de {nombre} calculado : {precioconiva}","bien")

def descuento():
    precio=int(input("Ingrese precio : "))
    descuento=float(input("Ingrese decuento : "))
    total=precio*descuento
    imprimir(f"total con descuento {precio-total}","bien")

def imc():
    peso=float(input("ingrese peso : "))
    altura=float(input("ingrese altura : "))
    resultado=peso/(altura**2)
    print(f"El imc es {resultado}")
    if resultado<18.5:
        print("Usted esta bajo peso")
    elif resultado>=18.5 and resultado <=24.9:
        print("Usted tiene peso normal")
    elif resultado>=25 and resultado<=29.9:
        print("Usted esta sobrepeso")
    elif resultado>=30 and resultado<=34.90:
        print("Usted esta en obesidad 1")
    elif resultado>=35 and resultado<=39.90:
        print("Usted esta en obesidad 2")
    elif resultado>=40:
        print(f"Usted esta en obesidad 3")
