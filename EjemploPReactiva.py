import rx
from rx import operators as ops

'''
 A partir de un observable que contiene  una secuencia de tuplas (nombre, edad), retornar hasta aquellas tuplas
 cuyo valor nombre empiece con l, cuya longitud sea mayor o igual a 5 y cuya edad sea menor a 55.
 Presentar las tuplas que cumplan con la condición y si no hay ningún error presentar al final un mensaje de éxito
'''

observado = rx.of(("Lucia", 45), ("jorge", 22), ("lana", 82), ("LILIANA", 18), ("Andrea", 14), ("leandro", 45),
               ("carlos", 10), ("Josue", 28), ("Laura", 66), ("Lebron", 34)) # Observable con las tuplas (nombre, edad)

observador = observado.pipe(  # Observador que manipulará las tuplas con .pipe para filtrar según los parámetros requeridos
    ops.map(lambda e: (e[0].lower(), e[1])), # Operador .map para transformar los nombres de las tuplas a minúscula
    ops.filter(lambda e: e[0][0] == "l"), # Operador .filter para obtener tuplas con nombres que empiecen en "l"
    ops.filter(lambda e: len(e[0]) >= 5), # Operador .filter para obtener tuplas con nombres que sean mas largos que 5
    ops.take_while(lambda e: e[1] < 55) # Operador take_while para obtener hasta las tuplas cuya edad sea menor a 55
)

suscriptor = observador.subscribe( # Suscriptor que permitirá la impresión del observador
    on_next=lambda i: print(i), # Impresión de cada tupla filtrada y manipulada
    on_error=lambda e: print("Error: ${e}"), # Impresión en caso de error
    on_completed=lambda: print(f"Datos filtrados con éxito!") # Impresión de éxito
)

suscriptor.dispose() # Método dispose para terminar la suscripcipon al observable