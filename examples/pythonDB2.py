#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
# Creamos el cursor
micursor = Conexion.cursor()
# Insertamos algunos registros (de forma cutre e ineficiente) para tener con qué trabajar
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (3, \"Bestia del Pantano\",\"Monstruo\",\"Destripado\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (4, \"Serpiente\",\"Monstruo\",\"Destripado\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (5, \"Scerdote maligno\",\"Monstruo\",\"Desmembramiento a espada\");"
micursor.execute(query)
# Hacemos un commit, por si las moscas
Conexion.commit()
# Ahora vamos a hacer un SELECT
query= "SELECT * FROM Victimas WHERE 1;"
micursor.execute(query)
# Obtenemos el resultado con fetchmany
registros= micursor.fetchmany(2)
# para cada lista retornada (de 2 registros)
while (registros):
# recorremos la lista...
    for registro in registros:
# ... mprimimos el registro...
        print registro
# ...y recargamos los registros dentro del bucle, si quedan
    print
    registros= micursor.fetchmany(2)
# Esto que sigue es para borrar el contenido de la base de datos,
# y que no se nos acumule al ir haciendo pruebas
query= "DELETE FROM Victimas WHERE 1;"
micursor.execute(query)

