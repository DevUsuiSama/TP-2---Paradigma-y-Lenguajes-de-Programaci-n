#
# Trabajo Práctico Nº 2
#
# Alumnos: José Fernando Usui, Luciana Rojas.
#

import os
import random

# Función para limpiar la pantalla
clear = lambda: os.system('cls')

class Nodo:
    def __init__(self, dato: any):
        self.dato = dato
        self.siguiente = None

class Queue:
    def __init__(self):
        self.final = None
        self.principio = None
    def comparar(self, operacion):
        if self.principio == None:
            return False
        else:
            aux = self.final
            while not self.esta_vacio(aux):
                if operacion(aux):
                    return True
                aux = aux.siguiente
            return False
    def obtener_el_nodo_anterior(self, puntero):
        if self.esta_vacio(puntero):
            return None
        else:
            anterior = None
            while not self.esta_vacio(puntero.siguiente):
                    anterior = puntero
                    puntero = puntero.siguiente
            return [anterior, puntero]
    # Ingresa el nodo a la cola
    def encolar(self, nodo):
        if self.final == None:
            self.final = nodo
            self.principio = nodo
        else:
            self.principio.siguiente = nodo
            self.principio = nodo
    # Va sacando los nodos de la cola
    def desencolar(self):
        if self.principio == None:
            return None
        else:
            aux = self.final
            if self.esta_vacio(aux.siguiente):
                self.principio = None
                self.final = None
                return aux
            else:
                resultado = self.obtener_el_nodo_anterior(aux)
                anterior = resultado[0]
                aux = resultado[1]
                if aux == self.principio:
                    self.principio = anterior
                    self.principio.siguiente = None
                    return aux
                return None
    def desencolar_por_condicion(self, operacion):
        if self.principio == None:
            return None
        else:
            aux = self.final
            if self.esta_vacio(aux.siguiente):
                if operacion(aux):
                    self.principio = None
                    self.final = None
                    return aux
                else:
                    return None
            else:
                anterior = None
                while not self.esta_vacio(aux):
                    if operacion(aux):
                        self.principio = anterior
                        if self.esta_vacio(self.principio):
                            self.principio = aux.siguiente
                        else:
                            self.principio.siguiente = aux.siguiente
                        aux.siguiente = None
                        return aux
                    anterior = aux
                    aux = aux.siguiente
                return None
    # Devuelve la cantidad nodos existente en la cola
    def cantidad_nodos(self):
        if self.principio == None:
            return 0
        else:
            contador = 0
            aux = self.final
            while not self.esta_vacio(aux):
                contador += 1
                aux = aux.siguiente
            return contador
    # Comprueba que el puntero este vació
    def esta_vacio(self, puntero):
        if puntero == None:
            return True
        else:
            return False

class Stack:
    # Sé instancia la pila con el puntero en None
    def __init__(self):
        self.puntero = None
    # Enlaza los nodos, a los nodos existente en el puntero
    def insertar(self, nodo: Nodo):
        if self.esta_vacio(self.puntero):
            self.puntero = nodo
        else:
            nodo.siguiente = self.puntero
            self.puntero = nodo
    def buscar(self, operacion) -> Nodo:
        aux: Nodo = self.puntero
        while not self.esta_vacio(aux):
            if operacion(aux):
                return aux
            aux = aux.siguiente
        return None
    def cantidad(self, operacion) -> int:
        contador = 0
        aux: Nodo = self.puntero
        while not self.esta_vacio(aux):
            if operacion(aux):
                contador += 1
            aux = aux.siguiente
        return contador
    # Comprueba que el puntero este vació
    def esta_vacio(self, puntero: Nodo):
        return puntero == None

# Sé hace responsable solamente de almacenar los datos que pasé por parámetro
class Cliente:
    # DNI: Documento Nacional de Identidad
    # nombre: El nombre de la persona
    # apellido: El apellido de la persona
    # estado: En que estado se encuentra el cliente (1: Embarazada, 2: Anciano, 3: Discapacitado, 4: Perfectamente Normal)
    def __init__(self, DNI: int, nombre: str, apellido: str, estado: int):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.estado = estado

# Sé hace responsable solamente de almacenar los datos que pasé por parámetro
class Carrito:
    # id: Nos permite identificar el Carrito
    # cliente: Es un nodo que nos dará la maxima información del mismo
    # nro_cola: Es el número con la cual identificamos en que cola esta (no incluye el 0).
    # estado: En que estado se encuentra el carrito (0: Esta ocupado, 1: Esta libre)
    def __init__(self, id: int, cliente: Nodo, nro_cola: int, estado: int):
        self.id = id
        self.cliente = cliente
        self.nro_cola = nro_cola
        self.estado = estado

