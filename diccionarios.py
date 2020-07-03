
# el diccionario es un tipo de dato que permite generar registros, se accede a por las llaves+ valor
#se pueden generar listas de diccionarios, solamente que se debe de acceder a las listas por medio de un indice y despues la llave a la que queremos acceder.

dato = {}
dato['nombre'] = input ("ingresar un nuevo nombre:")
dato['direccion']=input ("ingresa la direccion")
dato['correo']=input ("ingresa la correo")
for llave, valor in dato.items():
    print(llave,valor)
#clases y objetos sintaxis class nombre de la clase: ...init es la palabra reservada para el contructor 
# el primer argumento es self, y elistar los atributos del objeto se instancia se hae nombre del objeto = clase (atributos)
#  ejemplo funciones clases y objetos

