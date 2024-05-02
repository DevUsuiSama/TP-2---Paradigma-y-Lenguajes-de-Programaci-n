# TP 2
- Asignatura: Paradigma y Lenguaje de Programación
- Carrera: Ingeniería en Sistemas de Información
- Profesor: Ing. Pedro Ferrando

## Descripción
Este proyecto es la entrega del último TP solicitado. En la cual se solicita la utilización de una estructura de datos tipo pila, cola, lista enlazada.

## Consigna
```
Desarrollar un programa en lenguaje de programación Python según la siguiente consigna:

En un supermercado dispone en la salida de 3 cajas para pagar, una para Prioridad (embarazadas y 
ancianos), otra para Discapacitados, y otra Normal (sin prioridad). 
En el local hay 6 carritos de compra. 

Escribir un programa que simule el comportamiento, siguiendo las siguientes reglas:

Implementar los carritos en un PILA (sobre una lista enlazada), teniendo en claro las operaciones 
posibles sobre este tipo de estructura de datos. Al principio la pila deberá estar llena con todos los 
carritos, cada carrito debe tener una identificación, además debe conocer a que cliente tiene y en 
que cola se encuentra, según corresponda cada caso. Esto debe estar en una opción del Menú, la 
posibilidad de conocer el estado completo de un carrito según su identificación.

Cuando ingresa una persona se debe indicar si la condición especial (Embarazada - Anciano - 
discapacitado - normal)

Los carritos se entregan o usan según prioridad, primero embarazadas, segundo ancianos, tercero 
discapacitado, y por último el normal.

De acuerdo a la condición del Cliente, va a la cola correspondiente, con la excepción de que si las 
colas especiales están vacías, uno normal puede ir a cualquiera de ellas, la que tenga menos Clientes
en espera.

Ningún cliente abandona el supermercado sin pasar por alguna de las colas de las cajas, cuando un 
cliente finaliza su compra (luego de haberle asignado un carrito), se coloca en la cola de la caja 
correspondiente y no se cambia de cola.

En el momento en que un cliente paga en la caja (primero en la cola), el carro de la compra que 
tiene queda disponible (se vuelve a apilar).

Representar las opciones de ingresar un cliente, cobrar en caja, mostrar estado de colas de cajas y 
mostrar el estado de los carritos y cola de espera de carritos. 

Cada vez que se ejecuta una opción de ingreso de cliente o cobro en caja, se actualizan todas las 
colas.

Secuencia 1: cuando ingresa un cliente mira si hay carritos disponibles, si hay toma uno (según su 
condición), caso contrario queda en cola de espera de carros.

Secuencia 2: cuando se paga en caja, se libera la cola de caja y se liberan esos carritos. Los que 
están con carritos pasan a las cajas (manteniendo el orden de ingreso). Los que están en cola de 
espera de carritos pasan a tomar los disponibles.
Luego de cualquier secuencia, deberá limpiarse la pantalla, mostrar el estado general y luego de 
presionar una tecla deberá limpiarse la pantalla y mostrar el menú nuevamente.
Hacer un menú con las opciones de ejecución mencionadas. Todas las opciones deben estar en un 

Menú, incluyendo la opción para finalizar la ejecución.
1- Ingreso de Cliente
2- Cobros en Caja
3- Estado de un Carrito
4- Estado General del Supermercado
5- Salir

Incluir comentarios en los métodos.

Desarrollar los casos de pruebas completos en un documento, indicar que punto se ejecuta, qué 
ingresa y como quedan las colas.
```

Autores
- Usui, José Fernando
- Rojas, Luciana