class Caja:
    # Caja[0] = {x|prioridad clientes embarazadas y ancianos}
    # Caja[1] = {x|solo clientes discapacitados}
    # Caja[2] = {x|solo clientes normales} 
    def __init__(self):
        self.cajas_del_supermercado = [Queue(), Queue(), Queue()]
    # (1 > x > 3)
    def esta_dentro_del_intervalo(self, nro_caja):
        if nro_caja < 1 or nro_caja > 3:
            print("ER-0001: El nro de caja no se encuentra dentro del intervalo [1,3]")
            return True
        else:
            return False
    def agregar_a_la_cola(self, nro_caja, nodo):
        if not self.esta_dentro_del_intervalo(nro_caja):
            self.cajas_del_supermercado[nro_caja - 1].encolar(nodo)
    def sacar_de_la_cola(self, nro_caja):
        if not self.esta_dentro_del_intervalo(nro_caja):
            return self.cajas_del_supermercado[nro_caja - 1].desencolar()
        else:
            return None
    # Tarea: Comprobar la cantidad de clientes en cola de la caja
    def cantidad_de_clientes(self, nro_caja):
        if not self.esta_dentro_del_intervalo(nro_caja):
            return self.cajas_del_supermercado[nro_caja - 1].cantidad_nodos()
        else:
            return 0
    def comparar_datos(self, nro_caja, operacion):
        if not self.esta_dentro_del_intervalo(nro_caja):
            return self.cajas_del_supermercado[nro_caja - 1].comparar(operacion)
        else:
            return None

# Sé hace responsable de un conjunto de carritos
class Carritos:
    # Sé inicializa con 6 carritos con valor predeterminado
    def __init__(self):
        self.carritos = Stack()
        for i in range(6):
            self.carritos.insertar(Nodo(Carrito(i + 1, None, 0, 1)))
    def hay_carrito_disponible(self):
        return self.carritos.buscar(lambda x: x.dato.estado == 1)
    # Buscar un carrito por su ID
    def buscar_por_id(self, id: int) -> Nodo:
        return self.carritos.buscar(lambda x: x.dato.id == id)
    def buscar_por_DNI(self, DNI: int) -> Nodo:
        return self.carritos.buscar(lambda x: not self.carritos.esta_vacio(x.dato.cliente) and x.dato.cliente.dato.DNI == DNI)
    # Comprueba que el puntero este vació
    def cantidad(self):
        return self.carritos.cantidad(lambda x: x.dato.estado == 1)
    def esta_vacio(self, puntero: Nodo):
        return puntero == None

# Nos permite verificar si la opción está dentro del conjunto "lista_de_opcion"
def controlar_opcion(opcion: int, conjunto: list):
    for x in conjunto:
        if opcion == x:
            return True
    return False

