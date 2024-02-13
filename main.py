# -------------------------------------------------------------------------------------------
import csv

# -------------------------------------------------------------------------------------------
#Define la clase Nodo
class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None

#--------------------------------------------------------------------------------------------------
# #Define la clase ArbolBinario
class ArbolBinario:
    def __init__(self, clave_raiz=None):
        """
        Constructor de la clase, la raíz comienza sin atributos.

        Parameters:
            clave_raiz (int): Clave opcional de la raíz del árbol.
        """
        self.raiz = None
        if clave_raiz is not None:
            self.raiz = Nodo(clave_raiz)

    def insertar(self, clave):
        """
        Inserta un nuevo nodo con la clave proporcionada en el árbol AVL.

        Parameters:
            clave (int): La clave a insertar en el árbol.

        Returns:
            None
        """
        self.raiz = self._insertar(self.raiz, clave)

    def _insertar(self, raiz, clave):
        """
        Inserta un nodo con la clave dada en el árbol de búsqueda binaria con raíz en raiz.

        Parámetros:
            raiz (Nodo): La raíz del árbol de búsqueda binaria.
            clave (int): La clave del nodo a insertar.

        Retorna:
            Nodo: La raíz del árbol de búsqueda binaria después de la inserción.
        """
        if raiz is None:
            return Nodo(clave)
        if clave < raiz.clave:
            raiz.izquierda = self._insertar(raiz.izquierda, clave)
        elif clave > raiz.clave:
            raiz.derecha = self._insertar(raiz.derecha, clave)
        return raiz


#--------------------------------------------------------------------------------------------------
# Función para mostrar el árbol
def mostrar_arbol(arbol):
    """
    Función para mostrar la estructura del árbol a partir del nodo raíz.
    
    Args:
    arbol: El objeto árbol que se mostrará.
    
    Returns:
    None
    """
    if arbol.raiz is not None:
        imprimir_arbol(arbol.raiz, 0)

#--------------------------------------------------------------------------------------------------
def imprimir_arbol(raiz, espacio):
    """
    Imprime recursivamente el árbol binario en un formato visualmente atractivo.
    
    Args:
    - raiz: El nodo raíz del árbol binario.
    - espacio: La cantidad de espacio para sangrar cada nivel del árbol.
    
    Returns:
    None
    """
    if raiz is not None:
        imprimir_arbol(raiz.derecha, espacio + 10)
        print(" " * espacio + str(raiz.clave))
        imprimir_arbol(raiz.izquierda, espacio + 10)

#------------------------------------------------------------------------------
def cargar_datos_desde_csv(archivo_csv):
    """
    Carga datos desde un archivo CSV y devuelve el contenido como una lista de diccionarios.

    Args:
    archivo_csv (str): La ruta al archivo CSV que se cargará.

    Returns:
    list: Una lista de diccionarios que contiene los datos del archivo CSV.

    Si el archivo no se encuentra, se devuelve None.
    """
    try:
        with open(archivo_csv, 'r', encoding='latin-1') as archivo:
            reader = csv.DictReader(archivo)
            datos = [row for row in reader]
        return datos
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_csv}' no se encuentra.")
        return None

#------------------------------------------------------------------------------
def ordenar_por_burbuja(datos, campo_clave):
    """
    Ordena la lista dada de diccionarios por el campo especificado utilizando el algoritmo de burbuja.

    Parámetros:
    - datos: una lista de diccionarios que se ordenarán
    - campo_clave: la clave que se utilizará para ordenar los diccionarios

    Retorna:
    None
    """
    n = len(datos)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if datos[j][campo_clave] > datos[j + 1][campo_clave]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

#------------------------------------------------------------------------------
def ordenar_por_insercion(datos, campo_clave):
    """
    Ordena la lista de datos mediante inserción utilizando el campo clave especificado.

    Parámetros:
    - datos: la lista de elementos que se ordenarán
    - campo_clave: el campo clave en función del cual se realizará la ordenación

    Retorna:
    None
    """
    n = len(datos)
    for i in range(1, n):
        valor_actual = datos[i]
        j = i - 1
        while j >= 0 and valor_actual[campo_clave] < datos[j][campo_clave]:
            datos[j + 1] = datos[j]
            j -= 1
        datos[j + 1] = valor_actual

