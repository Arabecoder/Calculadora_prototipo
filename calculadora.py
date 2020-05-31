"""Aquí elaboré una clase para cerrar el programa una vez quiera hacerlo"""


def Salir():
    input("Presiona cualquier tecla para finalizar: ")
    import sys
    sys.exit()


"""Aquí elaboré una clase para limpiar la pantalla en cada operación si el usuario así lo quiere, de esta manera todo estará mas organizado"""


def LimpiarPantalla():
    import os
    os.system("cls")


"""La siguiente clase mostrará el menú"""


def MenuAritmetico():
    print("""************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Cuadrado
6) Ir al menú geométrico
7) Salir""")


"""El menú para seleccionar las operaciones geométricas"""


def MenuGeometrico():
    print("""*************
Calculadora Geométrica
************
Menu
1) Cuerpos redondos
2) Cuerpos cuadrados
3) Cuerpos triangulares
4) Volver al menú aritmético
5) Salir""")


def MenuRedondos():
    print("""*************
Cuerpos Redondos
************
Menu
1) Círculo
2) Cilindro
3) Elipse
4) Volver al menú geométrico
5) Salir""")


def MenuCirculo():
    print("""*************
Menú Círculo
************
Menu
1) Área
2) Volúmen
3) Diametro
4) Volver al menú geométrico""")


def MenuCilindro():
    print("""*************
Menú Cilindro
************
Menu
1) Área total
2) Volúmen
3) Diametro
4) Volver al menú geométrico""")


def MenuElipse():
    print("""*************
Menú Elipse
************
Menu
1) Área
2) Volúmen
3) Diametro
4) Volver al menú geométrico""")


"""La calculadora capaz de hacer operaciones geométricas"""