def main():
    cola_de_la_caja = Caja()
    cola_de_espera_de_carritos_disponibles = Queue()
    carritos = Carritos()
    while True:
        print('Menu:')
        print('1> Ingreso de Clientes')
        print('2> Cobros en Caja')
        print('3> Estado de un Carrito')
        print('4> Estado General del Supermercado')
        print('5> Salir')
        print()
        try:
            opcion = int(input('Ingrese una opcion: '))
        except ValueError:
            print('-- Error -- Ingrese un opción valida')
            input('Presione cualquier tecla para continuar...')
            clear()
            continue
        print()
        if controlar_opcion(opcion, [1, 2, 3, 4, 5]):
            if opcion == 1:
                clear()
                print('Agregar cliente:')
                nombre = input('\nIngresar el nombre del cliente: ')
                apellido = input('Ingresar el apellido del cliente: ')
                # =================================================================
                # ESTRUCTURA DE CONTROL 1
                while True:
                    try:
                        DNI = int(input('Ingresar el DNI del cliente: '))
                        if DNI > 0 and DNI < 70000000:
                            break
                        else:
                            print('-- El DNI ingresado no se encuentra dentro del intervalo [1, 69999999] --')
                            continue
                    except ValueError:
                        print('-- Error -- Ingrese un valor valido')
                        continue
                # =================================================================
                print('\nEstado del cliente:')
                print('\t1> \U0001F930 Embarazada')
                print('\t2> \U0001F474 Anciano')
                print('\t3> \U0001F9BD Discapacitados')
                print('\t4> \U0001F9CD Perfectamente normal')
                # =================================================================
                # ESTRUCTURA DE CONTROL 2
                while True:
                    try:
                        estado = int(input('Ingrese una opcion: '))
                        while True:
                            if controlar_opcion(estado, [1, 2, 3, 4]):
                                break
                            else:
                                print('-- El estado ingresado no se encuentra dentro del conjunto definido [1, 2, 3, 4] --')
                                estado = int(input('Ingrese una opcion: '))
                        break
                    except ValueError:
                        print('-- Error -- Ingrese una opción valida')
                        continue
                # =================================================================
                if (cola_de_espera_de_carritos_disponibles.comparar(lambda aux : aux.dato.DNI == DNI) or 
                    cola_de_la_caja.comparar_datos(1, lambda aux : aux.dato.DNI == DNI) or 
                    cola_de_la_caja.comparar_datos(2, lambda aux : aux.dato.DNI == DNI) or
                    cola_de_la_caja.comparar_datos(3, lambda aux : aux.dato.DNI == DNI)):
                    print(f'\tEl cliente con DNI {DNI} ya se encuentra en algunas de las colas del supermercado')
                else:
                    carrito = carritos.hay_carrito_disponible()
                    if not carritos.esta_vacio(carrito):
                        carrito.dato.cliente = Nodo(Cliente(DNI, nombre, apellido, estado))
                        carrito.dato.estado = 0
                        if estado == 1 or estado == 2:
                            cola_de_la_caja.agregar_a_la_cola(1, Nodo(Cliente(DNI, nombre, apellido, estado)))
                            print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 1')
                            carrito.dato.nro_cola = 1
                        elif estado == 3:
                            cola_de_la_caja.agregar_a_la_cola(2, Nodo(Cliente(DNI, nombre, apellido, estado)))
                            print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 2')
                            carrito.dato.nro_cola = 2
                        elif estado == 4:
                            cola_de_la_caja.agregar_a_la_cola(3, Nodo(Cliente(DNI, nombre, apellido, estado)))
                            print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 3')
                            carrito.dato.nro_cola = 3
                        carrito = None
                    else:
                        print(f'\t{nombre} {apellido} de DNI {DNI} entro a la COLA DE ESPERA DE CARRITOS DISPONIBLES')
                        cola_de_espera_de_carritos_disponibles.encolar(Nodo(Cliente(DNI, nombre, apellido, estado)))
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 2:
                clear()
                print('---------------------------------------------------------------')
                nro_caja = random.randint(1, 3)
                cliente = cola_de_la_caja.sacar_de_la_cola(nro_caja)
                if cliente != None:
                    print(f'El cliente {cliente.dato.nombre} {cliente.dato.apellido} de DNI {cliente.dato.DNI} dejo la Caja Nro {nro_caja}')
                    carrito = carritos.buscar_por_DNI(cliente.dato.DNI)
                    if not carritos.esta_vacio(carrito):
                        carrito.dato.cliente = None
                        carrito.dato.estado = 1
                        carrito.dato.nro_cola = 0
                        print('\tUn carrito liberado')
                    cliente = None
                    carrito = None
                    carrito = carritos.hay_carrito_disponible()
                    if not carritos.esta_vacio(carrito):
                        # Tarea: Buscar en la COLA DE ESPERA DE CARRITOS DISPONIBLES, personas con prioridad definida y asignar un carrito.
                        if cola_de_espera_de_carritos_disponibles.comparar(lambda aux : aux.dato.estado == 1 or aux.dato.estado == 2 or aux.dato.estado == 3):
                            print('Hay un cliente de condiciones "ESPECIALES" en la COLA DE ESPERA DE CARRITOS DISPONIBLES')
                            cliente = cola_de_espera_de_carritos_disponibles.desencolar_por_condicion(lambda aux : aux.dato.estado == 1 or aux.dato.estado == 2 or aux.dato.estado == 3)
                            if cliente != None:
                                print('El cliente de la COLA DE ESPERA DE CARRITOS DISPONIBLES:')
                                carrito.dato.cliente = cliente
                                carrito.dato.estado = 0
                                if cliente.dato.estado == 1 or cliente.dato.estado == 2:
                                    cola_de_la_caja.agregar_a_la_cola(1, cliente)
                                    print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 1')
                                    carrito.dato.nro_cola = 1
                                elif cliente.dato.estado == 3:
                                    cola_de_la_caja.agregar_a_la_cola(2, cliente)
                                    print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 2')
                                    carrito.dato.nro_cola = 2
                                elif cliente.dato.estado == 4:
                                    cola_de_la_caja.agregar_a_la_cola(3, cliente)
                                    print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 3')
                                    carrito.dato.nro_cola = 3
                            else:
                                print('No hay ningún cliente en la COLA DE ESPERA DE CARRITOS DISPONIBLES')
                            cliente = None
                        else:
                            cliente = cola_de_espera_de_carritos_disponibles.desencolar()
                            if cliente != None:
                                print('El cliente de la COLA DE ESPERA DE CARRITOS DISPONIBLES:')
                                carrito.dato.cliente = cliente
                                carrito.dato.estado = 0
                                if cola_de_la_caja.cantidad_de_clientes(1) == 0:
                                    cola_de_la_caja.agregar_a_la_cola(1, cliente)
                                    print('\tLa Caja Nro 1 se encuentra vacia, el cliente normal identificado como:')
                                    print(f'\t\t{cliente.dato.nombre} {cliente.dato.apellido} de DNI {cliente.dato.DNI} entro a la cola de espera Caja Nro 1')
                                    carrito.dato.nro_cola = 1
                                elif cola_de_la_caja.cantidad_de_clientes(2) == 0:
                                    cola_de_la_caja.agregar_a_la_cola(2, cliente)
                                    print('\tLa Caja Nro 1 se encuentra vacia, el cliente normal identificado como:')
                                    print(f'\t\t{cliente.dato.nombre} {cliente.dato.apellido} de DNI {cliente.dato.DNI} entro a la cola de espera Caja Nro 2')
                                    carrito.dato.nro_cola = 2
                                else:
                                    cola_de_la_caja.agregar_a_la_cola(3, cliente)
                                    print(f'\t{cliente.dato.nombre} {cliente.dato.apellido} de DNI {cliente.dato.DNI} entro a la cola de espera Caja Nro 3')
                                    carrito.dato.nro_cola = 3
                            else:
                                print('No hay ningún cliente en la COLA DE ESPERA DE CARRITOS DISPONIBLES')
                            cliente = None
                    else:
                        print(f'\tNo hay carritos disponibles')
                    carrito = None 
                else:
                    print(f'No hay ningún cliente en la Caja Nro {nro_caja}')
                print('---------------------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 3:
                clear()
                print('---------------------------------------------------------------')
                try:
                    id = int(input('Ingrese un ID (1 - 6): '))
                    carrito = carritos.buscar_por_id(id)
                    if not carritos.esta_vacio(carrito):
                        print(f'\nCarrito ID {carrito.dato.id}:')
                        if carritos.esta_vacio(carrito.dato.cliente):
                            print('\tCliente: Ninguno')
                        else:
                            print(f'\tCliente:')
                            print(f'\t\t DNI: {carrito.dato.cliente.dato.DNI}')
                            print(f'\t\t Nombre: {carrito.dato.cliente.dato.nombre}')
                            print(f'\t\t Apellido: {carrito.dato.cliente.dato.apellido}')
                            if carrito.dato.cliente.dato.estado == 1:
                                print(f'\t\t Estado: \U0001F930 Embarazado/a')
                            elif carrito.dato.cliente.dato.estado == 2:
                                print(f'\t\t Estado: \U0001F474 Anciano/a')
                            elif carrito.dato.cliente.dato.estado == 3:
                                print(f'\t\t Estado: \U0001F9BD Discapacitado')
                            elif carrito.dato.cliente.dato.estado == 4:
                                print(f'\t\t Estado: \U0001F9CD Perfectamente Normal')
                        print(f'\tCola: {'Ninguno' if carrito.dato.nro_cola == 0 else carrito.dato.nro_cola}')
                        print(f'\tEstado: {'Libre' if carrito.dato.estado else 'Ocupado'}')
                    else:
                        print('El carrito buscado, no existe')
                except ValueError:
                    print('-- Error -- Ingrese un valor valido')
                    input('Presione cualquier tecla para continuar...')
                    clear()
                    continue
                print('---------------------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 4:
                clear()
                print('------------------------------------------------')
                print('Caja Nro 1: prioridad clientes embarazadas y ancianos')
                print('Caja Nro 2: solo clientes discapacitados')
                print('Caja Nro 3: solo clientes perfectamente normales')
                print('\nEstado General del Supermercado:')
                print('\tCarritos: ', end='')
                for x in range(carritos.cantidad()):
                    print(f'\U0001F6D2', end='')
                print('\n\tCaja Nro 1: ', end='')
                for x in range(cola_de_la_caja.cantidad_de_clientes(1)):
                    print(f'\U0001F9CD', end='')
                print('\n\tCaja Nro 2: ', end='')
                for x in range(cola_de_la_caja.cantidad_de_clientes(2)):
                    print(f'\U0001F9BD', end='')
                print('\n\tCaja Nro 3: ', end='')
                for x in range(cola_de_la_caja.cantidad_de_clientes(3)):
                    print(f'\U0001F9CD', end='')
                print('\n\tEsperando Carrito Disponibles: ', end='')
                for x in range(cola_de_espera_de_carritos_disponibles.cantidad_nodos()):
                    print(f'\U0001F9CD', end='')
                print('\n------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 5:
                break
        else:
            print('-- Error -- La opcion ingresada no existe')
            input('Presione cualquier tecla para continuar...')
            clear()

if __name__ == '__main__':
    main()