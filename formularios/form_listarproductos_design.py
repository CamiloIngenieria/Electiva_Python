import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from config import  COLOR_CUERPO_PRINCIPAL
from Tablas import *
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sqlite3

 
class FormularioListarProductosDesign():
    db_name= 'Tablas.db'

    def __init__(self, panel_principal, logo):

        # Crear paneles: barra superior
        self.barra_superior = tk.Frame( panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False) 

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame( panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        # Primer Label con texto
        self.labelTitulo = tk.Label(self.barra_superior, text="Lista de Productos")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.six = ttk.Treeview(self.barra_inferior,height = 10, columns =[f"#{n}" for n in range(1,3)])
        self.six.pack(fill=tk.X, padx=20,pady=5) 
        self.six.heading('#0', text = 'Nombre', anchor = CENTER)
        self.six.heading('#1', text = 'Cantidad', anchor = CENTER)
        self.six.heading('#2', text = 'Categoria', anchor = CENTER)

        self.eliminar = tk.Button(self.barra_inferior,text="ELIMINAR",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.Eliminar_Producto)
        self.eliminar.pack(fill=tk.X, padx=20,pady=15) 
        self.get_productos()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_productos(self): 
        # Limpiar tabla
        records = self.six.get_children()
        for element in records:
            self.six.delete(element)
        # Obtener datos
        query = 'SELECT * FROM productos'
        db_rows = self.run_query(query)
        # Rellenar datos
        for row in db_rows:
            self.six.insert('', 0, text=row[1], values=(row[2],row[3]))

    def Eliminar_Producto(self):
        try:
           self.six.item(self.six.selection())['text'][0]
        except IndexError as e:
            return
        nombre = self.six.item(self.six.selection())['text']
        query = 'DELETE FROM productos WHERE name_producto = ?'
        self.run_query(query, (nombre, ))
        self.get_productos()