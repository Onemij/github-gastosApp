from tkinter import Frame, Tk, Label, Button, Entry, messagebox
from tkinter.constants import RIGHT, LEFT
from tkinter.ttk import Combobox, Treeview
from new_constants import sub_categories_list, categories_list
from tkcalendar import Calendar
import base_datos as db
from fechas import obtener_fecha
from datetime import datetime
from detail_window import DetailWindow


class GastosApp:
    
    def __init__(self) -> None:
        db.create_table()
        self.window = Tk()
        self.init_widgets()
        self.frame_ingresos.bind('<Button-1>', lambda x: self.show_categories_list("ingreso"))
        self.frame_gastos.bind('<Button-1>', lambda x: self.show_categories_list("gasto"))


    def init_widgets(self):        
        self.frame_master_arriba = Frame(self.window)
        self.frame_master_abajo = Frame(self.window)
        self.frame_ingresos = Frame(self.frame_master_arriba)
        self.frame_gastos = Frame(self.frame_master_arriba)
        self.l1 = Label(self.frame_ingresos, font=("Arial Bold", 12), text=f'Ingresos de {datetime.now().strftime("%B")}')
        self.l2 = Label(self.frame_ingresos, font=("Arial Bold", 12), text=str(db.get_total("ingreso")))
        self.l3 = Label(self.frame_gastos, font=("Arial Bold", 12), text=f'Gastos de {datetime.now().strftime("%B")}')
        self.l4 = Label(self.frame_gastos, font=("Arial Bold", 12), text=str(db.get_total("gasto")))
        self.treebox = Treeview(self.frame_master_arriba, columns=("Movimiento", "Categoría", "Subcategoría"))
        self.treebox_previous_month_button = Button(self.frame_master_arriba, text="Mes anterior", height = 2, width = 20)
        self.treebox_back_button = Button(self.frame_master_arriba, text="Atrás", height = 2, width = 20)
        self.treebox_next_month_button = Button(self.frame_master_arriba, text="Siguiente mes", height = 2, width = 20)
        self.cal = Calendar(self.frame_master_abajo)
        self.entry = Entry(self.frame_master_abajo, width=20)
        self.combo_categories = Combobox(self.frame_master_abajo, state="readonly", values=categories_list)
        self.combo_sub_categories = Combobox(self.frame_master_abajo, state="readonly", values=sub_categories_list["Nómina"])

        self.btn_ingreso = Button(self.frame_master_abajo, text="Ingreso", height = 2, width = 20, command= lambda: self.movimiento_clicked("ingreso"))
        self.btn_gasto = Button(self.frame_master_abajo, text="Gasto", height = 2, width = 20, command= lambda: self.movimiento_clicked("gasto"))
        self.btn_devolucion = Button(self.frame_master_abajo, text="Devolución", height = 2, width = 20, command= lambda: self.movimiento_clicked("devolucion"))


        self.category_buttons_ingreso, self.category_buttons_gasto = {}, {}

        self.category_buttons_ingreso["Nómina"] = Button(self.frame_ingresos, text="Nómina", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Nómina", tipo="ingreso"))
        self.category_buttons_gasto["Nómina"] = Button(self.frame_gastos, text="Nómina", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Nómina", tipo="gasto"))

        self.category_buttons_ingreso["Ingresos no nómina"] = Button(self.frame_ingresos, text="Ingresos no nómina", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Ingresos no nómina", tipo="ingreso"))
        self.category_buttons_gasto["Ingresos no nómina"] = Button(self.frame_gastos, text="Ingresos no nómina", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Ingresos no nómina", tipo="gasto"))

        self.category_buttons_ingreso["Transportes y viajes"] = Button(self.frame_ingresos, text="Transportes y viajes", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Transportes y viajes", tipo="ingreso"))
        self.category_buttons_gasto["Transportes y viajes"] = Button(self.frame_gastos, text="Transportes y viajes", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="NómTransportes y viajesina", tipo="gasto"))

        self.category_buttons_ingreso["Seguros"] = Button(self.frame_ingresos, text="Seguros", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Seguros", tipo="ingreso"))
        self.category_buttons_gasto["Seguros"] = Button(self.frame_gastos, text="Seguros", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Seguros", tipo="gasto"))

        self.category_buttons_ingreso["Salud"] = Button(self.frame_ingresos, text="Salud", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Salud", tipo="ingreso"))
        self.category_buttons_gasto["Salud"] = Button(self.frame_gastos, text="Salud", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Salud", tipo="gasto"))

        self.category_buttons_ingreso["Ocio"] = Button(self.frame_ingresos, text="Ocio", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Ocio", tipo="ingreso"))
        self.category_buttons_gasto["Ocio"] = Button(self.frame_gastos, text="Ocio", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Ocio", tipo="gasto"))

        self.category_buttons_ingreso["Casa"] = Button(self.frame_ingresos, text="Casa", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Casa", tipo="ingreso"))
        self.category_buttons_gasto["Casa"] = Button(self.frame_gastos, text="Casa", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Casa", tipo="gasto"))

        self.category_buttons_ingreso["Efectivo y pagos"] = Button(self.frame_ingresos, text="Efectivo y pagos", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Efectivo y pagos", tipo="ingreso"))
        self.category_buttons_gasto["Efectivo y pagos"] = Button(self.frame_gastos, text="Efectivo y pagos", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Efectivo y pagos", tipo="gasto"))

        self.category_buttons_ingreso["Educación"] = Button(self.frame_ingresos, text="Educación", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Educación", tipo="ingreso"))
        self.category_buttons_gasto["Educación"] = Button(self.frame_gastos, text="Educación", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Educación", tipo="gasto"))

        self.category_buttons_ingreso["Compras"] = Button(self.frame_ingresos, text="Compras", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Compras", tipo="ingreso"))
        self.category_buttons_gasto["Compras"] = Button(self.frame_gastos, text="Compras", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Compras", tipo="gasto"))

        self.category_buttons_ingreso["Otros"] = Button(self.frame_ingresos, text="Otros", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Otros", tipo="ingreso"))
        self.category_buttons_gasto["Otros"] = Button(self.frame_gastos, text="Otros", padx=5,
            pady=5, width=15, height=2, command=lambda:self.detailed_view(category="Otros", tipo="gasto"))


        self.category_buttons_ingreso["Atras"] = Button(self.frame_ingresos, text="Atrás",
        command=lambda: self.show_categories_list(back=True, tipo="ingreso"), padx=5, pady=5, width=15, height=2)
        self.category_buttons_gasto["Atras"] = Button(self.frame_gastos, text="Atrás", 
        command=lambda: self.show_categories_list(back=True, tipo="gasto"), padx=5, pady=5, width=15, height=2)
        self.window.title("GastosApp")
        self.window.state("zoomed")
        self.window.configure(bg='#a1f28e', pady=20, padx=20)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.frame_master_arriba.config(bg='#dfcc12', width=480, height=50, padx=50, pady=10)
        self.frame_master_arriba.grid(row=0, column=0, columnspan=3, pady=10)
        self.frame_ingresos.config(bg='#8cce7c', width=480, height=50)
        self.frame_gastos.config(bg='#8cce7c', width=480, height=50)
        self.frame_master_abajo.config(bg='#8cce7c', width=480, height=50, padx=10, pady=10)
        self.frame_master_abajo.grid(row=2, column=0, columnspan=3, pady=10)
        self.l1.config(width=20, bg='#8cce7c', fg='#fff')
        self.l2.config(width=10, bg='#8cce7c', fg='#fff')
        self.l3.config(width=20, bg='#8cce7c', fg='#fff')
        self.l4.config(width=10, bg='#8cce7c', fg='#fff')
        self.treebox.heading("#0", text="Fecha")
        self.treebox.heading("Movimiento", text="Movimiento")
        self.treebox.heading("Categoría", text="Categoría")
        self.treebox.heading("Subcategoría", text="Subcategoría")
        self.treebox_previous_month_button.config(bg='#8cce7c', activebackground='#76a969')
        self.treebox_back_button.config(bg='#8cce7c', activebackground='#76a969')
        self.treebox_next_month_button.config(bg='#8cce7c', activebackground='#76a969')
        self.btn_ingreso.config(activebackground='#fff')
        self.btn_gasto.config(activebackground='#fff')
        self.btn_devolucion.config(activebackground='#fff')
        self.combo_categories.current(0)
        self.combo_categories.bind('<<ComboboxSelected>>', self.select_subcategory)
        self.combo_sub_categories.current(0)

    def pack_frames_arriba_inicio(self):
        '''Coloca (grid) en el Frame MASTER de arriba todos los elementos que se necesitan al inicio del programa'''

        self.frame_ingresos.grid(row=0, column=0, columnspan=3, pady=5)
        self.frame_gastos.grid(row=2, column=0, columnspan=3, pady=5)
        self.l1.grid(row=0, column=0, pady = 10, padx = 50)
        self.l2.grid(row=0, column=2, pady = 10, padx = 50)
        self.l3.grid(row=0, column=0, pady = 10, padx = 50)
        self.l4.grid(row=0, column=2, pady = 10, padx = 50)

    def pack_frames_abajo_inicio(self):
        '''Coloca (grid) en el Frame MASTER de abajo todos los elementos que se necesitan al inicio del programa
        - Parámetros: ninguno
        - Devuelve: None'''

        self.entry.grid(row=40, column=0, pady=20)
        self.combo_categories.grid(row=40, column=1)
        self.combo_sub_categories.grid(row=40, column=2)
        self.btn_ingreso.grid(row=50, column=0)
        self.btn_gasto.grid(row=50, column=1)
        self.btn_devolucion.grid(row=50, column=2)
        self.cal.grid(row=10, column=1, pady=20)
    
    def select_subcategory(self, e):
        if self.combo_categories.get() == "Nómina":
            self.combo_sub_categories.config(values=sub_categories_list["Nómina"])
        if self.combo_categories.get() == "Ingresos no nómina":
            self.combo_sub_categories.config(values=sub_categories_list["Ingresos no nómina"])
        if self.combo_categories.get() == "Transportes y viajes":
            self.combo_sub_categories.config(values=sub_categories_list["Transportes y viajes"])
        if self.combo_categories.get() == "Seguros":
            self.combo_sub_categories.config(values=sub_categories_list["Seguros"])
        if self.combo_categories.get() == "Salud":
            self.combo_sub_categories.config(values=sub_categories_list["Salud"])
        if self.combo_categories.get() == "Ocio":
            self.combo_sub_categories.config(values=sub_categories_list["Ocio"])
        if self.combo_categories.get() == "Casa":
            self.combo_sub_categories.config(values=sub_categories_list["Casa"])
        if self.combo_categories.get() == "Efectivo y pagos":
            self.combo_sub_categories.config(values=sub_categories_list["Efectivo y pagos"])
        if self.combo_categories.get() == "Educación":
            self.combo_sub_categories.config(values=sub_categories_list["Educación"])
        if self.combo_categories.get() == "Compras":
            self.combo_sub_categories.config(values=sub_categories_list["Compras"])
        if self.combo_categories.get() == "Otros":
            self.combo_sub_categories.config(values=sub_categories_list["Otros"])

        self.combo_sub_categories.current(0)
    
    def initialize(self):
        '''Llama a los métodos pack_frames_abajo_inicio() y pack_frames_arriba_inicio() para colocar todos los elementos
            necesarios en la aplicación.
        - Parámetros: ninguno
        - Devuelve: None'''

        self.pack_frames_abajo_inicio()
        self.pack_frames_arriba_inicio()
    
    def run(self):
        '''Llama al método "mainloop" de la ventana principal, iniciando la aplicación.
        - Parámetros: ninguno
        - Devuelve: None'''

        self.window.mainloop()
    
    def movimiento_clicked(self, tipo): 
        fecha = self.cal.get_date()
        movimiento = self.entry.get()
        category = self.combo_categories.get()
        subcategory = self.combo_sub_categories.get()
        respuesta = messagebox.askyesno(message=f"¿Confirmar {tipo} de {movimiento} €?\n\n\nCategoría: {category}\nSubcategoría: {subcategory}", title="Añadir movimiento")

        if respuesta:
            try:   
                float_movimiento = float(movimiento.replace(",","."))
                
                db.data_entry(obtener_fecha(fecha).strftime("%Y-%m-%d"), tipo, float_movimiento, category, subcategory)
                
                #self.lbl_movimiento.grid(row=4, column=1, pady=10)
                #self.lbl_movimiento.after(750, self.lbl_movimiento.grid_forget)
                self.entry.delete(0,"end")
                #self.update_treebox(tipo, new_movement=True)
                self.l2.config(text=str(db.get_total("ingreso")))
                self.l4.config(text=str(db.get_total("gasto")))
        

            except:
                self.messagebox.showwarning(message="El valor no es correcto", title="Error")

    def show_categories_list(self, tipo, back=False):
        
        if tipo == "ingreso":
            frame = self.frame_ingresos
            botones = self.category_buttons_ingreso
        elif tipo == "gasto":
            frame = self.frame_gastos
            botones = self.category_buttons_gasto

        if not back:
            i, j = 0, 0
            for widget in frame.winfo_children():
                widget.grid_forget()
            for button in botones:
                botones[button].grid(row=j, column=i%3, padx=10, pady=10)
                i += 1
                if i%3 == 0:
                    j += 1
        else:
            for widget in frame.winfo_children():
                widget.grid_forget()
            
            self.pack_frames_arriba_inicio()
            
    
    def detailed_view(self, category, tipo):
        detailed_view = DetailWindow(category=category, tipo=tipo)
        print(category, tipo)
        detailed_view.detail()
        detailed_view.run()