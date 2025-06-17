from funciones_actividad import *

while True:
    try:
        limpiar()
        imprimir("  Gestion de productos","titulo")
        print("""
    ╔════════════════════════╗
    ║1.-calcularIva          ║
    ║2.-descuento            ║
    ║3.-calcularImc          ║
    ║0.-Salir                ║
    ╚════════════════════════╝""")
        opcion=int(input("Seleccione : "))
        match opcion:
            case 0:
                break
            case 1:
                imprimir("calcularIva","titulo")
                calculariva()
            case 2:
                imprimir("descuento","titulo")
                descuento()
            case 3:
                imprimir("calcularImc","titulo")
                imc()
            case _:
                imprimir("Opcion no valida","error")

    except Exception as e:
        imprimir(f"Error : {e}","error")