def CalculadoraGeometrica():
    opc = int(input("Seleccione una opción: "))
    while (opc > 0 and opc < 5):
        if (opc == 1):
            MenuRedondos()
            redondo = int(input("Seleccione una opción: "))
            if (redondo == 1):
                MenuCirculo()
                circulo = int(input("Seleccione una opción: "))
                if (circulo == 1):
                    radio = float(input("Ingrese el radio del cículo: "))
                    print("El área del círculo es: ", radio ** 2 * 3.14159)
                    val = str(input(
                        "Ingrese una C para limpiar la pantalla y hacer una nueva operación, D para continuar sin borrar la pantalla, cualquier otra tecla finalizará el programa: "))
                    if (val == "C" or val == "c"):
                        LimpiarPantalla()
                        MenuGeometrico()
                        return CalculadoraGeometrica()
                    else:
                        if (val == "D" or val == "d"):
                            MenuGeometrico()
                            return CalculadoraGeometrica()
                        else:
                            Salir()
                else:
                    if (circulo == 2):
                        radio = float(input("Ingrese el radio del círculo/esfera: "))
                        print("El volúmen del círculo/esfera es: ", radio ** 3 * 3.14159 * 4 / 3)
                        val = str(input(
                            "Ingrese una C para limpiar la pantalla y hacer una nueva operación, D para continuar sin borrar la pantalla, cualquier otra tecla finalizará el programa: "))
                        if (val == "C" or val == "c"):
                            LimpiarPantalla()
                            MenuGeometrico()
                            return CalculadoraGeometrica()
                        else:
                            if (val == "D" or val == "d"):
                                MenuGeometrico()
                                return CalculadoraGeometrica()
                            else:
                                Salir()
                    else:
                        if (circulo == 3):
                            radio = float(input("Ingrese el radio del círculo: "))
                            print("El diámetro del círculo es: ", 2 * radio)
                            val = str(input(
                                "Ingrese una C para limpiar la pantalla y hacer una nueva operación, D para continuar sin borrar la pantalla, cualquier otra tecla finalizará el programa: "))
                            if (val == "C" or val == "c"):
                                LimpiarPantalla()
                                MenuGeometrico()
                                return CalculadoraGeometrica()
                            else:
                                if (val == "D" or val == "d"):
                                    MenuGeometrico()
                                    return CalculadoraGeometrica()
                                else:
                                    Salir()
                        else:
                            if (circulo == 4):
                                LimpiarPantalla()
                                MenuGeometrico()
                                return CalculadoraGeometrica()
            else:
                if (redondo == 2):
                    MenuCilindro()
                    cilindro = int(input("Seleccione una opción: "))
                    if (cilindro == 1):
                        radio = float(input("Ingrese el radio del cilindro: "))
                        altura = float(input("Ingrese la altura del cilindro: "))
                        areabase = 2 * 3.14159 * radio * altura
                        print("El área del a base del cilindro es ", areabase)
                        print("El área total del cilindro es ", areabase + 2 * radio ** 2 * 3.14159 * 2)
                        val = str(input(
                            "Ingrese una C para limpiar la pantalla y hacer una nueva operación, D para continuar sin borrar la pantalla, cualquier otra tecla finalizará el programa: "))
                        if (val == "C" or val == "c"):
                            LimpiarPantalla()
                            MenuGeometrico()
                            return CalculadoraGeometrica()
                        else:
                            if (val == "D" or val == "d"):
                                MenuGeometrico()
                                return CalculadoraGeometrica()
                            else:
                                Salir()
                    else:
                        if (cilindro == 2):
                            radio = float(input("Ingrese el radio del cilindro: "))
                            altura = float(input("Ingrese la altura del cilindro: "))
                            print("El volumen del cilindro es: ", radio ** 2 * 3.14159 * altura)
                            val = str(input(
                                "Ingrese una C para limpiar la pantalla y hacer una nueva operación, D para continuar sin borrar la pantalla, cualquier otra tecla finalizará el programa: "))
                            if (val == "C" or val == "c"):
                                LimpiarPantalla()
                                MenuGeometrico()
                                return CalculadoraGeometrica()
                            else:
                                if (val == "D" or val == "d"):
                                    MenuGeometrico()
                                    return CalculadoraGeometrica()
                                else:
                                    Salir()
                        else:
                            if (cilindro == 3):
                                radio = float(input("Ingrese el radio del cilindro: "))
                                print("El diámetro del cilindro es: ", radio * 2)
                                val = str(input(
                                    "Ingrese una C para limpiar la pantalla y hacer una nueva operación, D para continuar sin borrar la pantalla, cualquier otra tecla finalizará el programa: "))
                                if (val == "C" or val == "c"):
                                    LimpiarPantalla()
                                    MenuGeometrico()
                                    return CalculadoraGeometrica()
                                else:
                                    if (val == "D" or val == "d"):
                                        MenuGeometrico()
                                        return CalculadoraGeometrica()
                                    else:
                                        Salir()
                            else:
                                if (cilindro == 4):
                                    LimpiarPantalla()
                                    MenuGeometrico()
                                    return CalculadoraGeometrica()
                else:
                    if (redondo == 3):
                        MenuElipse()
                        elipse = int(input("Selecciona una opción: "))
                        if (elipse == 1):
                            radio1 = float(input("Ingrese el primer radio: "))
                            radio2 = float(input("Ingrese el segundo radio: "))
                            print("El área del elipse es: ", radio1 + radio2 * 3.14159)
                            val = str(input(
                                "Ingrese una C para limpiar la pantalla y hacer una nueva operación, D para continuar sin borrar la pantalla, cualquier otra tecla finalizará el programa: "))
                            if (val == "C" or val == "c"):
                                LimpiarPantalla()
                                MenuGeometrico()
                                return CalculadoraGeometrica()
                            else:
                                if (val == "D" or val == "d"):
                                    MenuGeometrico()
                                    return CalculadoraGeometrica()
                                else:
                                    Salir()
                        else:
                            if (elipse == 2):
                                radio1 = float(input("Ingrese el primer radio: "))
                                radio2 = float(input("Ingrese el segundo radio: "))
                                radio3 = float(input("Ingrese el tercer radiO: "))
                                print("El volumen del elipse es: ", 4 * 3.14159 * radio1 * radio2 * radio3 / 3)
                                val = str(input(
                                    "Ingrese una C para limpiar la pantalla y hacer una nueva operación, D para continuar sin borrar la pantalla, cualquier otra tecla finalizará el programa: "))
                                if (val == "C" or val == "c"):
                                    LimpiarPantalla()
                                    MenuGeometrico()
                                    return CalculadoraGeometrica()
                                else:
                                    if (val == "D" or val == "d"):
                                        MenuGeometrico()
                                        return CalculadoraGeometrica()
                                    else:
                                        Salir()
                            else:
                                if (elipse == 3):
                                    radiototal = 0
                                    valor = int(input("Ingrese la cantidad de radio del elipse: "))
                                    for x in range(valor):
                                        radio = float(input("Ingrese el radio del elipse: "))
                                        radiototal = radiototal + radio
                                    print("El diametro del elipse es: ", radiototal)
                                    val = str(input(
                                        "Ingrese una C para limpiar la pantalla y hacer una nueva operación, D para continuar sin borrar la pantalla, cualquier otra tecla finalizará el programa: "))
                                    if (val == "C" or val == "c"):
                                        LimpiarPantalla()
                                        MenuGeometrico()
                                        return CalculadoraGeometrica()
                                    else:
                                        if (val == "D" or val == "d"):
                                            MenuGeometrico()
                                            return CalculadoraGeometrica()
                                        else:
                                            Salir()
                                else:
                                    if (elipse == 4):
                                        LimpiarPantalla()
                                        MenuGeometrico()
                                        return CalculadoraGeometrica()
                    else:
                        if (redondo == 4):
                            LimpiarPantalla()
                            MenuGeometrico()
                            return CalculadoraGeometrica()
                        else:
                            LimpiarPantalla()
                            print("Ha escrito una tecla fuera de las opciones, el programa se reinició.")
                            MenuGeometrico()
                            return CalculadoraGeometrica()
        else:
            if (opc == 4):
                LimpiarPantalla()
                MenuAritmetico()
                CalculadoraAritmetica()
    if (opc == 5):
        Salir()
    else:
        LimpiarPantalla()
        print("Ha escrito una tecla fuera de las opciones, el programa se reinició.")
        MenuGeometrico()
        return CalculadoraGeometrica()
