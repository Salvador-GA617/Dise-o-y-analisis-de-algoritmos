import sys

sys.setrecursionlimit(2000)

# --- Variables Globales ---
laberinto_grid = None
num_filas = 0
num_columnas = 0
pila_solucion = []

def cargar_laberinto(filename):
    
    laberinto = []
    pos_inicio = None
    
    try:
        with open(filename, 'r') as f:
            try:
                filas = int(f.readline().strip())
            except ValueError:
                return None, 0, 0, None
            
            try:
                columnas = int(f.readline().strip())
            except ValueError:               
                return None, 0, 0, None

            for r in range(filas):
                linea = f.readline().strip()
                if not linea:
                    
                    return None, 0, 0, None              
                datos_fila = linea.split(',')
                if len(datos_fila) != columnas:
                    
                    return None, 0, 0, None
                
                laberinto.append(datos_fila)
                
                for c in range(columnas):
                    if datos_fila[c] == 'E':
                        pos_inicio = (r, c)
                        
    except FileNotFoundError:
        return None, 0, 0, None
    except Exception as e:
        
        return None, 0, 0, None
        
    if pos_inicio is None:
        
        return None, 0, 0, None

    return laberinto, filas, columnas, pos_inicio

def guardar_solucion_visual(archivo_original, archivo_salida, pila_ruta):
    
    
   
    laberinto_limpio = []
    try:
        with open(archivo_original, 'r') as f:
            filas = int(f.readline().strip())
            columnas = int(f.readline().strip())
            
            for _ in range(filas):
                datos_fila = f.readline().strip().split(',')
                laberinto_limpio.append(datos_fila)
    except Exception as e:
        return

    
    for (fila, col) in pila_ruta:
        celda_actual = laberinto_limpio[fila][col]
        if celda_actual != 'E' and celda_actual != 'S':
            laberinto_limpio[fila][col] = '*' 
            
    
    try:
        with open(archivo_salida, 'w') as f:
            f.write(f"{filas}\n")
            f.write(f"{columnas}\n")
            
            for fila_datos in laberinto_limpio:
                linea = ",".join(fila_datos)
                f.write(linea + "\n")
        
    except Exception as e:
        print(f"Error  {e}")

def resolver_laberinto_recursivo(x, y):
   
    
   
    if not (0 <= x < num_filas and 0 <= y < num_columnas):
        return False
        
    celda = laberinto_grid[x][y]
    if celda == '1' or celda == '.':
        return False
        
    
    pos_actual = (x, y)
    pila_solucion.append(pos_actual)
    
    
    if celda == 'S':
        return True
        
    
    if celda == '0' or celda == 'E':
        laberinto_grid[x][y] = '.' 

    if resolver_laberinto_recursivo(x + 1, y): # Abajo
        return True
    if resolver_laberinto_recursivo(x - 1, y): # Arriba
        return True
    if resolver_laberinto_recursivo(x, y + 1): # Derecha
        return True
    if resolver_laberinto_recursivo(x, y - 1): # Izquierda
        return True
        
    
    pila_solucion.pop()
    return False


def main():
   
    global laberinto_grid, num_filas, num_columnas, pila_solucion
    
    nombre_archivo = 'entrada.txt'
    
    datos_laberinto = cargar_laberinto(nombre_archivo)
    
    if datos_laberinto[0] is None:
        return
        
    laberinto_grid, num_filas, num_columnas, pos_inicio = datos_laberinto
    
    pila_solucion = [] 
    
    print(f"Laberinto de {num_filas}x{num_columnas} ")
    print(f"Iniciando en la Entrada 'E' en: {pos_inicio}")
    
    (x_inicio, y_inicio) = pos_inicio
    encontrado = resolver_laberinto_recursivo(x_inicio, y_inicio)
    
    if encontrado:
        print("La ruta de solución (de 'E' a 'S') guardada en la pila es:")
        print(pila_solucion)
        
       
        guardar_solucion_visual(nombre_archivo, 'solucion.txt', pila_solucion)
        
    else:
        print("\nNo se encontró una ruta de solución para el laberinto.")


if __name__ == "__main__":
    main()