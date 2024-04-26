import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from config import  COLOR_CUERPO_PRINCIPAL
from Tablas import *


class FormularioCrearCategoriasDesign():

    def __init__(self, panel_principal, logo):

        # Crear paneles: barra superior
        self.barra_superior = tk.Frame( panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False) 

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame( panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)  

        # Primer Label con texto
        self.labelTitulo = tk.Label(self.barra_superior, text="Crear Categoria")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.labelNombre = tk.Label(self.barra_inferior, text="Nombre")
        self.labelNombre.config(fg="#222d33", font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.labelNombre.pack(fill=tk.X, padx=20,pady=5)

        self.nombrecategoria = ttk.Entry(self.barra_inferior, font=('Times', 14))
        self.nombrecategoria.pack(fill=tk.X, padx=20,pady=10)

        self.registrar = tk.Button(self.barra_inferior,text="Agregar Categoria",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.registrar_categoria)
        self.registrar.pack(fill=tk.X, padx=20,pady=20) 

    def registrar_categoria(self):
        cursor.execute(f"INSERT INTO categorias (name_categoria) VALUES('{self.nombrecategoria.get()}')")
        cnx.commit() # permite que los datos se guarden en la base de datos


