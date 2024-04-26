import sqlite3

cnx=sqlite3.connect('Tablas.db')


cursor=cnx.cursor()

#crear base de datos 
products_table='''
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY, 
        name_producto TEXT NOT NULL,
        Cantidad TEXT NOT NULL,
        id_categoria INTEGER 
    );
'''

categories_table='''
    CREATE TABLE IF NOT EXISTS categorias(
        id INTEGER PRIMARY KEY, 
        name_categoria TEXT NOT NULL
    );
'''
usuarios_tabla='''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY, 
        Nombre TEXT NOT NULL,
        Apellido TEXT NOT NULL,
        Cedula TEXT NOT NULL,
        Correo TEXT NOT NULL,
        Contraseña TEXT NOT NULL
    );
'''

cursor.execute(products_table)
cursor.execute(categories_table)
cnx.commit() #crea la tabla 