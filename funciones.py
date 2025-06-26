#importamos aqui

import os,time

#tuplas, dicionarios y listas aqui
reservas=[]

#mi mayor momento cerebro galaxia esta aqui abajo
cantidadR=[]

def borrador():
    os.system("cls")
def esperar():
    time.sleep(3)
#estructura menu

def menu():
    mostrador="""TOTEM AUTOATENCIÓN RESERVA STRIKE
1.- Reservar zapatillas
2.- Buscar zapatillas reservadas.
3.- Cancelar reserva de zapatillas.
4.- SaLir.
"""
    
    while True:
        
        borrador()
        print(mostrador)
        print("Reservas actuales:",len(cantidadR))
        opc=input("Ingrese opcion (1-4): ")
        borrador()
        
        if opc=="1":
            reserva_zapatillas()
        
        elif opc=="2":
            buscar_reserva()
        elif opc=="3":
            cancerlar_reserva()
        elif opc=="4":
            print("Programa terminado...")
            return
        else:
            print("Debe ingresar una opción válida!!")
        esperar()

def reserva_zapatillas():
    
    print("MENU DE RESERVAS")
    
    if len(cantidadR)==20:
        print("No quedan mas reservas disponibles")
        return
    while True:
        nombre=input("Ingrese nombre de la persona a reservar: ").title().strip()
        if len(nombre)<3:
            print("Nombre muy corto")
            esperar()
            continue
        if nombre.isalpha():
            pass
        else:
            print("No se aceptan numeros.")
            esperar
            continue

        repetido=False
        for r in reservas:
            if nombre==r["nombre"]:
                print("Nombre ocupado")
                esperar()
                repetido=True
            
        if repetido==False:
            break
    while True:

        if repetido==False:
            while True:
                codigo=input("Escriba el código secreto (Recuerde respetar las mayúsculas y minúsculas): ")
                if codigo=="EstoyEnListaDeReserva":
                    reserva={
                        "nombre":nombre,
                        "cantidad":1
                    }
                    reservas.append(reserva)
                    cantidadR.append("a")
                    print("Reserva exitosa")
                    return
                else:
                    print("Codigo secreto no valido, pruebe otra vez")
                    esperar()


def buscar_reserva():
    print("BUSCAR RESERVA")
    while True:
       
        nombre=input("Ingrese nombre a buscar: ").title()
        for r in reservas:
            if nombre==r["nombre"]:
                print(f"Reserva encontrada: {r["nombre"]}, {r["cantidad"]} par(es) (estándar).")
                if r["cantidad"]<2 and len(cantidadR)<20:
                    vip=input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").lower()
                    if vip=="s":
                        print(f"Reserva actualizada a VIP. Ahora {r["nombre"]} tiene 2 pares reservados")
                        r["cantidad"]+=1
                        cantidadR.append("a")
                        return
                    else:
                        print("Manteniendo reserva actual")  
                        return
                else:
                    return
            else:
                print("Nombre no encontrado")

def cancerlar_reserva():
    print("CANCELAR RESERVA")
    while True:
        nombre=input("Ingrese nombre a cancelar reserva: ").title()
        for r in reservas:
            if nombre==r["nombre"]:
                print(f"La reserva de {r["nombre"]} ha sido cancelada")
                if r["cantidad"]==1:
                    cantidadR.pop()
                if r["cantidad"]==2:
                    cantidadR.pop()
                    cantidadR.pop()
                reservas.remove(r)

                return
            else:
                print("Nombre no encontrado")
                return
