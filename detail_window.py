from tkinter import Frame, Tk, Label, Button, Entry, messagebox
from base_datos import get_movs

class DetailWindow():
    
    def __init__(self, category="Nómina", tipo="ingreso") -> None:
        self.root = Tk()
        self.root.title(f"{tipo}s de la categoría {category}")
        self.root.geometry("700x700")
        self.root.configure(bg='#a1f28e', pady=20, padx=20)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.category = category
        self.tipo = tipo

        self.detail_lbl = Label(self.root, text=category.capitalize())
        self.detail_lbl.pack() 


    
    def run(self):
        '''Llama al método "mainloop" de la ventana principal, iniciando la aplicación.
        - Parámetros: ninguno
        - Devuelve: None'''

        self.root.mainloop()
    
    def detail(self):
        movs = get_movs(tipo=self.tipo, category=self.category)
        text = "\n\nMovimientos:\n"
        for mov in movs:
            text += str(mov[2]) + "\t\t\t" + str(mov[3]) + "\t\t\t" + str(mov[0]) + "\n"
            print(mov)
        
        self.detail_lbl.config(text=text)

         