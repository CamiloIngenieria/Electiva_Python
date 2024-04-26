import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from formularios.form_reportes_design import FormularioReportesDesign
from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign
from formularios.form_info_design import FormularioInfoDesign
from formularios.form_crearcategorias_design import FormularioCrearCategoriasDesign
from formularios.form_crearproductos_design import FormularioCrearProductosDesign
from formularios.form_listarcategorias_design import FormularioListarCategoriasDesign
from formularios.form_listarproductos_design import FormularioListarProductosDesign
import sys

class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./imagenes/logo.png", (600, 500))
        self.perfil = util_img.leer_imagen("./imagenes/logo2.png", (100, 100))
        self.img_sitio_construccion = util_img.leer_imagen("./imagenes/sitio_construccion.png", (200, 200))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Universidad Cesmag')
        self.iconbitmap("./imagenes/logo.png")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
         # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Almacen UCESMAG")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelTitulo = tk.Label(self.barra_superior, text="camilo@unicesmag.edu.co")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
    
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
         # Etiqueta de perfil
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        self.buttonDashBoard = tk.Button(self.menu_lateral)        
        self.buttonCrearCategoria = tk.Button(self.menu_lateral)        
        self.buttonCrearProducto= tk.Button(self.menu_lateral)
        self.buttonListarCategorias = tk.Button(self.menu_lateral)        
        self.buttonListarProductos = tk.Button(self.menu_lateral)        
        self.buttonReportes = tk.Button(self.menu_lateral)        
        self.buttonConfiguraciones = tk.Button(self.menu_lateral)
        self.buttonSalir = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Dashboard", "\uf113", self.buttonDashBoard,self.abrir_panel_en_construccion),
            ("Crear Categoria", "\uf113", self.buttonCrearCategoria,self.abrir_panel_crearcategorias),
            ("Crear Producto", "\uf113", self.buttonCrearProducto,self.abrir_panel_crearproductos),
            ("Listar Categorias", "\uf113", self.buttonListarCategorias,self.abrir_panel_listarcategorias),
            ("Listar Productos", "\uf113", self.buttonListarProductos,self.abrir_panel_listarproductos),
            ("Reportes", "\uf113", self.buttonReportes,self.abrir_panel_reportes),
            ("Configuraciones", "\uf113", self.buttonConfiguraciones,self.abrir_panel_info),
            ("Cerrar Sesion", "\uf013", self.buttonSalir,self.cerrar_sesion)
        ]

        for text, icon, button,comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu,comando)                    
    
    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo,bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)        
  
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,command = comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')
    # Nuevo
    
    def abrir_panel_crearcategorias(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioCrearCategoriasDesign(self.cuerpo_principal,self.img_sitio_construccion)
   
    def abrir_panel_crearproductos(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioCrearProductosDesign(self.cuerpo_principal,self.img_sitio_construccion)

    def abrir_panel_listarcategorias(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioListarCategoriasDesign(self.cuerpo_principal,self.img_sitio_construccion)

    def abrir_panel_listarproductos(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioListarProductosDesign(self.cuerpo_principal,self.img_sitio_construccion)

    def abrir_panel_reportes(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        FormularioReportesDesign(self.cuerpo_principal,self.img_sitio_construccion)   
        
    def abrir_panel_en_construccion(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        FormularioSitioConstruccionDesign(self.cuerpo_principal,self.img_sitio_construccion) 

    def abrir_panel_info(self):           
        FormularioInfoDesign() 

    def cerrar_sesion(self):           
        sys.exit()     

    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()