#------------------------------------------------------------------------------
def quicksort(datos, campo_clave, bajo, alto):
    """
    Ordena los datos dados utilizando el algoritmo de quicksort.

    Parámetros:
    - datos: la lista de datos que se ordenará
    - campo_clave: el campo utilizado como clave para la comparación durante la ordenación
    - bajo: el índice inferior de los datos que se ordenarán
    - alto: el índice superior de los datos que se ordenarán
    """
    stack = [(bajo, alto)]
    while stack:
        bajo, alto = stack.pop()
        if bajo < alto:
            pivote = particion_rapida(datos, campo_clave, bajo, alto)
            stack.append((bajo, pivote - 1))
            stack.append((pivote + 1, alto))

#------------------------------------------------------------------------------
def particion_rapida(datos, campo_clave, bajo, alto):
    """
    Esta función implementa el algoritmo de partición quicksort para particionar la lista 'datos' basada en el campo 'campo_clave'. 
    Toma la lista 'datos', 'campo_clave' como el campo clave, 'bajo' como el índice bajo, y 'alto' como el índice alto como parámetros. 
    Retorna el índice del elemento pivote después de la partición.
    """
    pivote = datos[alto][campo_clave]
    i = bajo - 1
    for j in range(bajo, alto):
        if datos[j][campo_clave] <= pivote:
            i += 1
            datos[i], datos[j] = datos[j], datos[i]
    datos[i + 1], datos[alto] = datos[alto], datos[i + 1]
    return i + 1

#------------------------------------------------------------------------------
def busqueda_secuencial(datos, campo_clave, valor):
    """
    Realiza una búsqueda secuencial del valor dado en el conjunto de datos proporcionado basándose en el campo clave especificado.
    
    :param datos: El conjunto de datos que se va a buscar.
    :param campo_clave: El campo clave en función del cual se realizará la búsqueda.
    :param valor: El valor que se va a buscar dentro del conjunto de datos.
    :return: El índice de la primera ocurrencia del valor dentro del conjunto de datos, o -1 si el valor no se encuentra.
    """
    for i, dato in enumerate(datos):
        if dato[campo_clave] == valor:
            return i
    return -1

#------------------------------------------------------------------------------
def busqueda_secuencial_con_conteo(datos, campo_clave, valor):
    """
    Realiza una búsqueda secuencial en los datos dados para el campo clave y el valor especificados, contando el número de interacciones.
    """
    interacciones = 0
    for dato in datos:
        interacciones += 1
        if dato[campo_clave] == valor:
            return interacciones
    return -1

#------------------------------------------------------------------------------
def busqueda_binaria_optimizada(datos, campo_clave, valor):
    """
    Realiza una búsqueda binaria optimizada en los datos dados basándose en el campo clave y el valor especificados.

    Args:
    - datos: lista de diccionarios que representan los datos que se van a buscar
    - campo_clave: el campo clave en cada diccionario dentro de los datos que se utilizará para la comparación
    - valor: el valor que se va a buscar en el campo clave especificado

    Returns:
    - int: el índice del valor encontrado en los datos, o -1 si el valor no se encuentra
    """
    bajo = 0
    alto = len(datos) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if datos[medio][campo_clave] == valor:
            return medio
        elif datos[medio][campo_clave] < valor:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1

#------------------------------------------------------------------------------
def insertar_elemento(arbol, campo_clave):
    """
    Inserta un elemento en el árbol utilizando el valor proporcionado como clave.
    
    :param arbol: El árbol en el que se va a insertar el elemento.
    :param campo_clave: El valor que se utilizará como clave para insertar el elemento en el árbol.
    :return: No devuelve nada.
    """
    valor = input("Introduzca el valor a insertar: ")
    arbol.insertar(valor)
    print(f"Elemento '{valor}' insertado correctamente.")


#------------------------------------------------------------------------------
if __name__ == "__main__":
    archivo_csv = 'DatosPF2.csv'
    todos_los_datos = cargar_datos_desde_csv(archivo_csv)

