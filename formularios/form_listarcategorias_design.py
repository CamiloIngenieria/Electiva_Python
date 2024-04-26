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

 
class FormularioListarCategoriasDesign():
    db_name= 'Tablas.db'

    def __init__(self, panel_principal, logo):

        # Crear paneles: barra superior
        self.barra_superior = tk.Frame( panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False) 

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame( panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        # Primer Label con texto
        self.labelTitulo = tk.Label(self.barra_superior, text="Lista de Categorias")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.six = ttk.Treeview(self.barra_inferior,height = 10, columns = 1)
        self.six.pack(fill=tk.X, padx=20,pady=5) 
        self.six.heading('#0', text = 'Id', anchor = CENTER)
        self.six.heading('#1', text = 'Nombre', anchor = CENTER)

        self.eliminar = tk.Button(self.barra_inferior,text="ELIMINAR",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.Eliminar_Categoria)
        self.eliminar.pack(fill=tk.X, padx=20,pady=15) 
        self.get_categorias()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_categorias(self): 
        # Limpiar tabla
        records = self.six.get_children()
        for element in records:
            self.six.delete(element)
        # Obtener datos
        query = 'SELECT * FROM categorias'
        db_rows = self.run_query(query)
        # Rellenar datos
        for row in db_rows:
            self.six.insert('', 0, text=row[0],values=row[1])

    def Eliminar_Categoria(self):
        try:
           self.six.item(self.six.selection())['text'][0]
        except IndexError as e:
            return
        nombre = self.six.item(self.six.selection())['text']
        query = 'DELETE FROM categorias WHERE name_categoria = ?'
        self.run_query(query, (nombre, ))
        self.get_categorias()

    