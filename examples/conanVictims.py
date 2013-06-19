#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
# Creamos el cursor, pero especificando que sea de la subclase DictCursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
# Insertamos un par de registros
query=""
id = 0
inval = False
iden = 1

for i in range(0,9):
     name = raw_input("Nombre: ")
     if (name==""):
        print "Valor de nombre invalido."
        inval = True
     profesion = raw_input("Profesión: ")
     if (profesion==""):
        print "Valor de profesión invalido."
        inval = True
     muerte = raw_input("Muerte: ")
     if (muerte==""):
        print "Valor de muerte invalido."
        inval = True
     if(inval):
         print "No se insertará la tupla"
     else:
         query = "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (%i,'%s','%s','%s');" %(iden,name,profesion,muerte)
         iden+=1
         micursor.execute(query)
     inval = False

if(query!=""):
    Conexion.commit()

opt = raw_input("¿Desea mostrar los registros existentes? s/n :");
if(opt=="s"):
    query= "SELECT * FROM Victimas WHERE 1;"
    micursor.execute(query)
# Obtenemos el resultado con fetchall
    registros= micursor.fetchall()
    for registro in registros:
# ... imprimimos el registro..
        print "Id: %s" %registro["id"]
        print "Nombre: %s" %registro["Nombre"]
        print "Profesion: %s" %registro["Profesion"]
        print "Muerte: %s" %registro["Muerte"]
        print
    