#------------------------------------------------------------------------------
    def cambiar_campo_clave():
        """
        Función para cambiar el campo clave.
        """
        nuevo_campo = input("\nIntroduzca el nuevo campo clave: ")
        return nuevo_campo
    
    if todos_los_datos:
        campo_clave = input("\nIntroduzca el campo clave (opciones: " + ", ".join(todos_los_datos[0].keys()) + "): ")
        if campo_clave not in todos_los_datos[0].keys():
            print(f"Campo clave '{campo_clave}' no válido.")
        
        else:
            arbol = ArbolBinario()
            for dato in todos_los_datos:
                arbol.insertar(dato[campo_clave])

            while True:
                print("-" * 40)
                print("\n      Menú Principal:\n")
                print("     1. Mostrar árbol Binario")
                print("     2. Ordenar por Burbuja")
                print("     3. Ordenar por Inserción")
                print("     4. Ordenar por QuickSort")
                print("     5. Búsqueda Secuencial")
                print("     6. Búsqueda Secuencial con conteo")
                print("     7. Búsqueda Binaria")
                print("     8. Insertar elemento")
                print("     9. Cambiar campo clave")
                print("     10. Salir\n")
                print("-" * 40)

                opcion = input("\nIntroduzca una opción: ")
                
                if opcion == "1":
                    mostrar_arbol(arbol)
                elif opcion == "2":
                    ordenar_por_burbuja(todos_los_datos, campo_clave)
                    print("Base de datos ordenada por Burbuja:")
                    for dato in todos_los_datos:
                        print(dato)
#--------------------------------------------------------------------------------------------------
                elif opcion == "3":
                    ordenar_por_insercion(todos_los_datos, campo_clave)
                    print("Base de datos ordenada por Inserción:")
                    for dato in todos_los_datos:
                        print(dato)
#--------------------------------------------------------------------------------------------------
                elif opcion == "4":
                    try:
                        quicksort(todos_los_datos, campo_clave, 0, len(todos_los_datos) - 1)
                        print("Base de datos ordenada por QuickSort:")
                        for dato in todos_los_datos:
                            print(dato)
                    except TypeError:
                        print("No se puede aplicar QuickSort a campos no numéricos.")
#--------------------------------------------------------------------------------------------------
                elif opcion == "5":
                    valor_buscar = input("Introduzca el valor a buscar: ")
                    resultado = busqueda_secuencial(todos_los_datos, campo_clave, valor_buscar)
                    if resultado != -1:
                        print(f"Elemento encontrado en la posición {resultado}")
                    else:
                        print("Elemento no encontrado.")
#--------------------------------------------------------------------------------------------------
                elif opcion == "6":
                    valor_buscar = input("Introduzca el valor a buscar: ")
                    interacciones = busqueda_secuencial_con_conteo(todos_los_datos, campo_clave, valor_buscar)
                    if interacciones != -1:
                        print(f"Elemento encontrado. Interacciones: {interacciones}")
                    else:
                        print("Elemento no encontrado.")
#--------------------------------------------------------------------------------------------------
                elif opcion == "7":
                    valor_buscar = input("Introduzca el valor a buscar: ")
                    resultado = busqueda_binaria_optimizada(todos_los_datos, campo_clave, valor_buscar)
                    if resultado != -1:
                        print(f"Elemento encontrado en la posición {resultado}")
                    else:
                        print("Elemento no encontrado.")
#--------------------------------------------------------------------------------------------------
                elif opcion == "8":
                    insertar_elemento(arbol, campo_clave)
#--------------------------------------------------------------------------------------------------
                elif opcion == "9":
                    campo_clave = cambiar_campo_clave()
                    arbol = ArbolBinario()
                    for dato in todos_los_datos:
                        arbol.insertar(dato[campo_clave])
#--------------------------------------------------------------------------------------------------
                elif opcion == "10":
                    print("\nGracias por consultar. ¡Hasta luego!\n")
                    print("-" * 40)
                    break
                else:
                    print("Opción no válida.\n")
# -------------------------------------------------------------------------------------------