# Importar el módulo 'sys' que proporciona acceso a variables y funciones específicas del intérprete de Python.
import sys

# Reconfigurar la salida estándar (stdout) para usar la codificación 'utf-8'.
sys.stdout.reconfigure(encoding='utf-8')


# Grafo no dirigido representado como una tabla de adyacencias
grafo = {
    'Venecia': ['Milán', 'Bolonia'],
    'Milán': ['Turín', 'Génova'],
    'Bolonia': ['Florencia', 'Venecia'],
    'Turín': ['Milán', 'Génova'],
    'Génova': [],
    'Florencia': ['Bolonia']
}

# Imprimir la tabla de adyacencias
print("| Ciudad      | Conexiones                          |")
print("|-------------|-------------------------------------|")

# Iterar sobre las ciudades y sus conexiones en el grafo
for ciudad, conexiones in grafo.items():
    # Convertir la lista de conexiones a una cadena o '-' si está vacía
    conexiones_str = ', '.join(conexiones) if conexiones else '-'
    print(f"| {ciudad:<11}| {conexiones_str:<35}|")
