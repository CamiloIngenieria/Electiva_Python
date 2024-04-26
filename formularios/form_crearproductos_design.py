import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from config import  COLOR_CUERPO_PRINCIPAL
from Tablas import *


class FormularioCrearProductosDesign():

    def __init__(self, panel_principal, logo):

        # Crear paneles: barra superior
        self.barra_superior = tk.Frame( panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False) 

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame( panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)  

        # Primer Label con texto
        self.labelTitulo = tk.Label(self.barra_superior, text="Crear Productos")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.labelNombre = tk.Label(self.barra_inferior, text="Nombre")
        self.labelNombre.config(fg="#222d33", font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.labelNombre.pack(fill=tk.X, padx=20,pady=5)
        self.nombreproducto = ttk.Entry(self.barra_inferior, font=('Times', 14))
        self.nombreproducto.pack(fill=tk.X, padx=20,pady=10)

        self.labelCantidad = tk.Label(self.barra_inferior, text="Cantidad")
        self.labelCantidad.config(fg="#222d33", font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.labelCantidad.pack(fill=tk.X, padx=20,pady=15)
        self.cantidad = ttk.Entry(self.barra_inferior, font=('Times', 14))
        self.cantidad.pack(fill=tk.X, padx=20,pady=20)

        self.labelCategoria = tk.Label(self.barra_inferior, text="Categoria")
        self.labelCategoria.config(fg="#222d33", font=("Roboto", 15), bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.labelCategoria.pack(fill=tk.X, padx=20,pady=25)
        self.categoria = ttk.Entry(self.barra_inferior, font=('Times', 14))
        self.categoria.pack(fill=tk.X, padx=20,pady=30)


        self.registrar = tk.Button(self.barra_inferior,text="Agregar Producto",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.registrar_producto)
        self.registrar.pack(fill=tk.X, padx=20,pady=35) 

    def registrar_producto(self):
       cursor.execute(f"INSERT INTO productos (name_producto, cantidad,id_categoria) VALUES('{self.nombreproducto.get()}','{self.cantidad.get()}','{self.categoria.get()}')")        
       cnx.commit() # permite que los datos se guarden en la base de datos