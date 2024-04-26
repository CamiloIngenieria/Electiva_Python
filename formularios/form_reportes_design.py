import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import matplotlib.pyplot as pt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
from Tablas import *
from config import  COLOR_CUERPO_PRINCIPAL


class FormularioReportesDesign():
      
    def __init__(self, panel_principal, logo):

        # Crear paneles: barra superior
        self.barra_superior = tk.Frame( panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False) 

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame( panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)  

        # Primer Label con texto
        self.labelTitulo = tk.Label(self.barra_superior, text="Generar Reportes")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.labelSeleccion = tk.Label(self.barra_inferior, text="Seleccione el Reporte")
        self.labelSeleccion.config(fg="#222d33", font=("Roboto", 20), bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.labelSeleccion.pack(fill=tk.X, padx=20,pady=5)

        self.generar1 = tk.Button(self.barra_inferior,text="Total Productos",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.reporte1)
        self.generar1.pack(fill=tk.X, padx=20,pady=10) 
        self.generar2 = tk.Button(self.barra_inferior,text="Total Por Categoria",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.reporte2)
        self.generar2.pack(fill=tk.X, padx=20,pady=15) 
        self.salir = tk.Button(self.barra_inferior,text="Salir",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.salir)
        self.salir.pack(fill=tk.X, padx=20,pady=15) 

    def reporte1 (self):           
        query_reporte1='''
            SELECT 
                c.name_categoria, 
                SUM(p.cantidad) as total_productos
            FROM 
                productos p INNER JOIN 
                    categorias c
                ON p.id_categoria = c.id
            GROUP BY 
                c.name_categoria 
        '''
        cursor.execute(query_reporte1)
        data=cursor.fetchall()
        # Preparar los datos para la gráfica
        categorias = [resultado[0] for resultado in data]
        total_productos = [resultado[1] for resultado in data]

        # Crear la gráfica
        pt.figure(figsize=(10, 6))
        pt.bar(categorias, total_productos, color='skyblue')
        pt.xlabel('Categorías')
        pt.ylabel('Total de productos')
        pt.title('Total de productos por categoría')
        pt.xticks(rotation=45)
        pt.tight_layout()
        #pip freeze > requirements.txt
        # Mostrar la gráfica
        pt.show() 

    def reporte2 (self):           
        query_reporte2='''
            SELECT * FROM productos
        '''
        cursor.execute(query_reporte2)
        data=cursor.fetchall()
        # Preparar los datos para la gráfica
        print(data)
        total_productos = [resultado[0] for resultado in data]
        productos = [resultado[1] for resultado in data]


        # Crear la gráfica
        pt.figure(figsize=(10, 6))
        pt.bar(productos, total_productos, color='skyblue')
        pt.xlabel('Productos')
        pt.ylabel('Total de productos')
        pt.title('Total de productos por categoría')
        pt.xticks(rotation=45)
        pt.tight_layout()
        #pip freeze > requirements.txt
        # Mostrar la gráfica
        pt.show()        
    def salir (self):
        print('Nos Vemos')
        sys.exit()           


        