

#Nodo para la clase linked list
class Node:
    def __init__(self,nombre,id,calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
        self.id = id
        self.siguiente =None


#Nodo para la clase arbol
class NodeAB:
    def __init__(self,raiz):
        self.raiz = raiz
        self.der = None
        self.izq = None

#Para indexar las matrículas  (ID) de los estudiantes,permitiendo búsquedas de alta velocidad para consultar datos específicos.
class ArbolB: 
    def __init__(self):
        self.raiz = None

    def insertar(self,dato):
        if not self.raiz:
            self.raiz = NodeAB(dato)
        else:
            self._insertar_rec(self.raiz,dato)

    def _insertar_rec(self,actual,dato):
        if actual is not None:
            if actual.raiz > dato:
                if actual.izq is None:
                    actual.izq = NodeAB(dato)
                else:
                    self._insertar_rec(actual.izq,dato)
            else:
                if actual.der is None:
                    actual.der = NodeAB(dato)
                else:
                    self._insertar_rec(actual.der,dato)
        
    def buscar(self,buscar):
        node = self._buscar_rec(self.raiz,buscar)
        if node:
            print(f'Encontrado ID: {node.raiz}')
        else:
            print('No encontrado')

    def _buscar_rec(self,actual,buscar):
        if actual is None:
            return None
        if actual.raiz == buscar:
            return actual
        if actual.raiz > buscar:
            return self._buscar_rec(actual.izq, buscar)
        else:
            return self._buscar_rec(actual.der,buscar)


#Para almacenar el registro principal de estudiantes activos.
class LinkedList:
    def __init__(self):
        self.cabeza = None
        
    def agregar_estudiante(self, id_estudiante, nombre, calificacion):
        nuevo_estudiante = Node(nombre ,id_estudiante, calificacion)
        if self.cabeza is None:
            self.cabeza = nuevo_estudiante
            print(f"Estudiante {nombre} añadido")
            return
        actual = self.cabeza
        while actual.siguiente: 
            actual = actual.siguiente
        
        actual.siguiente = nuevo_estudiante
        print(f"Estudiante {nombre} añadido al final.")

    def mostrar_lista(self):
        estudiantes = []
        actual = self.cabeza
        while actual:
            estudiantes.append(f"ID: {actual.id} | {actual.nombre} ({actual.calificacion})")
            actual = actual.siguiente
        
        print("\nLISTA DE ESTUDIANTES ACTIVOS")
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("\n".join(estudiantes))
            print("-------------------------------")


    def obtener_lista_nodos(self):
            nodos = []
            actual = self.cabeza
            while actual:
                nodos.append(actual)
                actual = actual.siguiente
            return nodos

#Funcionará como un historial de "Deshacer" (Undo). Almacenará las últimas
#acciones realizadas (ej. agregar un estudiante) para poder revertirlas si hubo un error,


class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0
    
    def remove(self):
        if self.isEmpty():
            return False
        else:
            self.list.pop(-1)

    def addAction(self, value):
        self.list.append(value)
    
    def top(self):
        print(self.list[-1])

#Gestionará la "Ventanilla de Atención".
class Queue:
    def __init__(self):
        self.list= []

    def isEmpty(self):
        return len(self.list) == 0

    def remove(self):
        if self.isEmpty():
            return False
        else:
            self.list.pop(0)
        
    def add(self,idAlumno):
        self.list.append(idAlumno)

    def peek(self):
        print(self.list[0])

#Para ordenar la lista de estudiantes según su promedio general (de mayor a menor).
   
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].calificacion < arr[j+1].calificacion:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Para ordenar alfabéticamente los reportes de asistencia 
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j].nombre.lower() < arr[min_index].nombre.lower():
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


#Menú interactivo en consola que permita navegar entre las distintas estructuras
#(Agregar alumno, Atender cola, Buscar en árbol, Generar reporte ordenado).
def menu():
    print('''Elija una opcion:
(1)Agregar Alumno
(2)Atender Cola
(3)Buscar en Arbol
(4)Generar Reporte ordenado
(5)Salir''')
    return input('')

#Uso de archivos .csv o .txt para cargar y guardar la base de datos de
#estudiantes al iniciar y cerrar el programa.

def data():
    pass


def main():
    tree = ArbolB()
    pila = Stack() 
    cola = Queue()
    lista_estudiantes = LinkedList()
    while True:
        x = menu()
        match x:
            case '1':
                id_alum = int(input('Ingrese ID del estudiante: '))
                nom_alum = input('Ingrese Nombre del estudiante: ')
                cal_alum = float(input('Ingrese Calificación: '))
                
                lista_estudiantes.agregar_estudiante(id_alum, nom_alum, cal_alum)
                tree.insertar(id_alum)
                pila.addAction(f"Agregado ID: {id_alum}")

            case '2':
                if not cola.isEmpty():
                    print(f"Atendiendo al alumno con ID: {cola.list[0]}")
                    cola.remove()
                else:
                    print("La cola está vacía.")

            case '3':
                id_busqueda = int(input("Ingrese ID a buscar: "))
                tree.buscar(id_busqueda)

            case '4':
                    x = input('Quiere el reporte alfabeticamente(A) o por calificaciones(B)? ')
                    if x == 'A':

                        nodos = lista_estudiantes.obtener_lista_nodos()
                        nombres = selection_sort(nodos)
                        with open('ReporteAlfabetico.txt', 'a') as f:
                            for nodo in nombres:
                                f.writelines(f"Nombre: {nodo.nombre} | ID: {nodo.id} | Calificación: {nodo.calificacion}\n")
                        print('Reporte guardado como ReporteAlfabetico.txt')
                    elif x == 'B':

                        nodos = lista_estudiantes.obtener_lista_nodos()
                        calif = bubble_sort(nodos)
                        with open('ReporteCalificaciones.txt', 'a') as f:
                            for nodo in calif:
                                f.writelines(f"Nombre: {nodo.nombre} | ID: {nodo.id} | Calificación: {nodo.calificacion}\n")
                        print('Reporte guardado como ReporteCalificaciones.txt')

            case '5':
                break
            
if __name__ == '__main__':
    main()