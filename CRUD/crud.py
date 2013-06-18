#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gi.repository import Gtk
import MySQLdb

class DBManager:

    def __init__(self):
        self.conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
        self.micursor = self.conexion.cursor(MySQLdb.cursors.DictCursor)
        self.query="""
        create table if not exists Personajes( 
        id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
        nombre VARCHAR(100) , 
        casa VARCHAR(100), 
        padre VARCHAR(100),
        ciudad VARCHAR(100),
        muerte VARCHAR(100));
        """
        self.micursor.execute(self.query)
        self.conexion.commit()
        #self.insert('Robb','Stark','Eddard','Winterfell','Los gemelos')
        #print self.select(2)
        #self.update('Robb','Stark','Eddard','Riverrun','Los gemelos',2)
#        print self.select(2)
        #print self.delete(2)
    def insert(self,nombre,casa,padre,ciudad,muerte):
        self.query = "INSERT INTO Personajes (nombre,casa,padre,ciudad,muerte) VALUES ('%s','%s','%s','%s','%s');" %(nombre,casa,padre,ciudad,muerte)
        self.micursor.execute(self.query)
        self.conexion.commit()

    def update(self,nombre,casa,padre,ciudad,muerte,iden):
        self.query = " UPDATE Personajes SET nombre = '%s',casa = '%s', padre = '%s', ciudad = '%s', muerte = '%s' WHERE id = %i; " % (nombre,casa,padre,ciudad,muerte,iden)
        self.micursor.execute(self.query)
        self.conexion.commit()

    def select(self,iden):
        self.query= "SELECT * FROM Personajes WHERE id = %i;" % iden
        self.micursor.execute(self.query)
        registro = self.micursor.fetchone()
        return (registro["id"],registro["nombre"],registro["casa"],registro["padre"],registro["ciudad"],registro["muerte"])
        
    def delete(self,iden):
        self.query= "DELETE FROM Personajes WHERE id = %i;" % iden
        self.micursor.execute(self.query)
        self.conexion.commit()



db2=DBManager()

class Handler:
        
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
                
    def onMenuInsert(self,*args):
        print "insert"
        tupla = self.__getArgs(*args)
        db2.insert(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5])

    def onMenuSelect(self,*args):
        print "select"
        self.__getArgs(*args)
        iden = int(self.__getArgs(*args)[0])
        print db2.select(iden)
        tupla = self.__getArgs(*args)
        self.__setText(args[0],tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5])

    def onMenuUpdate(self,*args):
        print "update"
        tupla = self.__getArgs(*args)
        db2.update(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],int(tupla[0]))

    def onMenuDelete(self,*args):
        print "delete"
        db2.delete(int(self.__getArgs(*args)[0]))

    def onHelpMenu(self,*args):
        print "help"
        
    def __getArgs(self,*args):
        iden = args[0].get_child_at(1,0).get_text()
        nombre = args[0].get_child_at(1,1).get_text()
        casa = args[0].get_child_at(1,2).get_text()
        padre = args[0].get_child_at(1,3).get_text()
        ciudad = args[0].get_child_at(1,4).get_text()
        muerte = args[0].get_child_at(1,5).get_text()
        return (iden,nombre,casa,padre,ciudad,muerte)

    def __setText(self,grid,iden,nombre,casa,padre,ciudad,muerte):
        grid.get_child_at(1,0).set_text(iden)
        grid.get_child_at(1,1).set_text(nombre)
        grid.get_child_at(1,2).set_text(casa)
        grid.get_child_at(1,3).set_text(padre)
        grid.get_child_at(1,4).set_text(ciudad)
        grid.get_child_at(1,5).set_text(muerte)


class Crud_GUI:
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("interface.glade")
        self.builder.connect_signals(Handler())
        #self.builder.connect_signals("destroy", gtk.main_quit) 

 
        self.window = self.builder.get_object("window1")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()


    def __del__(self,*args):
        print "Deleted"
        #Gtk.main_quit(*args)


def main():
        window = Crud_GUI()
        Gtk.main()

        return 0

if __name__ == '__main__':
        main()

